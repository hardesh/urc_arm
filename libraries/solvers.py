#!/usr/bin/env python
import numpy as np
# import autograd
import scipy.optimize

from sympy.matrices import Matrix
import sympy as sp

import sys


class fk():
    """
    a forward kinematics class.
    Takes in list of link lengths and angles
    
    Assumptions:    All rotations are about z-axis.
                    Translation is about x-axis.
    The assumptions are taken according to the D-H parameters. 
    """
    def __init__(self,lengths, angles):

        if len(lengths) != len(angles):
            print("Invalid Arguments Passed to fk object!")
            sys.exit()

        self.lengths = lengths      # these are link lengths of the arm
        self.angles = angles        # these are initial angles

        self.q = sp.Symbol("q")
        self.l = sp.Symbol("l")
        
        self.final_T = np.identity(3)
        # after substitution use evalf to calculate the value of the expression

        self.T_a = Matrix([[sp.cos(self.q),-sp.sin(self.q),0],[sp.sin(self.q),sp.cos(self.q),0],[0,0,1]]) # T angle
        self.T_x = Matrix([[1,0,self.l],[0,1,0],[0,0,1]])

        print("FK class initialized")

    def forward_kinematics(self):
        temp_T = Matrix.eye(3)
        for i in range(len(self.lengths)):
            angle_mat = self.T_a.subs(self.q,self.angles[i]).evalf()
            len_mat = self.T_x.subs(self.l,self.lengths[i]).evalf()
            temp_T = temp_T * angle_mat * len_mat
        
        self.final_T = np.array(temp_T,dtype=float)
        
        return self.final_T

    def get_pos(self,angles=None):
        """
        Takes 9ms to return the value

        returns the co-ordinates of the end point of the end effector
        """
        if angles != self.angles and angles != None:
            self.forward_kinematics()
            return [self.final_T[0][2],self.final_T[1][2],0]
        else:
            self.forward_kinematics()
            return [self.final_T[0][2],self.final_T[1][2],0]
    
    def get_sym_matrix(self):
        """
        Returns symbolic form of the forward kinematics matrix
        """
        temp_T = Matrix.eye(3)
        for i in range(len(self.lengths)):
            angle_mat = self.T_a.subs(self.q,self.angles[i]).evalf()
            len_mat = self.T_x.subs(self.l,self.lengths[i]).evalf()
            temp_T = temp_T * angle_mat * len_mat
        
        return temp_T



class ik():
    """
    Inverse Kinematics class for 3 links.
    Pass list of link lengths and list of default joint angles.

    Assumptions:    
    1) All rotations are about z-axis.
    2) Translation is about x-axis.

    Reference:  
    1) https://github.com/AliShug/EvoArm/tree/master/PyIK/src 
    2) https://github.com/lanius/tinyik/tree/master/tinyik
        
    *3) https://github.com/studywolf/blog/blob/master/InvKin/Arm.py
    *4) https://docs.scipy.org/doc/scipy-0.13.0/reference/tutorial/optimize.html#tutorial-sqlsp

    """
    def __init__(self,lengths, ee_pos):
        """
        ee_pos is a 2D list

        q: the initial joint angles of the arm
        self.q0: the default (resting state) joint configuration
        lenths: the arm segment lengths
        """
        self.length = np.asarray(lengths, dtype=np.float32)
        self.ee_pos = np.asarray(ee_pos, dtype= np.float32)
        
        self.q0 = [np.pi/3,-np.pi/4,np.pi/6]
        self.q = self.q0[:]

        # we have to define these properly
        # self.max_angles = [np.pi, np.pi, np.pi/4]
        # self.min_angles = [0, 0, -np.pi/4]


    def inv_kin(self, ee_pos=None):
        """
        Got this from the 3rd reference.

        This is just a quick write up to find the inverse kinematics
        for a 3-link arm, using the SciPy optimize package minimization
        function.

        Given an (x,y) position of the hand, return a set of joint angles (q)
        using constraint based minimization, constraint is to match hand (x,y),
        minimize the distance of each joint from it's default position (q0).

        self.ee_pos : tuple
            the desired self.ee_pos position of the arm

        returns : list
            the optimal [shoulder, elbow, wrist] angle configuration
        """

        if ee_pos != None:
            self.ee_pos = ee_pos
        else:
            ee_pos = self.ee_pos
        
        def distance_to_default(q, *args):
            """Objective function to minimize
            Calculates the euclidean distance through joint space to the
            default arm configuration. The weight list allows the penalty of
            each joint being away from the resting position to be scaled
            differently, such that the arm tries to stay closer to resting
            state more for higher weighted joints than those with a lower
            weight.

            q : np.array
                the list of current joint angles

            returns : scalar
                euclidean distance to the default arm position
            """
            # weights found with trial and error,
            # get some wrist bend, but not much
            weight = [1, 1, 1.3]
            return np.sqrt(np.sum([(qi - q0i)**2 * wi
                           for qi, q0i, wi in zip(q, self.q0, weight)]))

        def x_constraint(q,ee_pos):
            """Returns the corresponding hand self.ee_pos coordinates for
            a given set of joint angle values [shoulder, elbow, wrist],
            and the above defined arm segment lengths, L

            q : np.array
                the list of current joint angles
            self.ee_pos : np.array
                current self.ee_pos position (not used)

            returns : np.array
                the difference between current and desired x position
            """
            x = (self.length[0]*np.cos(q[0]) + self.length[1]*np.cos(q[0]+q[1]) +
                 self.length[2]*np.cos(np.sum(q))) - self.ee_pos[0]
            return x

        def y_constraint(q,ee_pos):
            """Returns the corresponding hand self.ee_pos coordinates for
            a given set of joint angle values [shoulder, elbow, wrist],
            and the above defined arm segment lengths, L

            q : np.array
                the list of current joint angles
            self.ee_pos : np.array
                current self.ee_pos position (not used)
            returns : np.array
                the difference between current and desired y position
            """
            y = (self.length[0]*np.sin(q[0]) + self.length[1]*np.sin(q[0]+q[1]) +
                 self.length[2]*np.sin(np.sum(q))) - self.ee_pos[1]
            return y

        def joint_limits_upper_constraint(q,ee_pos):
            """Used in the function minimization such that the output from
            this function must be greater than 0 to be successfully passed.

            q : np.array
                the current joint angles
            self.ee_pos : np.array
                current self.ee_pos position (not used)

            returns : np.array
                all > 0 if constraint matched
            """
            return self.max_angles - q

        def joint_limits_lower_constraint(q,ee_pos):
            """Used in the function minimization such that the output from
            this function must be greater than 0 to be successfully passed.

            q : np.array
                the current joint angles
            self.ee_pos : np.array
                current self.ee_pos position (not used)

            returns : np.array
                all > 0 if constraint matched
            """
            return q - self.min_angles

        return scipy.optimize.fmin_slsqp(
            func=distance_to_default,
            x0=self.q,
            eqcons=[x_constraint,
                    y_constraint],
            # uncomment to add in min / max angles for the joints
            # ieqcons=[joint_limits_upper_constraint,
            #          joint_limits_lower_constraint],
            args=(self.ee_pos,),
            iprint=0)  # iprint=0 suppresses output
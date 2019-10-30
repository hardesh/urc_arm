#!/usr/bin/env python
import numpy as np
# import autograd

from sympy.matrices import Matrix
import sympy as sp

import sys

class fk():
    """
    This is a forward kinematics class. 
    Takes in list of link lengths and angles
    
    Assumptions: All rotations are about z-axis.
                Translation is about x-axis.
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
        returns the co-ordinates of the end point of the end effector
        """
        if angles != self.angles and angles != None:
            self.forward_kinematics()
            return [self.final_T[0][2],self.final_T[1][2],0]
        else:
            self.forward_kinematics()
            return [self.final_T[0][2],self.final_T[1][2],0]
        

class ik():
    def __init__(self,lengths, ee_pos):
        """
        pass links lenght array, limits,  

        use this for reference: https://github.com/AliShug/EvoArm/tree/master/PyIK/src 
        https://github.com/lanius/tinyik/tree/master/tinyik
        """
        
        pass
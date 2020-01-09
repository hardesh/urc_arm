#!/usr/bin/env python
import rospy
import math
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Point

class Kin():
    def __init__(self):
        #lengths in meters
        self.x = 0
        self.y = 0
        self.l1 = 293.39 * (10**-3)
        self.l2 = 240.49 * (10**-3)
        self.k1 = 154.02 * (10**-3)
        self.k2 = 94.09 * (10**-3)
        self.a1 = self.l1
        self.a2 = self.l2
        self.q1 = 0
        self.q2 = 0
        self.f = math.radians(30.35)
        self.x_max = 2
        self.y_max = 2
        self.x_min = 0.5
        self.y_min = 0.5
       	self.q1_max = 1
       	self.q1_min = 1
       	self.q2_max = 1
       	self.q2_min = 1

        self.is_xy_not_set = True
        
        self.pub = rospy.Publisher("final_ext", Point, queue_size=1)
        #plot
        self.pub2 = rospy.Publisher("plot1", Point, queue_size=1)
        self.pub3 = rospy.Publisher("plot2", Point, queue_size=1)
        #plot
        self.sub1 = rospy.Subscriber("current_ext", Point, self.curr_ext_callback)
        self.sub2 = rospy.Subscriber("joy", Joy, self.joy_callback)

    def forward_kinematics(self):
        self.x = self.l1*math.cos(self.q1) + self.l2*math.cos(self.q1+self.q2)
        self.y = self.l1*math.sin(self.q1) + self.l2*math.sin(self.q1+self.q2)

    def inverse_kinematics(self):
        m = (self.x**2+self.y**2-self.l1**2-self.l2**2)/(2*self.l1*self.l2)
        if m < 1:
            print(self.x, self.y)
        try:
            self.q2 = -math.acos((self.x**2+self.y**2-self.l1**2-self.l2**2)/(2*self.l1*self.l2))
            self.q1 = math.atan(self.y/self.x)+math.atan((self.l2*math.sin(self.q2))/(self.l1+self.l2*math.cos(self.q2)))

            p1 = math.pi - self.q1 - self.f
            p2 = math.pi - self.q1
            self.a1 = math.sqrt(self.k1**2+self.l1**2-2*self.k1*self.l1*math.cos(p1))
            self.a2 = math.sqrt(self.k2**2+self.l2**2-2*self.k2*self.l2*math.cos(p2))

            print("q1",math.degrees(self.q1))
            print("q2",math.degrees(self.q2))
            print("a1",math.degrees(self.a1))
            print("a2",math.degrees(self.a2))
            #plot
            self.pub2.publish(self.q1,self.q2,0)
            self.pub3.publish(self.a1,self.a2,0)
            #plot

        except Exception as e:
            print(e)
        

    def curr_ext_callback(self, msg):
        if self.is_xy_not_set:
        	#conversion from inches to m, and added the link length
            self.a1 = (msg.x * 0.0254) + 0.265
            self.a2 = (msg.y * 0.0254) + 0.265
            p1 = math.acos((self.k1**2+self.l1**2-self.a1**2)/(2*self.k1*self.l1))
            p2 = math.acos((self.k2**2+self.l2**2-self.a2**2)/(2*self.k2*self.l2))
            self.q1 = math.pi-(self.f+p1)
            self.q2 = -(math.pi-p2)
            self.forward_kinematics()
            self.is_xy_not_set = False

    # indexes not checked
    def joy_callback(self, msg):
        if(msg.axes[0] < -0.5 and self.x < self.x_max ):
            self.x += 0.005
        elif(msg.axes[0] > 0.5 and self.x > -self.x_max ):
            self.x -= 0.005
        if(msg.axes[1] > 0.5 and self.y < self.y_max):
            self.y += 0.005
        elif(msg.axes[1] < -0.5 and self.y > -self.y_max):
            self.y -= 0.005

        try:
            self.inverse_kinematics()
            self.pub.publish((self.a1 - 0.265)/0.0254, (self.a2 - 0.265)/0.0254, 0)
        except Exception as e:
            print(e)
            # pass

if __name__ == "__main__":
    rospy.init_node("arm_node")
    kin = Kin()
    rospy.spin()


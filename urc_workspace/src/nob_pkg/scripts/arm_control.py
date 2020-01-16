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
        self.f = math.radians(30.35)
        self.x_max = 0.7
        self.y_max = 0.7

        self.is_xy_not_set = True
        
        self.pub = rospy.Publisher("final_ext", Point, queue_size=1)
        self.sub1 = rospy.Subscriber("current_ext", Point, self.curr_ext_callback)
        self.sub2 = rospy.Subscriber("joy", Joy, self.joy_callback)

    def forward_kinematics(self, q1, q2):
        x = self.l1*math.cos(q1) + self.l2*math.cos(q1+q2)
        y = self.l1*math.sin(q1) + self.l2*math.sin(q1+q2)
        return x, y

    def inverse_kinematics(self):
        m = (self.x**2+self.y**2-self.l1**2-self.l2**2)/(2*self.l1*self.l2)
        if m < 1:
            print(self.x, self.y)
        try:
            self.q2 = math.acos((self.x**2+self.y**2-self.l1**2 -
                        self.l2**2)/(2*self.l1*self.l2))
            self.q1 = math.atan(self.y/self.x)-math.atan((self.l2 * math.sin(self.q2))/(self.l1+self.l2*math.cos(self.q2)))

            p1 = self.q1 - math.pi + self.f
            p2 = self.q2 + math.pi
            a1 = math.sqrt(self.k1**2+self.l1**2-2*self.k1*self.l1*math.cos(p1))
            a2 = math.sqrt(self.k2**2+self.l2**2-2*self.k2*self.l2*math.cos(p2))

            print("q1",math.degrees(self.q1))
            print("q2",math.degrees(self.q2))

            return a1, a2

        except Exception as e:
            print(e)
        

    def curr_ext_callback(self, msg):
        if self.is_xy_not_set:
            a1 = msg.x
            a2 = msg.y
            p1 = math.acos((self.k1**2+self.l1**2-a1**2)/(2*self.k1*self.l1))
            p2 = math.acos((self.k2**2+self.l2**2-a2**2)/(2*self.k2*self.l2))
            q1 = math.pi-(self.f+p1)
            q2 = -(math.pi-p2)
            self.x, self.y = self.forward_kinematics(q1, q2)
            self.is_xy_not_set = False

    # indexes not checked
    def joy_callback(self, msg):
        if(msg.axes[0] > 0.5 and self.x < self.x_max):
            self.x += 0.005
        elif(msg.axes[0] < -0.5 and self.x > -self.x_max):
            self.x -= 0.005
        if(msg.axes[-1] > 0.5 and self.y < self.y_max):
            self.y += 0.005
        elif(msg.axes[-1] < -0.5 and self.y > -self.y_max):
            self.y -= 0.005

        try:
            a1, a2 = self.inverse_kinematics()
        except Exception as e:
            print(e)
            # pass
        self.pub.publish(a1, a2, 0)



if __name__ == "__main__":
    rospy.init_node("arm_node")
    kin = Kin()
    rospy.spin()


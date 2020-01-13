#!/usr/bin/env python
import rospy
import math
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Point
import time


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
        self.q1 = math.radians(60)
        self.q2 = -math.radians(60)
        self.q1_prev = self.q1
        self.q2_prev = self.q2
        self.f = math.radians(30.35)
        self.x_max = 2
        self.y_max = 2
        self.x_min = 0.5
        self.y_min = 0.5

        self.pub = rospy.Publisher("final_ext", Point, queue_size=1)
        self.pub2 = rospy.Publisher("plot1", Point, queue_size=1)
        self.sub = rospy.Subscriber("joy", Joy, self.joy_callback)

        #initialize
        p1 = math.pi - self.q1 - self.f
        p2 = math.pi + self.q2
        self.a1 = math.sqrt(self.k1**2+self.l1**2-2 *
                            self.k1*self.l1*math.cos(p1))
        self.a2 = math.sqrt(self.k2**2+self.l2**2-2 *
                            self.k2*self.l2*math.cos(p2))
    
    def forward_kinematics(self):
        x = self.l1*math.cos(self.q1) + \
                self.l2*math.cos(self.q1-self.q2)
        y = self.l1*math.sin(self.q1) + \
                self.l2*math.sin(self.q1-self.q2)
        return x,y

    def inverse_kinematics(self):
        m = (self.x**2+self.y**2-self.l1**2-self.l2**2)/(2*self.l1*self.l2)
        if m < 1:
            print(self.x, self.y)
        try:
            self.q2 = -math.acos((self.x**2+self.y**2 -
                                  self.l1**2-self.l2**2)/(2*self.l1*self.l2))
            self.q1 = math.atan(self.y/self.x)+math.atan((self.l2 *
                                                          math.sin(self.q2))/(self.l1+self.l2*math.cos(self.q2)))
            
            x,y = self.forward_kinematics()
            if (x < 0 or self.q1 < 0):
                self.q1 = self.q1_prev
                self.q2 = self.q2_prev
                self.x, self.y = self.forward_kinematics()
            else:
                self.q1_prev = self.q1
                self.q2_prev = self.q1

            p1 = math.pi - self.q1 - self.f
            p2 = math.pi + self.q2
            self.a1 = math.sqrt(self.k1**2+self.l1**2-2 *
                                self.k1*self.l1*math.cos(p1))
            self.a2 = math.sqrt(self.k2**2+self.l2**2-2 *
                                self.k2*self.l2*math.cos(p2))

            print("q1", math.degrees(self.q1))
            print("q2", math.degrees(self.q2))
            print("a1", math.degrees(self.a1))
            print("a2", math.degrees(self.a2))
            # plot
            self.pub2.publish(self.q1, self.q2, 0)
            # plot

        except Exception as e:
            print(e)

    # indexes not checked
    def joy_callback(self, msg):
        if(msg.axes[0] < -0.5 and self.x < self.x_max):
            self.x += 0.0005
        elif(msg.axes[0] > 0.5 and self.x > -self.x_max):
            self.x -= 0.0005
        if(msg.axes[1] > 0.5 and self.y < self.y_max):
            self.y += 0.0005
        elif(msg.axes[1] < -0.5 and self.y > -self.y_max):
            self.y -= 0.0005

        try:
            self.inverse_kinematics()
            self.pub.publish((self.a1 - 0.265)/0.0254,
                             (self.a2 - 0.265)/0.0254, 0)
        except Exception as e:
            print(e)
            # pass


if __name__ == "__main__":
    rospy.init_node("arm_node")
    kin = Kin()
    rate = rospy.Rate(10)
    kin.x,kin.y = kin.forward_kinematics()
    while not rospy.is_shutdown():
        kin.pub.publish((kin.a1 - 0.265)/0.0254, (kin.a2 - 0.265)/0.0254, 0)
        kin.pub2.publish(kin.q1, kin.q2, 0)
        print("published {} {}".format(kin.x,kin.y))
        rate.sleep()
    rospy.spin()

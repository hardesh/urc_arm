#!/usr/bin/env python
import rospy
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from nob_pkg.msg import JointValues

def callback(msg):
    global t1,t2,t3
    t1 = msg.a
    t2 = msg.b
    t3 = msg.c

rospy.init_node("plotter_node")
rospy.Subscriber("joint_values", JointValues, callback)

#link lenghts
l1 = 10
l2 = 10
l3 = 10

#initial joint angles
t1 = 0
t2 = 0
t3 = 0

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    ax1.clear()
    x1 = l1*math.cos(t1)
    y1 = l1*math.sin(t1)
    x2 = x1 + l2*math.cos(t2)
    y2 = y1 + l2*math.sin(t2)
    x3 = x2 + l3*math.cos(t3)
    y3 = y2 + l3*math.sin(t3)

    ax1.plot([0,x1],[0,y1])
    ax1.plot([x1,x2],[y1,y2])
    ax1.plot([x2,x3],[y2,y3])
    plt.xlim([-l1-l2-l3,l1+l2+l3])
    plt.ylim([-l1-l2-l3,l1+l2+l3])
    ax1.grid()
    
ani = animation.FuncAnimation(fig, animate, interval=100)    
plt.show()

rospy.spin()

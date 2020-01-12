#!/usr/bin/env python
import rospy
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from geometry_msgs.msg import Point

def callback1(msg):
    print("called1")
    global q1,q2,q3
    q1 = msg.x
    q2 = msg.y
    q3 = msg.z

rospy.init_node("plotter_node")
rospy.Subscriber("plot1", Point, callback1)

#link lenghts
    
a1 = 293.39 * (10**-3)
a2 = 240.49 * (10**-3)

#initial joint angles
q1 = 0
q2 = 0
q3 = 0

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    ax1.clear()
    x1 = a1*math.cos(q1)
    y1 = a1*math.sin(q1)
    x2 = x1 + a2*math.cos(q2)
    y2 = y1 + a2*math.sin(q2)

    ax1.plot([0,x1],[0,y1])
    ax1.plot([x1,x2],[y1,y2])
    plt.xlim([-a1-a2,a1+a2])
    plt.ylim([-a1-a2,a1+a2])
    ax1.grid()
    
ani = animation.FuncAnimation(fig, animate, interval=100)    
plt.show()

rospy.spin()

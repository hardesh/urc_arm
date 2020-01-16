#!/usr/bin/env python
import rospy
# from std_msgs.msg import String, Float64
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist


V_MAX = 10
OMEGA_MAX = 2


def joy_sub_cb(joymsg):
    # print joymsg.axes
    # twist = Twist()
    global twist
    twist = Twist()
    x_coordi = joymsg.axes[1]
    y_coordi = joymsg.axes[0]

    if abs(x_coordi) < 0.2:
        x_coordi = 0
    if abs(y_coordi) < 0.2:
        y_coordi = 0

    twist.linear.x = x_coordi * 10
    twist.angular.z = y_coordi * 2

    # print(twist)
    # print(twist.linear.x)

    #vel_pub.publish(twist)


if __name__ == "__main__":
    rospy.init_node('Manual_Drive')
    r = rospy.Rate(10)

    vel_pub = rospy.Publisher("cmd_vel", Twist, queue_size = 1)

    # twist = Twist()

    while not rospy.is_shutdown():
        global twist    
        subtojoy = rospy.Subscriber('joy', Joy, joy_sub_cb)
        vel_pub.publish(twist)
        r.sleep()
    
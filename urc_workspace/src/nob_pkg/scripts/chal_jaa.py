#!/usr/bin/env python
import rospy
from std_msgs.msg import String, Float64
from sensor_msgs.msg import Joy

rospy.init_node('use')
r = rospy.Rate(2)

pub1 = rospy.Publisher("chal_jaa_x", Float64, queue_size=1)
pub2 = rospy.Publisher("chal_jaa_y", Float64, queue_size=1)

def joy_sub_cb(joymsg):
    # print joymsg.axes
    x_coordi = joymsg.axes[0]
    y_coordi = joymsg.axes[1]
    # pub_str = "!"+ ":" + str(x_coordi) + ":" + str(y_coordi) + ':'
    pub1.publish(x_coordi)
    pub2.publish(y_coordi)


while not rospy.is_shutdown():
    
    subtojoy = rospy.Subscriber('joy', Joy, joy_sub_cb)
    r.sleep()
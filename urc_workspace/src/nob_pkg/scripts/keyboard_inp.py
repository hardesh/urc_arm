#!/usr/bin/env python

import sys
import rospy
from std_msgs.msg import String
import pygame


if __name__ == '__main__':
    rospy.init_node("keyboard_driver")
    key_pub = rospy.Publisher('keys', String, queue_size=1)
    rate = rospy.Rate(20)

    pygame.init()
    pygame.display.set_mode((200,200))


    while not rospy.is_shutdown():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    key_pub.publish("w")
                if event.key == pygame.K_s:
                    key_pub.publish("s")
                if event.key == pygame.K_x:
                    key_pub.publish("x")
                if event.key == pygame.K_UP:
                    key_pub.publish("i")
                if event.key == pygame.K_DOWN:
                    key_pub.publish("k")
        
        rate.sleep()
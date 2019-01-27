#!/usr/bin/env python

import rospy 
import sensor_msgs.msg
import geometry_msgs.msg
import moveit_commander
import moveit_msgs.msg
import sys


class move_arm():
    def __init__(self):
        self.arm = moveit_commander.RobotCommander()   # provides information such as model and joint states
        self.scene = moveit_commander.PlanningSceneInterface() # provides a remote interface for getting, setting, and updating the robot’s internal understanding of the surrounding world
        self.group_name = "armbot"
        self.move_group = moveit_commander.MoveGroupCommander(group_name)
        
        self.publishers()


    def publishers(self):
        self.display_trajectory = rospy.Publisher("/move_group/display_planned_path",moveit_msgs.msg.DisplayTrajectory,queue_size=10)
        
    # def joint_state_to_plan(self):         # plans path according to the joint states given
    #     self.joint_goal = self.move_group.get_current_joint_values()
    #     self.joint_goal[0] = 0
    #     self.joint_goal[1] = -pi/4
    #     self.joint_goal[2] = 0
    #     self.joint_goal[3] = -pi/2
    #     self.joint_goal[4] = 0
    #     self.joint_goal[5] = pi/3
    #     self.joint_goal[6] = 0

    #     self.move_group.go(joint_goal, wait=True)
    #     self.move_group.stop()

    def plan_according_to_pose(self,x_pos,y_pos,z_pos):
        self.pose_goal = geometry_msgs.msg.Pose()
        self.pose_goal.position.x = x_pos
        self.pose_goal.position.y = y_pos
        self.pose_goal.position.z = z_pos
        self.move_group.set_pose_target(self.pose_goal)

        plan = self.move_group.go(wait=True)

        self.move_group.stop()

        # self.move_group.clear_pose_targets()   # clears the pose targets given to move_group interface

        


if __name__ == "__main__":
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node('armbot_inv_kin', anonymous=True)
    halwa_robot = move_arm()

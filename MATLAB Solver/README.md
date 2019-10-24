# urc_arm

The folder Arm contains the codes used for finding the link lenghts.

arm_link_solve has some issues that need to be solved in order to use


base is attached at 50cm, link lenghts - (50cm,40cm), gripper-27cm  


|       i    |   Theta(about z)   |   d(along z)  |  a(along x)  |   alpha(about x)  |
|------------|:------------------:|:-------------:|:------------:|:-----------------:|
|       1    |   q1(constrained)  |       0       |     0.5 m    |         0         |       
|       2    |   q2(constrained)  |       0       |    0.4  m    |         0         |
|       3    |         q3         |       0       |    0.27 m    |         0         |


i = 3 is gripper.

Angles q1 and q2 are constrained due to the linear actuator. 

![](https://raw.githubusercontent.com/hardesh/urc_arm/master/MATLAB%20Solver/workspace.png "wrk_spc")

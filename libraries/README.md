## Libraries:

Solvers - Contains forward kinematics solver and inverse kinematics solver

#### Dependencies:
- numpy
- pandas
- scipy
- sympy

To install the dependencies use:
```
pip2 install --user $LIBRARY
```

Example:
```
>>> from solvers import *
>>> my_fk = fk([50,40,30],[np.pi/3,-np.pi/3,-np.pi/6])
    # first array is link lengths, sencond array is default joint angles

>>> my_ik = ik([50,40,30],ee_coords)
>>> my_ik.inv_kin()
```


Joystick Inputs and their use:
- Left Joystick (Movement in X-Y plane)
- Right Joystick (Movement of the base motor)  
- Up-Down-Left-Right Button (Movement in Z direction)
- LB and RB for gripper rotation
- X to close gripper and B to open the gripper
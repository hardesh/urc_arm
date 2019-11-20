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
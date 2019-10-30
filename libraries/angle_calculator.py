#!/usr/bin/env python
import numpy as np

from solvers import *

my_fk = fk([50,40,30],[0,np.pi/2,-np.pi/2])

# temp = my_fk.forward_kinematics()
temp = my_fk.get_pos()
print(temp)
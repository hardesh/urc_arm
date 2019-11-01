#!/usr/bin/env python
import numpy as np
import sympy

import time

from solvers import *

start = time.time()
my_fk = fk([50,40,30],[np.pi/3,-np.pi/3,-np.pi/6])

# temp = my_fk.forward_kinematics()
temp = my_fk.get_pos()
print(temp)
# done = time.time()

# print("diff",done-start)

# q1 = sympy.Symbol("q1")
# q2 = sympy.Symbol("q2")

# new_fk = fk([50,40,30],[q1,q2,0])
# temp = new_fk.get_sym_matrix()


# new_temp = sympy.solve([temp[2]-80,temp[5]-40],dict=True)
# print(new_temp)


my_ik = ik([50,40,30],[90,20])
temp = my_ik.inv_kin()
temp = temp * 180 / np.pi
print(temp)

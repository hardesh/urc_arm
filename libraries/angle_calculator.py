#!/usr/bin/env python
import numpy as np
import sympy
import pandas as pd

import time

from solvers import *

start = time.time()
my_fk = fk([50,40,30],[np.pi/3,-np.pi/3,-np.pi/6])

# temp = my_fk.forward_kinematics()
# temp = my_fk.get_pos()
# print(temp)
# done = time.time()

# print("diff",done-start)

q1 = sympy.Symbol("q1")
q2 = sympy.Symbol("q2")

new_fk = fk([50,40,30],[q1,q2,0])
temp = new_fk.get_sym_matrix()

# new_temp = sympy.solve([temp[2]-80,temp[5]-40],dict=True)
print(sympy.simplify(temp[2]))


list_ee = [[60,-50],[60,-30],[60,30],[60,40],\
    [60,50],[70,-50],[70,20],[70,30],[70,40],[70,50],\
    [80,0],[80,-20],[80,-30],[80,-50],[80,20],[80,30],\
    [80,50]]
my_ik = ik([50,40,30],list_ee[0])

dataframe_dict = {"angle1":[],"angle2":[],"angle3":[],"ee_pos":[]}


for i in range(len(list_ee)):    
    temp = my_ik.inv_kin(list_ee[i])
    temp = temp * 180 / np.pi
    # temp[1] = temp[1] + 180
    # print(temp),
    # print("for"),
    # print(list_ee[i])
    dataframe_dict["angle1"].append(temp[0])
    dataframe_dict["angle2"].append(temp[1])
    dataframe_dict["angle3"].append(temp[2])
    dataframe_dict["ee_pos"].append(list_ee[i])

dataframe = pd.DataFrame(data=dataframe_dict)
# print(dataframe)
# print(dataframe.max())
# print(dataframe.min())
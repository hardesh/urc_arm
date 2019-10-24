
import tinyik
import numpy as np


arm = tinyik.Actuator(['z', [0.5, 0.0, 0.0], 'z', [0.4, 0.0, 0.0],'z', [0.27,0.0,0.0]])
print(arm.ee)
# for complete expansion
arm.ee = [0.6,0.,0.0]
angles1 =  np.round(np.rad2deg(arm.angles))
print(angles1)
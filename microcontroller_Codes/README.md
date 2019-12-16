# Microcontroller Codes:

Microcontroller used for these codes: ESP-32


To use these scripts:
1. Connect to the hostspot created by ESP-32
2. run:
```
roslaunch rosserial_server socket.launch
```

You'll be able to see the topics published/subscribed by the microcontroller.

To use the arm controller, run the __keyboard_inp__ node from the nob_pkg in urc_workspace.
To use the drive controller, run __chal_jaa__ node from the nob_pkg in urc_workspace.

```bash
cd urc_workspace
catkin build
source devel/setup.bash

# To run the keyboard_inp node
rosrun nob_pkg keyboard_inp.py

# To run the chal_jaa node 
rosrun nob_pkg chal_jaa.py

```
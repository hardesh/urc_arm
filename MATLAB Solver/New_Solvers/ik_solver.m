robot = rigidBodyTree('DataFormat','column','MaxNumBodies',4);

body1 = rigidBody('b1'); 

jnt1 = rigidBodyJoint('jnt1','revolute');
body1.Joint = jnt1;

basename = robot.BaseName;
addBody(robot,body1,basename);

showdetails(robot)

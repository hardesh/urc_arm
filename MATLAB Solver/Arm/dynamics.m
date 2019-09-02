% this program is used to find the joint torque values for a planer 2 DOF robotic manipulator

clear
clc

syms g a1 a2 q1 q2 q1d q2d q1dd q2dd l1 l2 m1 m2 torque1 torque2 i1 i2


%a1 = [-(l1/2) * q1d^2;(l1/2)*q1dd;0];

%a2 = [-l1*q1d^2*cos(q2)+l1*q1dd*sin(q2)-l2*(q1d+q2d)^2;l1*(q1d^2)*sin(q2)+l1*q1dd*cos(q2)-l2*(q1dd+q2dd)];

torque2 = i2*(q1dd+q2dd) + m2*l1*(l2/2)*sin(q2)*(q1d^2) + m2*l1*(l2/2)*cos(q2)*q1dd + ...
			m2*((l2/2)^2)*(q1dd+q2dd) + m2 * (l2/2) * g * cos(q2+q2);
		
		
torque1 = (m1*((l1/2)^2) + m2*(l1^2 +((l2/2)^2)+2*l1*((l2/2)^2)+2*l1*(l2/2)*cos(q2))+i1+i2) * q1dd+ ...
			(m2 *(((l2/2)^2)+l1*(l2/2)*cos(q2))+i2) * q2dd + ...
			2 * (-m2*l1*(l2/2)*sin(q2)) * q1d *q2d + (q2d^2) * (-m2*l1*(l2/2)*sin(q2)) + ...
			(m1*(l1/2)+m2*l1)*g*cos(q1) + m2 * (l2/2) * g * cos(q1+q2);
 
% Accl. due to gravity        
g = 9.8;
% Initial Joint Angles        
q1 = 0;
q2 = 0;
% Angular Vel.
q1d = 10;
q2d = 10;
% Angular accl.
q1dd = 2;
q2dd = 2;
% Worst Case Mass of 
m1 = 2;
m2 = 2;
% Link Lengths
l1 = 0.50;
l2 = 0.40;
% Moment of Inertias
i1 = ( m1 * (l1^2) )/12;
i2 = ( m2 * (l2^2) )/12;

eval(subs(torque1))
eval(subs(torque2))

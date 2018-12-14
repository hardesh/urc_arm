function arm_link_solve()

clc
clear all

%initializations
%max_work_len = 0.8;
%max_work_bre = 0.8;
%max_work_height = 1.8;

syms x1 x2 x3 y1 y2 y3;

syms theta1 theta2 theta3;
thetas = [theta1 theta2 theta3];

%symbolic expressions of phi1 and phi2
phi1 = theta1 + theta2 - pi;
phi2 = 2*pi - theta1 - theta2 - theta3;

%link lengths
syms l1 l2 l3

%joint co-ordinates
x1 = l1 * cos(theta1); 
y1 = l1 * sin(theta1);

x2 = x1 + l2 * cos(phi1);
y2 = y1 + l2 * sin(phi1);

x3 = x2 + l3 * cos(phi2);
y3 = y2 - l3 * sin(phi2);

joint_1 = [x1 y1];
joint_2 = [x2 y2];
joint_3 = [x3 y3];

%theta1 = pi/2; theta2 = pi/2; theta3 = pi/2;
%l1 = 2; l2 =2 ; l3 =2;

params = zeros(1,6);

l1 = 0.21;
l2 = 0.24;
l3 = 0.16;
count = 0;
for l1 = 0.2:0.03:0.50
    
    %considering theta1 in bet 0 and 90
    theta1 =0;
    %considering theta2 in bet 45 to 135 deg
    theta2 = pi / 4;
    %considering theta3 in bet 90 and 150 deg
    theta3 = pi / 2;

    count = count + 1
        
    if count < 10
        l2 = l2 + 0.02;        %incrementing link lengths l2 and l3
        l3 = l3 + 0.01;
        continue
    end
    
    for theta1_deg = 0:10:90
        
        for theta2_deg = 45:10:135
        
            for theta3_deg = 90:10:180
                
                theta1 = (pi/180) * theta1_deg;     % degree to radian convertion
                theta2 = (pi/180) * theta2_deg;
                theta3 = (pi/180) * theta3_deg;
                
                point = eval(subs(joint_3));
                plot(point(1),point(2),'ro','MarkerSize',2);
                grid on;
                
                hold on;
                
                if point(2) > 1.2 && point(1) > 0.8    % changed 1.8 to 1.2 since the arm is already going to be high
                    params_new = zeros(1,6);
                    params_new(1) = l1;
                    params_new(2) = l2;
                    params_new(3) = l3;
                    params_new(4) = theta1;
                    params_new(5) = theta2;
                    params_new(6) = theta3;
                    params_new
                    
                    plot(point(1),point(2),'bo')      % plotting end effector
                   
                    point1 = eval(subs(joint_2));
                    plot(point1(1),point1(2),'bo')    %plotting joints
                    point2 = eval(subs(joint_1));
                    plot(point2(1),point2(2),'bo')
                    
                    pt1 = eval(subs(joint_1));
                    pt2 = eval(subs(joint_2));
                    pt3 = eval(subs(joint_3));
                    
                    plot([0 pt1(1)],[0 pt1(2)],'b');
                    plot([pt1(1) pt2(1)],[pt1(2) pt2(2)],'b');
                    plot([pt2(1) pt3(1)],[pt2(2) pt3(2)],'b');
                    
                    %plot([point1(1) point(1)],[point1(2) point(2)],'b')        %plotting the line joing the 2 joints
                    %plot([point1(1) point2(1)],[point1(2) point2(2)],'b')
                    
                    %plot([0 point2(1)],[0 point2(2)],'b')
                    
                    %hold on;
                    params = cat(1,params,params_new)
                end
            
            end
            
        end
        
    end
   l2 = l2 + 0.02;
   l3 = l3 + 0.01;
    
end
%subs(joint_3)
%whos

params

end

					%  D-H TABLE %
%   i   theta   d    a    alpha
%   1    q1     0    l1   0
%   2    q2     0    l2   0

clc
clear

%syms l1 l2 l3 q1 q2 q3 theta

% initializations
links = 2;
%a = [l1 l2 l3];
%theta = [q1 q2 -q3];
alpha = [0 0 0];
d = [0 0 0];

%fk_obj = fk(links,a,alpha,d,theta);
%fk_obj
l2 = 0.46;
%l3 = 0.24;

params = zeros(1,2);
params_new = zeros(1,2);

count = 0;
for l1 = 0.5:0.03:0.65
    count = count + 1
    
    if count < 4
        l2 = l2 + 0.02;
        %l3 = l3 + 0.01;
        continue
    end
        
    for q1 = 0:15:90
       
        for q2 = -75:15:75
                
                q1_rad = deg2rad(q1);
                q2_rad = deg2rad(q2);
                %q3_rad = deg2rad(q3);
                
                a = [l1 l2];
                theta = [q1_rad q2_rad];
                
                fk_obj = fk(links,a,alpha,d,theta);
                ee = fk_obj(1:3,4);
                ee_x = ee(1); 
                ee_y = ee(2);
                
                plot(ee_x,ee_y,'ro','MarkerSize',4);  %plotting every point
                grid on
                hold on
                if ee_x > 0.6 && ee_y > 0.8   %condition for checking the end effector
                   
                    plot(ee_x,ee_y,'b*','MarkerSize',6);
                    
                    joint_1_x = l1 * cos(q1_rad);
                    joint_1_y = l1 * sin(q1_rad);
                    joint_2_x = joint_1_x + l2 * cos(q1_rad+q2_rad);
                    joint_2_y = joint_1_y + l2 * sin(q1_rad+q2_rad);
                    %joint_3_x = joint_2_x + l3 * cos(q1_rad+q2_rad+q3_rad);
                    %joint_3_y = joint_2_y + l3 * sin(q1_rad+q2_rad+q3_rad);
                    
                    plot([0 joint_1_x],[0 joint_1_y],'b');
                    plot([joint_2_x joint_1_x],[joint_2_y joint_1_y],'b');
                    %plot([joint_2_x joint_3_x],[joint_2_y joint_3_y],'b');
                    
                    params_new = [l1 l2];
                    ee_x
                    ee_y

                    params = cat(1,params,params_new);
                
                end
            
        end
        
    end
    l2 = l2 + 0.02;

    
end

params

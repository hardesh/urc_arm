//retraction on postive

#include <ros.h>
#include <sensor_msgs/Joy.h>
#include <std_msgs/String.h>

#define DIR1 6
#define PWM1 12
#define DIR2 7
#define PWM2 13

int vel1,vel2;

void callback(const sensor_msgs::Joy& msg)
{
  float x = msg.axes[1];
  if(x>0.8){
    digitalWrite(DIR1,LOW);
    vel1 = 255;
  }
  else if(x<-0.8){
    digitalWrite(DIR1,HIGH);
    vel1 = 255;
  }
  else{
    vel1 = 0;
  }
  
  float y = msg.axes[4];
  if(y>0.8){
    digitalWrite(DIR2,LOW);
    vel2 = 255;
  }
  else if(y<-0.8){
    digitalWrite(DIR2,HIGH);
    vel2 = 255;
  }
  else{
    vel2 = 0;
  }
}

ros::NodeHandle n;
ros::Subscriber<sensor_msgs::Joy> sub1("joy", callback); 

void setup(){
  pinMode(DIR1,OUTPUT);
  pinMode(PWM1,OUTPUT);
  pinMode(DIR2,OUTPUT);
  pinMode(PWM2,OUTPUT);

  Serial.begin(9600);
  n.initNode();
  n.subscribe(sub1);
}

void loop(){
  analogWrite(PWM1,vel1);
  analogWrite(PWM2,vel2);
  n.spinOnce();
}

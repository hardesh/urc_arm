#include <analogWrite.h>
#include <WiFi.h>
#include <ros.h>
#include <std_msgs/String.h>
#include <std_msgs/Float64.h>
//#include <String.h>
#include <stdlib.h>


// max values
#define MAX_PWM 163
#define MAX_lin 5

// For WiFi access point
const char *ssid = "esp-arm";
const char *password = "123456789";

// Set the rosserial socket server IP address
IPAddress server(192,168,4,2);            // Laptop's IP address
const uint16_t serverPort = 11411;        // Set the rosserial socket server port

ros::NodeHandle nh;

// Make a chatter publisher
std_msgs::String str_msg;
ros::Publisher chatter("chatter", &str_msg);

String key;
// these will kind of store the speed
int lin_act[2];


void KeyboardCb(const std_msgs::String &msgdata){
  key = msgdata.data[0];

  if (key == "w"){
    lin_act[0] += 1;
    if (lin_act[0] > 5) lin_act[0] = MAX_lin;
  }
  else if (key == "s"){
    lin_act[0] = 0;
    lin_act[1] = 0;
  }
  else if (key == "x"){
    lin_act[0] -= 1;
    if (lin_act[0] < -5) lin_act[0] = -MAX_lin;
  }
  else if (key == "k"){
    lin_act[1] -= 1;
    if (lin_act[1] < -5) lin_act[1] = -MAX_lin;
  }
  else if (key == "i"){
    lin_act[1] += 1;
    if (lin_act[1] > 5) lin_act[1] = MAX_lin;
  }
  
}

ros::Subscriber<std_msgs::String> key_sub("keys", &KeyboardCb);

int dirs[2]={0,0};
int pwms[2];
int pwm_pins[2] = {12, 14};
int dir_pins[2] = {27, 26};


void setup()
{
  Serial.begin(115200);
  Serial.println();

  WiFi.softAP(ssid,password);
  IPAddress myIP = WiFi.softAPIP();
  
  // Set the connection to rosserial socket server
  nh.getHardware()->setConnection(server, serverPort);
  nh.initNode();

  // Start to be polite
  nh.advertise(chatter);
  nh.subscribe(key_sub);

  for (int i = 0; i < 2; i++)
  {
    pinMode(pwm_pins[i], OUTPUT);
    pinMode(dir_pins[i], OUTPUT);
  }

  delay(100);   //my_change
}

void loop()
{

  if (nh.connected()) {
    str_msg.data = "Hello!";
    chatter.publish( &str_msg );
    // instead of above data publish the pwm values

    if (lin_act[0] > 0){
      dirs[0] = HIGH;
      pwms[0] = map(abs(lin_act[0]), 0, MAX_lin, 0, 250); // 163 cause 12v  
    }
    else{
      dirs[0] = LOW;
      pwms[0] = map(abs(lin_act[0]), 0, MAX_lin, 0, 250);
    }

    if (lin_act[1] > 0){
      dirs[1] = HIGH;
      pwms[1] = map(abs(lin_act[1]), 0, MAX_lin, 0, 250); // 163 cause 12v  
    }
    else{
      dirs[1] = LOW;
      pwms[1] = map(abs(lin_act[1]), 0, MAX_lin, 0, 250);
    }

    Serial.print(pwms[0]);
    Serial.print(",");
    Serial.println(pwms[1]);

    // Sending commands to motor
    for (int i = 0; i < 2; i++)
    {
      analogWrite(pwm_pins[i], pwms[i]);
      
      if (dirs[i] == LOW) digitalWrite(dir_pins[i], LOW);
      else digitalWrite(dir_pins[i], HIGH);
    }
    
  } else {
    str_msg.data = "Hello, not!";
    chatter.publish( &str_msg );
  }
  nh.spinOnce();
  
  delay(50);
}


#include <analogWrite.h>
#include <WiFi.h>
#include <ros.h>
#include <std_msgs/String.h>
#include <std_msgs/Float64.h>

//#define SERIAL_DEBUG
//#define DEBUG

#define VMAX 10
#define OMEGA_MAX 5

// For WiFi access point
const char *ssid = "rover-esp";
const char *password = "123456789";

// Set the rosserial socket server IP address
IPAddress server(192,168,4,2);            // Laptop's IP address
const uint16_t serverPort = 11411;        // Set the rosserial socket server port

ros::NodeHandle nh;

// Make a chatter publisher
std_msgs::String str_msg;
ros::Publisher chatter("chatter", &str_msg);

// inputs from the joystick
float x_axis,y_axis;


int v, omega;
int vel_wheels[6], pwms[6] = {0, 0, 0, 0, 0, 0};
bool dirs[6];
int pwm_pins[6] = {15, 2, 4, 13, 12, 14};
int dir_pins[6] = {27, 26, 25, 33, 5, 18};
int yaw_off;


void KeyboardCb_x(const std_msgs::Float64 &msgdata){
  x_axis = msgdata.data;
  
  #ifdef SERIAL_DEBUG
//  Serial.println("in keyboard callback for x");
  Serial.print(x_axis); 
  Serial.print(',');
  #endif

  // Setting angular velocity
  if (x_axis <= 0.1 && x_axis >= -0.1) omega = 0;
  else omega = map(x_axis, -1.0, 1.0, -5, 5);

  #ifdef SERIAL_DEBUG
  Serial.print("omega in sub: ");
  Serial.println(omega);
  #endif
  
}

void KeyboardCb_y(const std_msgs::Float64 &msgdata){
  y_axis = msgdata.data;
  
  #ifdef SERIAL_DEBUG
//  Serial.println("in keyboard callback for y");
  Serial.println(y_axis); 
  #endif
}

// This should be done using a single subscriber
ros::Subscriber<std_msgs::Float64> key_sub_x("chal_jaa_x", &KeyboardCb_x);
ros::Subscriber<std_msgs::Float64> key_sub_y("chal_jaa_y", &KeyboardCb_y);


void setup()
{
  #ifdef DEBUG
  Serial.begin(115200);
  Serial.println();
  #endif
  
  WiFi.softAP(ssid,password);
  IPAddress myIP = WiFi.softAPIP();
  
  // Set the connection to rosserial socket server
  nh.getHardware()->setConnection(server, serverPort);
  nh.initNode();

  // Start to be polite
  nh.advertise(chatter);
  nh.subscribe(key_sub_x);
  nh.subscribe(key_sub_y);

  for (int i = 0; i < 6; i++)
  {
    pinMode(pwm_pins[i], OUTPUT);
    pinMode(dir_pins[i], OUTPUT);
  }
  
  delay(100);   //my_change
}

void loop()
{

  if (nh.connected()) {
    
    #ifdef SERIAL_DEBUG
//    Serial.println("Connected");
    str_msg.data = "Hello!";
    chatter.publish( &str_msg ); 
    #endif

    // Setting linear velocity
    // If omega == 0, then linear velocity will be more than that with omega != 0
    if (y_axis <= 0.2 && y_axis >= -0.2) v = 0;
    if (y_axis <= -0.8) v = -(14);
    else if (y_axis >= 0.8) v = (14);
    else
    {
      if (omega == 0) v = map(y_axis, -1.0, 1.0, -10, 10);
      else v = map(y_axis, -1.0, 1.0, -7, 7);
    }
  
//    Serial.print("x_axis: ");
//    Serial.println(x_axis);
//    Serial.print("y_axis: ");
//    Serial.println(y_axis);
    #ifdef SERIAL_DEBUG
    Serial.print("omega: ");
    Serial.println(omega);
    Serial.print("v is: ");
    Serial.println(v);
    #endif

    yaw_off = 0;
    // For right wheels
    vel_wheels[0] = v + (omega + yaw_off);
    vel_wheels[1] = v + (omega + yaw_off);
    vel_wheels[2] = v + (omega + yaw_off);
    // For left wheels
    vel_wheels[3] = v - (omega + yaw_off);
    vel_wheels[4] = v - (omega + yaw_off);
    vel_wheels[5] = v - (omega + yaw_off);
    
// 0
    if (vel_wheels[0] > 0)
    {
      dirs[0] = LOW;
//      pwms[0] = map(abs(vel_wheels[0]), 0, (VMAX + OMEGA_MAX), 0, 230);
      pwms[0] = map(abs(vel_wheels[0]), 0, (VMAX + OMEGA_MAX), 0, 100);
    }
    else
    {
      dirs[0] = HIGH;
//      pwms[0] = map(abs(vel_wheels[0]), 0, (VMAX + OMEGA_MAX), 0, 230);
      pwms[0] = map(abs(vel_wheels[0]), 0, (VMAX + OMEGA_MAX), 0, 100);
    }
    #ifdef SERIAL_DEBUG
    Serial.print("v0:");
    Serial.println(dirs[0]);
    #endif

// 1
    if (vel_wheels[1] > 0)
    {
      dirs[1] = HIGH;
//      pwms[1] = map(abs(vel_wheels[0]), 0, (VMAX + OMEGA_MAX), 0, 230);
      pwms[1] = map(abs(vel_wheels[1]), 0, (VMAX + OMEGA_MAX), 0, 100);
    }
    else
    {
      dirs[1] = LOW;
//      pwms[1] = map(abs(vel_wheels[0]), 0, (VMAX + OMEGA_MAX), 0, 230);
      pwms[1] = map(abs(vel_wheels[1]), 0, (VMAX + OMEGA_MAX), 0, 100);
    }
    #ifdef SERIAL_DEBUG
    Serial.print("v1:");
    Serial.println(dirs[1]);
    #endif

// 2
    if (vel_wheels[2] > 0)
    {
      dirs[2] = HIGH;
//      pwms[2] = map(abs(vel_wheels[0]), 0, (VMAX + OMEGA_MAX), 0, 230);
      pwms[2] = map(abs(vel_wheels[2]), 0, (VMAX + OMEGA_MAX), 0, 100);
    }
    else
    {
      dirs[2] = LOW;
//      pwms[2] = map(abs(vel_wheels[0]), 0, (VMAX + OMEGA_MAX), 0, 230);
      pwms[2] = map(abs(vel_wheels[2]), 0, (VMAX + OMEGA_MAX), 0, 100);
    }
    #ifdef SERIAL_DEBUG
    Serial.print("v2:");
    Serial.println(dirs[2]);    
    #endif

// 3
    if (vel_wheels[3] > 0)
    {
      dirs[3] = HIGH;
//      pwms[3] = map(abs(vel_wheels[0]), 0, (VMAX + OMEGA_MAX), 0, 230);
      pwms[3] = map(abs(vel_wheels[3]), 0, (VMAX + OMEGA_MAX), 0, 100);
    }
    else
    {
      dirs[3] = LOW;
//      pwms[3] = map(abs(vel_wheels[0]), 0, (VMAX + OMEGA_MAX), 0, 230);
      pwms[3] = map(abs(vel_wheels[3]), 0, (VMAX + OMEGA_MAX), 0, 100);
    }
    #ifdef SERIAL_DEBUG
    Serial.print("v3:");
    Serial.println(dirs[3]);
    #endif

// 4
    if (vel_wheels[4] > 0)
    {
      dirs[4] = HIGH;
//      pwms[4] = map(abs(vel_wheels[0]), 0, (VMAX + OMEGA_MAX), 0, 230);
      pwms[4] = map(abs(vel_wheels[4]), 0, (VMAX + OMEGA_MAX), 0, 100);
    }
    else
    {
      dirs[4] = LOW;
//      pwms[4] = map(abs(vel_wheels[0]), 0, (VMAX + OMEGA_MAX), 0, 230);
      pwms[4] = map(abs(vel_wheels[4]), 0, (VMAX + OMEGA_MAX), 0, 100);
    }
    #ifdef SERIAL_DEBUG
    Serial.print("v4:");
    Serial.println(dirs[4]);
    #endif

// 5    
    if (vel_wheels[5] > 0)
    {
      dirs[5] = LOW;
//      pwms[5] = map(abs(vel_wheels[0]), 0, (VMAX + OMEGA_MAX), 0, 230);
      pwms[5] = map(abs(vel_wheels[5]), 0, (VMAX + OMEGA_MAX), 0, 100);
    }
    else
    {
      dirs[5] = HIGH;
//      pwms[5] = map(abs(vel_wheels[0]), 0, (VMAX + OMEGA_MAX), 0, 230);
      pwms[5] = map(abs(vel_wheels[5]), 0, (VMAX + OMEGA_MAX), 0, 100);
    }
    #ifdef SERIAL_DEBUG
    Serial.print("v5:");
    Serial.println(dirs[5]);
    #endif

    // Sending commands to motor
    for (int i = 0; i < 6; i++)
    {
      analogWrite(pwm_pins[i], pwms[i]);
//      analogWrite(pwm_pins[i], 250);

      #ifdef SERIAL_DEBUG
      Serial.print("pwm0 is: ");
      Serial.println(pwms[0]);
      Serial.print("pwm1 is: ");
      Serial.println(pwms[1]);
      Serial.print("pwm2 is: ");
      Serial.println(pwms[2]);
      Serial.print("pwm3 is: ");
      Serial.println(pwms[3]);
      Serial.print("pwm4 is: ");
      Serial.println(pwms[4]);
      Serial.print("pwm5 is: ");
      Serial.println(pwms[5]);
      #endif
      
      if (dirs[i] == 0) digitalWrite(dir_pins[i], LOW);
      else digitalWrite(dir_pins[i], HIGH);
    }
    
    
  } else {
    
    #ifdef SERIAL_DEBUG
    Serial.println("Not Connected");
    #endif
  }
  nh.spinOnce();
  
  delay(30);
}

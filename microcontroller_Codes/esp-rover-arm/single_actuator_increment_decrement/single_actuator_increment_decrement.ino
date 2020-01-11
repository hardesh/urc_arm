//4inch extend on high
//6 inch extend on low

#define DIR 7
#define PWM 13

float pot,l;

float mymap(float a, float b, float c, float d, float e){
  return a/(c-b)*(e-d);
}

void setup(){
  pinMode(DIR,OUTPUT);  //digital output dir
  pinMode(PWM,OUTPUT); //PWM

  digitalWrite(DIR,HIGH);
  analogWrite(PWM,255);

Serial.begin(9600);
  
}

void loop(){
pot = analogRead(A3);
l = mymap(pot, 0,716,0,6.0);
Serial.println(pot);
 
  
}

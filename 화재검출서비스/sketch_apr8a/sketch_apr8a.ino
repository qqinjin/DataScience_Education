int ENA=6;
int in1=5;
int in2=4;
int Speed=255;

void setup() {
  pinMode(ENA,OUTPUT);
  pinMode(in1,OUTPUT);
  pinMode(in2,OUTPUT);
  Serial.begin(9600);
}

void loop() {
  digitalWrite(in1,LOW);
  digitalWrite(in2,HIGH);
  analogWrite(ENA,Speed);
  delay(1000);
  
}
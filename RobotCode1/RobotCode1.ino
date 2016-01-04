#define TRIG 4
#define ECHO 3
#define FORWARDRT 11
#define FORWARDLT 10
#define BACKWARDLT 9
#define BACKWARDRT 6

int dir = 0; 

unsigned long duration = 0;
int vel = 0;

void driveparse(int);
void leftforward();
void rightforward();
void rightbackward();
void leftbackward();
int allstop();

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);
  pinMode(FORWARDRT, OUTPUT);
  pinMode(FORWARDLT, OUTPUT);
  pinMode(BACKWARDRT, OUTPUT);
  pinMode(BACKWARDLT, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available()){
    int input = Serial.parseInt();
    driveparse(input);
    
    switch(dir){
      case 0:
        leftforward();
        rightforward();
        break;
      case 1:
        leftforward();
        rightbackward();
        break;
      case 2:
        leftbackward();
        rightforward();
        break;
      case 3:
        leftbackward();
        rightbackward();
        break;
      default:
        allstop();
    }
    for(int i = duration; i > 0; i--){
      delay(1000); 
    }
    int distance = allstop();
    Serial.println(distance);
  }
}
void driveparse(int input) {
  dir = input % 10;
  input = input / 10;
  vel = input % 10;
  duration = input / 10;
  duration = duration; 
}

void leftforward () {
  digitalWrite(FORWARDLT, vel * 28);
  digitalWrite(BACKWARDLT, LOW);
}

void rightforward () {
  digitalWrite(FORWARDRT, vel * 28);
  digitalWrite(BACKWARDRT, LOW);
}

void leftbackward () {
  digitalWrite(FORWARDLT, LOW);
  digitalWrite(BACKWARDLT, vel * 28);
}

void rightbackward () {
  digitalWrite(FORWARDRT, LOW);
  digitalWrite(BACKWARDRT, vel * 28);
}

int allstop() {
  digitalWrite(FORWARDRT, LOW);
  digitalWrite(FORWARDLT, LOW);
  digitalWrite(BACKWARDRT, LOW);
  digitalWrite(BACKWARDRT, LOW);
  int distance = echosense();
  return(distance);
}

int echosense(){
  digitalWrite(TRIG, HIGH);
  delay(10);
  digitalWrite(TRIG, LOW);
  duration = pulseIn(ECHO,HIGH);
  int distance= (duration/2)/29.1;
  return(distance);
}


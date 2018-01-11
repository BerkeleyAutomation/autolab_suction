#include <Servo.h>

String input;
Servo s;

void setup() {
  Serial.begin(57600);

  // Initialize at -90 degrees
  s.attach(6);
  s.writeMicroseconds(2250);
}

void loop() {
  while(Serial.available()) {
    if(Serial.available() > 0) {
      int deg = Serial.parseInt();
      int us = map(deg, -90, 90, 2250, 500); // map(value, fromLow, fromHigh, toLow, toHigh)
      s.writeMicroseconds(us);
    }
  }
}

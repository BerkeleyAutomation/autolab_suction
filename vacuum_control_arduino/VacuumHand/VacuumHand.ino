#include <Servo.h>

String input;
Servo s;

// Current values for 84, 0, and -90 deg.
// The microsecond limits for this servo are:
// Minimum: 550
// Maximum: 2350
// Angle calibration done by eye
int p84Deg = 550;
int zDeg = 1360;
int n90Deg = 2225;

void setup() {
  Serial.begin(57600);

  // Initialize at -90 degrees
  s.attach(6);
  s.writeMicroseconds(n90Deg);
}

void loop() {
  while(Serial.available()) {
    if(Serial.available() > 0) {
      int deg = Serial.parseInt();
      int us = map(deg, -90, 84, n90Deg, p84Deg);
      s.writeMicroseconds(us);
    }
  }
}

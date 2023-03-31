#include <Arduino.h>
#include <Wire.h>

const int upPin = 2;
const int downPin = 3;
const int leftPin = 4;
const int rightPin = 5;
const int speedPin = A0;

bool controls[5] = {0, 0, 0, 0, 0}; // 0th index for speed, 1-4 for directions

void setup() {
  pinMode(upPin, INPUT);
  pinMode(downPin, INPUT);
  pinMode(leftPin, INPUT);
  pinMode(rightPin, INPUT);
  pinMode(speedPin, INPUT);
}

void loop() {
  controls[1] = digitalRead(upPin);
  controls[2] = digitalRead(downPin);
  controls[3] = digitalRead(leftPin);
  controls[4] = digitalRead(rightPin);
  controls[0] = analogRead(speedPin);
  
  // use the controls array for motor controlling or other purposes
}

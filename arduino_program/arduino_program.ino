/*
 * This code is for arduino nano.
 * If you want to use this code on other
 * boards, please change the pin range
 * accordingly.
 */

const int DPIN_MIN = 2;
const int DPIN_MAX = 12;

const int APIN_MIN = 0;
const int APIN_MAX = 7;


void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  for (int i = DPIN_MIN; i <= DPIN_MAX; i++) {
    pinMode(i, INPUT_PULLUP);
  }
}

void loop() {
  for (int pin = APIN_MIN; pin <= APIN_MAX; pin++) {
    int value = analogRead(pin);
    int b0 = value / 256;
    int b1 = value % 256;
    //    value = map(0, 1023, 0, 127, value);
    Serial.print("AIN");
    Serial.write(pin);
    Serial.write(b0);
    Serial.write(b1);
    Serial.print("\n");
    delay(10);
  }

  for (int pin = DPIN_MIN; pin <= DPIN_MAX; pin++) {
    boolean value = digitalRead(pin);
    Serial.print("DIN");
    Serial.write(pin);
    Serial.write(value);
    Serial.print("\n");
    delay(10);
  }
}

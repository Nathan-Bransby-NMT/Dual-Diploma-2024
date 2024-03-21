# Chapter-2.1

<img src="https://raw.githubusercontent.com/Nathan-Bransby-NMT/Dual-Diploma-2024/main/Assets/diagram_esp32_ch2-1.png" alt="Exercise-2.1 Schematic Diagram"/>

```C
/********************************
* Filename: ex-2-1.c
********************************/

#define PIN_LED 2
#define PIN_BUTTON 13

void setup() {
  pinMode(PIN_LED, OUTPUT);
  pinMode(PIN_BUTTON, INPUT);
}

void loop() {
  if (digitalRead(PIN_BUTTON) == LOW) {
    digitalWrite(PIN_LED, HIGH);
  } else {
    digitalWrite(PIN_LED, LOW);
  }
}


```
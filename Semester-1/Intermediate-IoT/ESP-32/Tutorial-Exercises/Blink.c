/*******************************************************************************
* Filename          : Blink.c
* Description       : Make an LED blink.
* Author            : www.freenove.com
* Modification      : 2019-12-24
*******************************************************************************/

#define PIN_LED 2  // Define PIN_LED as the GPIO2 pin

// the setup function runs once when you press reset or power the board.
void setup() {
    // initialise digital pin LED_BUILTIN as an output.
    pinMode(PIN_LED, OUTPUT);
}

// the loop function runs over and over again forever.
void loop() {
    digitalWrite(PIN_LED, HIGH);  // turn the LED on by setting the voltage to high.
    delay(1000);                        // wait 1 second (1000ms).
    digitalWrite(PIN_LED, LOW);   // thurn the LED off by setting the voltage to low.
    delay(1000);                        // wait 1 second (1000ms).
}

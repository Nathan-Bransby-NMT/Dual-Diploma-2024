# Chapter 0 LED

## Project 0.1 Blink
A simple LED "blink" project.

### Overview
> Create a simple blinking LED circuit with the ESP32-WROVER from the GPIO2 pin. 

### Component List
> 1. ESP32-WROVER | X1
> 2. USB CABLE    | X1

### Setting Up
> 1. Open Arduino IDE
> 2. Create a new project.
> 3. Select the board:
>   -  `Tools` >> `Boards` >> `ESP32 Wrover Module`
> 4. Select the serial port:
>   - `Tools` >> `Port` >> `COM5`

### Program Code

```C
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

```

- Finally upload the code to the ESP32 by clicking `Upload`. 

# Chapter 1 LED

## Project 1.1 Blink
In this project we will use an ESP32 to control blinking a common LED.

### Component List
> 1. ESP-32 WROVER          | X1
> 2. GPIO Extension Board   | X1
> 3. Breadboard             | X1
> 4. LED (red)              | X1
> 5. Resistor ( 220Ω )      | X1
> 6. Jumper ( M/M )         | X2

#### LED
> An LED is a type of diode.
>  All diodes only work if current is flowing in the correct direction and have two poles. 
> A LED will only work (light up) if the longer pin (+) of LED is connected to the positive output from a power 
> source and the shorter pin is connected to the negative (-).

| LED   | Voltage  | Maximum Current | Recommended Current |
|-------|----------|-----------------|---------------------|
| Red   | 1.9-2.2V | 20mA            | 10mA                |
| Green | 2.9-3.4V | 10mA            | 5mA                 |
| Blue  | 2.9-3.4V | 10mA            | 5mA                 |

> **Volt ampere characteristics conform to diode**

#### Resistor
> Resistors use Ohms (**Ω**) as the unit measurement of their resistance (_R_).
> - 1MΩ = 1000kΩ
> - 1KΩ = 1000Ω
>
> Resistors are passive components that limit / regulate the flow of current in a circuit.
> The bands on resistors are a shorthand code used to identify the restance value.
>
>  ##### Ohms Law
> > The relationship between **Current, Voltage** and **Resistance** is expressed by the formula:
> > - `I=V/R`
> >   - Where `I = Current`, `V = Voltage` and `R = Resistance`
> > 
> > ```
> > Example:
> > 
> >   +₁<‒〰‒>₂-
> >   ⁵ⱽ  ᴿ¹₁₀ₖΩ
> > 
> >     R1 is I=U/R=5V/10KΩ=0.0005A=0.5mA
> > ``` 

### Schematics

<img src="https://raw.githubusercontent.com/Nathan-Bransby-NMT/Dual-Diploma-2024/main/Assets/diagram_esp32_ch1-1.png" alt="ch1.1 exercise"/>

### Set-Up
> 1. Open Arduino IDE.
> 2. Create new project.
> 3. Select the board:
>   - `Tools` >> `Board` >> `ESP32 Wrover Module`
> 4. Select the serial port:
>   - `Tools` >> `Port` >> `COM5`


### Programming Code

```C
/***************************************
* Filename:     Blink.c
* Author:       www.freenove.com
***************************************/

#define PIN_LED 2

void setup() {
    pinMode(PIN_LED, OUTPUT);
}

void loop() {
    digitalWrite(PIN_LED, HIGH);
    delay(1000);
    digitalWrite(PIN_LED, LOW);
    delay(1000);
}

```

> - Finally upload the code to the ESP by pressing `Upload`.

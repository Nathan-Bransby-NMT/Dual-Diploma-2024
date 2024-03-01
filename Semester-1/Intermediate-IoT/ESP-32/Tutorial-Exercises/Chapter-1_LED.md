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

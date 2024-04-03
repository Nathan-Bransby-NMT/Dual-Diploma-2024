# IoT Assessment Task 2 - Portfolio Part 3

Prepare for Work
Make sure you have followed the instructions on creating the answer document, as given in the General Instructions.

Familiarise yourself with the content and document your progress in this assessment.

Make sure that you complete the title page of the document.

At any stage during this assignment, you may consult the stakeholder(s) or their representative(s).

Please note that this assessment should be done on actual ESP32 hardware, which will be provided.

You can access the ESP32 API Reference here: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/gpio.html

This link specifically points to GPIO & RTC GPIO, but it will give you easy access to all the other areas of the API too.

## LEDs and Switches: start simple

For this task, you will be provided (in class) with a simple electronic circuit built around an ESP32 microcontroller.

The schematic for it looks like this (simplified):

<img src="https://github.com/Nathan-Bransby-NMT/Dual-Diploma-2024/blob/main/Assets/AT2_Portfolio3_Diagram.png?raw=true" alt="IoT Assessment Task 2 - Portfolio 3 Diagram" />

It contains the following elements:

- U1: ESP32 microcontroller
- R1, R2: resistors
- D1, D2: LEDs (one red – GPIO19, one green – GPIO18)
- SW1: switch (reed relay – GPIO15)
The microcontroller is powered with 3.3V, which may come from a battery or from a USB connection.

## 1

### _A01a_ **Q: What should be the value of R1 and R2 be?**
`todo**`
$$
R1=3.3V \times 0.02A = 0.66Ω
$$

$$
R2=\frac{3.3}{0.05}=66Ω
$$


| **Resister** | **LED** | **Resistance** |
|--------------|---------|----------------|
| R1           | Red     | 220Ω           |
| R2           | Green   | Ω              |

---

### _A01b_ **Q: How should each of the three GPIO pins be configured?**

---

### _A01c_ **Q: What additional requirements does GPIO15 have for it to work properly?**

---

## 2: Investigate the program

Download the provided software for this task from Blackboard.

Investigate the program to get an idea of its workings.

Answer the questions below.

### _A02a_ **Q: In your own words, describe what the program as a whole does.**

The code controls a series of LEDs that indicate whether a door is opened or closed based of the input from a door switch. If the door is opened the green LED will flash. If the door is closed the red LED will flash.

---

### _A02b_ **Q: What are the four main parts of the program?**

> __(Hint: look closely at the structure of the code.)__

The four parts are:
    1. Importing the required external modules for the script.
    2. Defining the pins being used on the device.
    3. Setting up the I/O State for the defined pins
    4. The main event loop function.

---

### _A02c_ Q: **What is the purpose of the function setup()?**

The purpose of the function `setup()` is to assign the read/write (Input/Output) states of the pins that are required.

---

### _A02d_ Q: **What is the purpose of the function loop()?**

The purpose of the function `loop()` is to define what actions will occur in each event cycle. Once the loop is called it will continue to loop until the device is interrupted.

## 3: Run the program

You will be provided with a way to program (or “flash”) the ESP32 in the circuit.

To run the program on the ESP32, it must first be transferred into its memory.

Use the Arduino IDE to program the ESP32.

You will use the code from Question 2.

After flashing the program, you can experiment with the circuit to see what it does.

Provide screenshots of the process of compiling and uploading the code.

Take a short video of the circuit in action (no more than 15 seconds).

Ensure you speak your name clearly when videoing the circuit.

Save this video as XXX-AT2-Pt3-03.mp4 (mp4, vog, avi or similar allowed). Replace XXX with your initials.

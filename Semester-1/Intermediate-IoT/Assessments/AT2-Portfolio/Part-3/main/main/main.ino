#include <driver/gpio.h>

#define GPIO_LED_GREEN  GPIO_NUM_18   /* Briefly flash if door is closed */
#define GPIO_LED_RED    GPIO_NUM_19   /* Briefly flash if door is open */

#define GPIO_SWITCH     GPIO_NUM_15   /* Door switch connected to this GPIO */

void setup() {
  Serial.begin(115200);

  /* LED outputs. */
  gpio_set_direction(GPIO_LED_GREEN, GPIO_MODE_OUTPUT);
  gpio_set_direction(GPIO_LED_RED, GPIO_MODE_OUTPUT);

  gpio_set_direction(GPIO_SWITCH, GPIO_MODE_INPUT);
  gpio_set_pull_mode(GPIO_SWITCH, GPIO_PULLUP_ONLY);
}

void loop() {
  const int pin_state = digitalRead(GPIO_SWITCH);
  
  gpio_set_level(pin_state ? GPIO_LED_RED : GPIO_LED_GREEN, 1);
  gpio_set_level(pin_state ? GPIO_LED_GREEN : GPIO_LED_RED, 0);

  delay(5000);
}

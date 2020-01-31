#ifndef __PROJ_CONST__
#define __PROJ_CONST__

/* **** PIN LAYOUTS **** */

/* Screen Defines */
#define SCL_PIN 5           // SCL Pin on ESP8266
#define SDA_PIN 4           // SDA Pin on ESP8266

/* DHT Defines */
#define DHT_PIN 14

/*PhotoResister Defines*/
#define PhotoResistor 0

/* WiFi Defines */

/* Other Defines */
#define EXTERNAL_RGB_RED    12
#define EXTERNAL_RGB_GREEN  13
#define EXTERNAL_RGB_BLUE   15

/* Include statements */
#include <Arduino.h>

void initialize_RGB_LED();

void set_RGB_LED(uint8_t r_val, uint8_t g_val, uint8_t b_val);

void blink_RGB_LED(unsigned long time, uint8_t r_val, uint8_t g_val, uint8_t b_val);

#endif

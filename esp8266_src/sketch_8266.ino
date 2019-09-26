/* ifndef to ignore IDE Complaints */
// #ifndef __IDE_COMPLAIN__
// #include "esp8266/variants/nodemcu/pins_arduino.h"
// #endif

/* Includes and libary supports */
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

extern "C"{
#include "debug.h"
#include "constants.h"
}
/* Initialization of global variables */
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);
Watchdog debug;

/* Initialization and setup of sensors and Wifi */
void setup() {
  // Initialize serial port
  Serial.begin(115200);

  // initialize digital OUT pins
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(EXTERNAL_LED_PIN, OUTPUT);

  /* Initialize display */
  if(!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)){
    debug.loop_blink_LED(EXTERNAL_LED_PIN, "Error initializing the screen");
  }
  display.display();
}

/* Main executable loop */
void loop() {

}

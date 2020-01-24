#ifndef __DISPLAY__
#define __DISPLAY__

#include <Arduino.h>
#include <Wire.h>
// #include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include <SoftwareSerial.h>

#include "constants.h"
#include "watchdog.h"

#define SCREEN_WIDTH 128    // OLED display width, in pixels
#define SCREEN_HEIGHT 64    // OLED display height, in pixels
#define OLED_RESET -1       // Reset pin, share with board
#define I2C_ADDRESS 0x3c

#define BATTERY_HIGH    3
#define BATTERY_MEDIUM  2
#define BATTERY_LOW     1
#define BATTERY_NONE    0

#define SIGNAL_HIGH     3
#define SIGNAL_MEDIUM   2
#define SIGNAL_LOW      1
#define SIGNAL_NONE     0

class Display_Module{
    /*
     *  Class to abstract display from Adafruit_SSD1306 Display.
     * 
     *  Provides more useful functions and direct calls, rather than trying to depend on 
     *      the default functions within Adafruit_SSD1306. The functions in this class are 
     *      intended to be used multiple times and make it easier to program the main .ino 
     *      file.
     */
    Adafruit_SSD1306 display = Adafruit_SSD1306(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);
    Watchdog watchdog = Watchdog();

    uint8_t battery_status;
    uint8_t wifi_status;

public:
    
    Display_Module();

    /*  Initialization function 
     *    - Prints to Serial that Display_Module module is initialized successfully.
     */
    void init(int voltage_setting, int i2c_address, uint8_t battery, uint8_t wifi);

    /*
     *
     */
    void initiate_status();

    /*
     *
     */
    void draw_battery_status(uint8_t status);

    /*
     *  Function to test display output
     */
    void testdrawlines();
};

#endif
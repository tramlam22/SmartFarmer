#include "display.h"

Display_Module::Display_Module(){

}

/*  Initialization function 
 *    - Prints to Serial that Display_Module module is initialized successfully.
 */
void Display_Module::init(int voltage_setting, int i2c_address, uint8_t battery, uint8_t wifi){
    Serial.println(F("[Display] Display is initializing..."));

    if(!display.begin(voltage_setting, i2c_address)){
        Serial.println(F("[Display] ERROR in initialization of display!!!"));
        watchdog.blocking_loop_blink_LED();
    }
    display.display();
    display.clearDisplay();
    delay(1000);

    battery_status = battery;
    wifi_status = wifi;
}

/*
 *
 */
void Display_Module::initiate_status(){
    
}

/*
 *
 */
void Display_Module::draw_battery_status(uint8_t status){
    display.clearDisplay();

    display.display();
    delay(1000);
}

/*
 * Function to test display output
 */
void Display_Module::testdrawlines(){
    int16_t i;

    display.clearDisplay(); // Clear display buffer

    for(i=0; i<display.width(); i+=4) {
        display.drawLine(0, 0, i, display.height()-1, WHITE);
        display.display(); // Update screen with each newly-drawn line
        delay(1);
    }
    for(i=0; i<display.height(); i+=4) {
        display.drawLine(0, 0, display.width()-1, i, WHITE);
        display.display();
        delay(1);
    }
    delay(250);

    display.clearDisplay();

    for(i=0; i<display.width(); i+=4) {
        display.drawLine(0, display.height()-1, i, 0, WHITE);
        display.display();
        delay(1);
    }
    for(i=display.height()-1; i>=0; i-=4) {
        display.drawLine(0, display.height()-1, display.width()-1, i, WHITE);
        display.display();
        delay(1);
    }
    delay(250);

    display.clearDisplay();

    for(i=display.width()-1; i>=0; i-=4) {
        display.drawLine(display.width()-1, display.height()-1, i, 0, WHITE);
        display.display();
        delay(1);
    }
    for(i=display.height()-1; i>=0; i-=4) {
        display.drawLine(display.width()-1, display.height()-1, 0, i, WHITE);
        display.display();
        delay(1);
    }
    delay(250);

    display.clearDisplay();

    for(i=0; i<display.height(); i+=4) {
        display.drawLine(display.width()-1, 0, 0, i, WHITE);
        display.display();
        delay(1);
    }
    for(i=0; i<display.width(); i+=4) {
        display.drawLine(display.width()-1, 0, i, display.height()-1, WHITE);
        display.display();
        delay(1);
    }

    delay(2000); // Pause for 2 seconds
}
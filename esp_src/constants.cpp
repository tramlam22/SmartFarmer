#include "constants.h"

void initialize_RGB_LED(){
    pinMode(EXTERNAL_RGB_RED, OUTPUT);
    pinMode(EXTERNAL_RGB_GREEN, OUTPUT);
    pinMode(EXTERNAL_RGB_BLUE, OUTPUT);
}

void set_RGB_LED(uint8_t r_val, uint8_t g_val, uint8_t b_val){
    digitalWrite(EXTERNAL_RGB_RED, r_val);
    digitalWrite(EXTERNAL_RGB_GREEN, g_val);
    digitalWrite(EXTERNAL_RGB_BLUE, b_val);
}

void blink_RGB_LED(unsigned long time, uint8_t r_val, uint8_t g_val, uint8_t b_val){
    delay(time);
    set_RGB_LED(r_val, g_val, b_val);
    delay(time);
    set_RGB_LED(0, 0, 0);
}
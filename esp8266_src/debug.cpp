#include <Arduino.h>

#include "debug.h"
#include "constants.h"

Watchdog::Watchdog(){
    
}

void Watchdog::loop_blink_LED(uint8_t pin){
    for(;;){
        digitalWrite(pin, HIGH);   // turn the LED on (HIGH is the voltage level)
        delay(1000);                       // wait for a second

        digitalWrite(pin, LOW);    // turn the LED off by making the voltage LOW
        delay(1000);  
    };
}

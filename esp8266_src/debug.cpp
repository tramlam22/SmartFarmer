#include <Arduino.h>

extern "C"{
#include "debug.h"
#include "constants.h"
}
Watchdog::Watchdog(){
    
}

void Watchdog::loop_blink_LED(uint8_t pin, const char* error_message){
    Serial.println(strcpy("[DEBUG] ", error_message));
    for(;;){
        digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
        delay(1000);                       // wait for a second

        digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
        delay(1000);  
    };
}

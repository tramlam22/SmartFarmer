#include "watchdog.h"

Watchdog::Watchdog(){
    
}

void Watchdog::init(){
    Serial.println(F("[WATCHDOG] Watchdog module is initialized!"));
}

void Watchdog::blocking_loop_blink_LED(){
    Serial.println(F("[WATCHDOG] Called from function: BLOCKING CODE PROGRESS\n"));
    for(;;){
        set_RGB_LED(HIGH, LOW, LOW);
        delay(1000);                      // wait for a second

        set_RGB_LED(LOW, LOW, LOW);    // turn the LED off by making the voltage LOW
        delay(1000);  
    };
}

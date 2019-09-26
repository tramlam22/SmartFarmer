#ifndef __INTERNAL_DEBUG__
#define __INTERNAL_DEBUG__

// #ifndef __IDE_COMPLAIN__
// #include "esp8266/variants/nodemcu/pins_arduino.h"
// #endif

#include <Arduino.h>

class Watchdog{
/*
    Debug class for indicating failures of the board. 
*/

public:
    /* Normal constructor */
    Watchdog();

    /* */
    void loop_blink_LED(uint8_t pin);

};

#endif


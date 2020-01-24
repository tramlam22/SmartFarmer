#ifndef __INTERNAL_DEBUG__
#define __INTERNAL_DEBUG__
#include <Arduino.h>
#include "constants.h"

class Watchdog{
    /*
     *  Debug class for indicating failures of the board. 
     */

public:
    /*  Normal constructor */
    Watchdog();

    /*  Initialization function 
     *      - Prints that Watchdog module is initialized successfully.
     */
    void init();

    /* */
    void blocking_loop_blink_LED();
};

#endif


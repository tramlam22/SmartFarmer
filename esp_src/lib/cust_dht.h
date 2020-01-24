#include <Arduino.h>
#include <SoftwareSerial.h>
#include "constants.h"
#define DHT_TYPE 11

#ifndef _USE_CUSTOM_DHT
#include <DHT.h>

class custom_DHT {

private:
    DHT dht = DHT(DHT_PIN, DHT_TYPE);

    float __humidity;
    float __temperature;
    float __heat_index;

protected:

    void read_sensor_values();

public:

    custom_DHT();

    char *get_string();

};

#else
#define custom_dht 0 // ignore for now

#endif
#include "cust_dht.h"

/* Constructor */
custom_DHT::custom_DHT(){
    Serial.println("[DHT] Initializing DHT Sensor");
    dht.begin();
}

/* Protected */
void custom_DHT::read_sensor_values(){
    Serial.println("[DHT] Reading Sensor Values.");
    __humidity = dht.readHumidity();
    __temperature = dht.readTemperature();
    __heat_index = dht.computeHeatIndex(__temperature, __humidity, true);
}

/* Public */
char *custom_DHT::get_string() {
    Serial.println("[DHT] Calling get_string()");
    read_sensor_values();
    
    char buffer[100];
    sprintf(buffer, "T:%f H:%f I:%f", __temperature, __humidity, __heat_index);
    Serial.print("[DHT] DHT String: ");
    Serial.print(buffer);
    Serial.print("\n");
    return buffer;
}
#include "DHT.h"
#include "Adafruit_seesaw.h"

Adafruit_seesaw ss;

//#define DHTPIN 14


DHT dht(14, DHT11);

void setup() {
  Serial.begin(9600);
  if (!ss.begin(0x36))
  {
    Serial.println("ERROR! soil sensor not found");
    while(1);
  }
  else
  {
    Serial.print("Soil Sensor: version ");
    Serial.print(ss.getVersion(), HEX);
  }
  dht.begin();
}

void loop() {
  // Wait a few seconds between measurements.
  delay(2000);

  // Reading temperature or humidity takes about 250 milliseconds!
  // Sensor readings may also be up to 2 seconds 'old' (its a very slow sensor)
  float h = dht.readHumidity();
  // Read temperature as Celsius
  float t = dht.readTemperature();
  // Read temperature as Fahrenheit
  float f = dht.readTemperature(true);

  Serial.print("humidity from dht: ");
  Serial.println (h);
  Serial.print("temperature C from dht: ");
  Serial.println (t);
  Serial.print("temperature F from dht: ");
  Serial.println (f);
  // float calc = dht.readTemperature(true) - 32 / (float)(9 / 5);

//  int sensorValue = analogRead(A0);
//  float voltage = sensorValue * (3.3/1023.0);


  // Check if any reads failed and exit early (to try again).

  if (isnan(h) || isnan(t) || isnan(f)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

  // Compute heat index
  // Must send in temp in Fahrenheit!
  float hic = dht.computeHeatIndex(t, h, false);
  float hif = dht.computeHeatIndex(f, h, true);
  // You can delete the following Serial.print's, it's just for debugging purposes
  Serial.print("HIC from dht: ");
  Serial.println (hic);
  Serial.print("HIF F from dht: ");
  Serial.println (hif);
  float tempC = ss.getTemp();
  uint16_t capread = ss.touchRead(0);

  Serial.print("temp from soil sensor: "); 
  Serial.println(tempC);
  Serial.print("Capactivie from soil sensor: ");
  Serial.println(capread);
  delay(100);

  float batteryLevel = map(analogRead(A0), 0.0f, 4095.0f, 0, 100);
  Serial.print("battery Level: ");
  Serial.println(batteryLevel);
}

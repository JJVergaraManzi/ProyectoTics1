#include <DHT11.h>
int Pin1 = A0;
int Pin2 = 7;
DHT11 dht11(Pin2);
int X;

void setup(){
  Serial.begin(9600);
}

void loop() {
  int err;
  float temp, humi;
  if((err=dht11.read(humi, temp))==0)
  {
    Serial.print("temperatura:");
    Serial.print(temp);
    Serial.print("°C");
    Serial.println("");
    Serial.print("Humedad relativa: ");
    Serial.print(humi);
    Serial.print("%");
    Serial.println("");
  }
  else
  {
    Serial.println();
    Serial.print("Error No :");
    Serial.print(err);
    Serial.println();    
  }
  int sensorValue = analogRead(Pin1);
  X = map(sensorValue, 0, 1023, 100, 0);
  Serial.print(X);
  Serial.print("% de humedad de suelo");
  Serial.println("");
  delay(3000);
}

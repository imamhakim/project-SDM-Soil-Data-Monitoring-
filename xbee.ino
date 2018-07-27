#include<dht.h>
#include<LiquidCrystal_I2C.h>
#include<Wire.h>
#define DHT11_PIN 9
dht DHT;

int kelembaban,t;int kel = A0;
LiquidCrystal_I2C lcd(0x3F,2,1,0,4,5,6,7,3,POSITIVE);
void setup(){
  Serial.begin(9600);
  lcd.begin(16,2);
  lcd.print("Welcome");delay(1500);lcd.clear();
  lcd.print("SDM (Soil Data");
  lcd.setCursor(0,1);lcd.print("Monitoring)");delay(3000);lcd.clear();
}

void loop() {
  DHT.read11(DHT11_PIN);
  t=analogRead(kel);
  kelembaban = 100-(t*0.0977517106549365);
  Serial.print(kelembaban);Serial.print(",");Serial.print(DHT.temperature);Serial.println(",");
  delay(100);lcd.print(kelembaban);lcd.setCursor(6,0);lcd.print(DHT.temperature);
  delay(1000);lcd.clear();
 
}

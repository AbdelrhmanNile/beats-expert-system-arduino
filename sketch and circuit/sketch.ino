#define USE_ARDUINO_INTERRUPTS true //--> Set-up low-level interrupts for most acurate BPM math.
#include <PulseSensorPlayground.h> //--> Includes the PulseSensorPlayground Library.   

//----------------------------------------Variable Declaration
const int PulseWire = 0; //--> PulseSensor PURPLE WIRE connected to ANALOG PIN 0
const int LED_3 = 3; //--> LED to detect when the heart is beating. The LED is connected to PIN 3 on the Arduino UNO.
int Threshold = 520; //--> Determine which Signal to "count as a beat" and which to ignore.
                     //--> Use the "Gettting Started Project" to fine-tune Threshold Value beyond default setting.
                     //--> Otherwise leave the default "520" value. 
//----------------------------------------
                               
PulseSensorPlayground pulseSensor; //--> Creates an instance of the PulseSensorPlayground object called "pulseSensor"

void setup() {   
  
  Serial.begin(9600);
  pulseSensor.analogInput(PulseWire);   
  pulseSensor.blinkOnPulse(LED_3); //--> blink LED with heartbeat.
  pulseSensor.setThreshold(Threshold);   
  pulseSensor.begin();
}

void loop() {
  int myBPM = pulseSensor.getBeatsPerMinute(); //--> Calls function on our pulseSensor object that returns BPM as an "int". "myBPM" hold this BPM value now.

  if (pulseSensor.sawStartOfBeat()) { // if a heatbeat happened 
  
    Serial.println(myBPM); //--> Print the value inside of myBPM
  }
  delay(20);
}

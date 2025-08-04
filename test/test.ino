// This code is designed for a NodeMCU (ESP8266) connected to a gas sensor (like MQ-2, MQ-135, etc.)
// It reads the analog value from the sensor, calculates a relative air quality percentage,
// and prints the value and a corresponding status to the Serial Monitor.

// No libraries are needed for this basic setup.

// The analog pin on the NodeMCU is A0.
const int gasSensorPin = A0;

// Variable to store the calculated air quality value.
double air_quality;

void setup() {
  // Initialize Serial communication at a baud rate of 115200.
  // Make sure your Serial Monitor is set to the same baud rate.
  Serial.begin(115200);
  delay(100); // Small delay to ensure serial is ready.
  Serial.println("Air Quality Monitoring System Initialized");
  Serial.println("----------------------------------------");
  Serial.println("Reading data from gas sensor...");
}

void loop() {
  // Read the raw analog value from the gas sensor connected to pin A0.
  // The NodeMCU's A0 pin has a 10-bit resolution (0-1023).
  int sensorValue = analogRead(gasSensorPin);

  // Convert the raw analog value (0-1023) to a percentage (0-100).
  // This is a simple mapping. For accurate PPM values, you would need to
  // consult the sensor's datasheet and perform a more complex calculation.
  air_quality = (sensorValue / 1023.0) * 100.0;

  // Print the calculated pollution percentage to the Serial Monitor.
  Serial.print("Pollution Level: ");
  Serial.print(air_quality);
  Serial.print("% - ");

  Serial.print("SensorValue");
  Serial.print(sensorValue);
  Serial.print("AirQualityValue");
  Serial.print(air_quality);
  // Determine and print the air quality status based on the percentage.
  // You can adjust these threshold values based on your sensor and environment.
  if (air_quality <= 20.0) {
    Serial.println("Status: Normal");
  } else if (air_quality > 20.0 && air_quality < 70.0) {
    Serial.println("Status: Medium");
  } else {
    Serial.println("Status: Danger!");
  }

  // Wait for 2 seconds before taking the next reading.
  delay(2000);
}

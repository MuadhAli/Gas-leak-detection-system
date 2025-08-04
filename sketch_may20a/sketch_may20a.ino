#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>
#include <DHT.h>

// WiFi credentials
const char* ssid = "Airtel_Zerotouch";
const char* password = "Airtel@123";

// Sensor pins
#define DHTPIN D5                // GPIO14
#define DHTTYPE DHT11
#define FLAME_SENSOR_PIN D2      // GPIO4
#define BUZZER_PIN D1            // GPIO5

DHT dht(DHTPIN, DHTTYPE);
ESP8266WebServer server(80);     // Web server on port 80

void setup() {
  Serial.begin(115200);

  // Setup pins
  pinMode(FLAME_SENSOR_PIN, INPUT);
  pinMode(BUZZER_PIN, OUTPUT);
  digitalWrite(BUZZER_PIN, LOW); // Buzzer OFF

  // Start DHT
  dht.begin();

  // Connect to WiFi
  Serial.println("Connecting to WiFi...");
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.print("✅ WiFi connected. IP Address: ");
  Serial.println(WiFi.localIP());

  // Set up HTTP endpoints
  server.on("/sensor", HTTP_GET, []() {
    float humidity = dht.readHumidity();
    float temperature = dht.readTemperature();
    int flameState = digitalRead(FLAME_SENSOR_PIN);
    String flameStatus = (flameState == LOW) ? "Flame Detected" : "No Flame";

    String json = "{";
    if (isnan(temperature) || isnan(humidity)) {
      json += "\"error\": \"Failed to read from DHT11\"";
    } else {
      json += "\"temperature\": " + String(temperature, 1);
      json += ", \"humidity\": " + String(humidity, 1);
    }
    json += ", \"flame\": \"" + flameStatus + "\"";
    json += "}";

    server.sendHeader("Access-Control-Allow-Origin", "*");  // CORS
    server.send(200, "application/json", json);
  });

  server.on("/buzzon", HTTP_GET, []() {
    digitalWrite(BUZZER_PIN, HIGH);
    server.sendHeader("Access-Control-Allow-Origin", "*");
    server.send(200, "text/plain", "🔔 Buzzer ON");
  });

  server.on("/buzzoff", HTTP_GET, []() {
    digitalWrite(BUZZER_PIN, LOW);
    server.sendHeader("Access-Control-Allow-Origin", "*");
    server.send(200, "text/plain", "🔕 Buzzer OFF");
  });

  server.begin();
  Serial.println("🌐 Web server started");
}

void loop() {
  server.handleClient();
}

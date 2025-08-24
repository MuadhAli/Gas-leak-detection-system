"""
Constants for Gas Leak Detection System.
This file contains all constants used throughout the application.
"""

# ==== Twilio Configuration ====
TWILIO_FROM_NUMBER = "+12766638646"
TO_NUMBER = "+919845119468"

# ==== ESP Sensor Endpoints ====
ESP_1_IP = "http://172.20.10.2"
ESP_2_IP = "http://172.20.10.3"

FIRE_AIR_URL = f"{ESP_1_IP}/sensor"  # ESP fire & air
GAS_URL = f"{ESP_2_IP}/sensor"       # ESP MQ-5 gas

# ==== Flask API Buzzer Endpoints ====
FLASK_IP = "http://127.0.0.1:5000"
BUZZER_SENSOR1_ON = f"{FLASK_IP}/api/sensor1/buzzon"
BUZZER_SENSOR1_OFF = f"{FLASK_IP}/api/sensor1/buzzoff"
BUZZER_SENSOR2_ON = f"{FLASK_IP}/api/sensor2/buzzon"
BUZZER_SENSOR2_OFF = f"{FLASK_IP}/api/sensor2/buzzoff"

# ==== ESP8266 Endpoints ====
ESP_SENSOR1_URL = f"{ESP_2_IP}/sensor"
ESP_SENSOR2_URL = f"{ESP_1_IP}/sensor"
ESP_BUZZER1_ON_URL = f"{ESP_2_IP}/buzzon"
ESP_BUZZER1_OFF_URL = f"{ESP_2_IP}/buzzoff"
ESP_BUZZER2_ON_URL = f"{ESP_1_IP}/buzzon"
ESP_BUZZER2_OFF_URL = f"{ESP_1_IP}/buzzoff"

# ==== Flask Server Configuration ====
FLASK_HOST = "0.0.0.0"
FLASK_PORT = 5000

# ==== Request Timeouts ====
SENSOR_REQUEST_TIMEOUT = 5  # seconds
BUZZER_REQUEST_TIMEOUT = 3  # seconds

# ==== Alert Configuration ====
ALERT_WAIT_TIME = 60  # seconds
MAIN_LOOP_DELAY = 1   # seconds

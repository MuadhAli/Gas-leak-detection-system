import requests
import time
from twilio.rest import Client
import os
from dotenv import load_dotenv

# ==== Load Env ====
load_dotenv()
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_FROM_NUMBER = "+12766638646"
TO_NUMBER = "+919845119468"

# ==== ESP Sensor Endpoints ====
FIRE_AIR_URL = "http://172.20.10.2/sensor"  # ESP fire & air
GAS_URL = "http://172.20.10.3/sensor"       # ESP MQ-5 gas

# ==== Flask API Buzzer Endpoints ====
BUZZER_SENSOR1_ON = "http://127.0.0.1:5000/api/sensor1/buzzon"
BUZZER_SENSOR1_OFF = "http://127.0.0.1:5000/api/sensor1/buzzoff"
BUZZER_SENSOR2_ON = "http://127.0.0.1:5000/api/sensor2/buzzon"
BUZZER_SENSOR2_OFF = "http://127.0.0.1:5000/api/sensor2/buzzoff"

# ==== Twilio Client ====
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def trigger_call(message):
    """Trigger a Twilio call with a spoken message."""
    call = client.calls.create(
        to=TO_NUMBER,
        from_=TWILIO_FROM_NUMBER,
        twiml=f'<Response><Say>{message}</Say></Response>'
    )
    print(f"📞 Call triggered. SID: {call.sid}")

def activate_buzzers():
    """Turn ON both ESP buzzers through Flask API."""
    try:
        requests.get(BUZZER_SENSOR1_ON, timeout=3)
        print("🔔 Sensor1 buzzer ON")
    except Exception as e:
        print(f"❌ Failed to activate Sensor1 buzzer: {e}")

    try:
        requests.get(BUZZER_SENSOR2_ON, timeout=3)
        print("🔔 Sensor2 buzzer ON")
    except Exception as e:
        print(f"❌ Failed to activate Sensor2 buzzer: {e}")

def deactivate_buzzers():
    """Turn OFF both ESP buzzers through Flask API."""
    try:
        requests.get(BUZZER_SENSOR1_OFF, timeout=3)
        print("🔕 Sensor1 buzzer OFF")
    except Exception as e:
        print(f"❌ Failed to deactivate Sensor1 buzzer: {e}")

    try:
        requests.get(BUZZER_SENSOR2_OFF, timeout=3)
        print("🔕 Sensor2 buzzer OFF")
    except Exception as e:
        print(f"❌ Failed to deactivate Sensor2 buzzer: {e}")


print("🚀 Monitoring fire, air quality, and petrol gas...")

while True:
    try:
        # === Fetch Fire & Air Quality Data ===
        response_fire = requests.get(FIRE_AIR_URL, timeout=5)
        response_fire.raise_for_status()
        data_fire = response_fire.json()

        flame_status = data_fire.get("flame", "")
        air_quality = data_fire.get("air_quality", "")

        print(f"🔥 Flame: {flame_status}, 🌫️ Air Quality: {air_quality}")

        if flame_status == "Fire Detected":
            print("🚨 Fire detected! Activating alarms & calling...")
            activate_buzzers()
            trigger_call("Warning! Fire detected at your premises.")
            print("⏳ Waiting 60 seconds...")
            time.sleep(60)
            deactivate_buzzers()

        elif "Poor" in air_quality:
            print("⚠️ Poor air quality detected! Activating alarms & calling...")
            activate_buzzers()
            trigger_call("Warning! Poor air quality detected. Please check immediately.")
            print("⏳ Waiting 60 seconds...")
            time.sleep(60)
            deactivate_buzzers()

        # === Fetch Petrol Gas Data ===
        response_gas = requests.get(GAS_URL, timeout=5)
        response_gas.raise_for_status()
        data_gas = response_gas.json()

        gas_detected = str(data_gas.get("gas_detected", "false")).lower() == "true"
        gas_value = data_gas.get("gas_value", 0)

        print(f"⛽ Petrol Gas Detected: {gas_detected}, Value: {gas_value}")

        if gas_detected:
            print("💥 Petrol gas detected! Activating alarms & calling...")
            activate_buzzers()
            trigger_call("Warning! Petrol gas detected. Please evacuate immediately.")
            print("⏳ Waiting 60 seconds...")
            time.sleep(60)
            deactivate_buzzers()

    except requests.RequestException as e:
        print(f"❌ Error fetching sensor data: {e}")

    time.sleep(1)  # main loop delay

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

# ==== Endpoints ====
FIRE_AIR_URL = "http://192.168.1.12/sensor"  # ESP fire & air
GAS_URL = "http://192.168.1.17/sensor"       # ESP MQ-5 gas

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
            print("🚨 Fire detected! Calling...")
            trigger_call("Warning! Fire detected at your premises.")
            print("waiting for 60 seconds before next check...")
            time.sleep(60)

        elif "Poor" in air_quality:
            print("⚠️ Poor air quality detected! Calling...")
            trigger_call("Warning! Poor air quality detected. Please check immediately.")
            print("waiting for 60 seconds before next check...")
            time.sleep(60)

        # === Fetch Petrol Gas Data ===
        response_gas = requests.get(GAS_URL, timeout=5)
        response_gas.raise_for_status()
        data_gas = response_gas.json()

        gas_detected = str(data_gas.get("gas_detected", "false")).lower() == "true"
        gas_value = data_gas.get("gas_value", 0)

        print(f"⛽ Petrol Gas Detected: {gas_detected}, Value: {gas_value}")

        if gas_detected:
            print("💥 Petrol gas detected! Calling...")
            trigger_call("Warning! Petrol gas detected. Please evacuate immediately.")
            print("waiting for 60 seconds before next check...")
            time.sleep(60)

    except requests.RequestException as e:
        print(f"❌ Error fetching sensor data: {e}")

    time.sleep(1)  # main loop delay

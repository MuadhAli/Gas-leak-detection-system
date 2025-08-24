from flask import Flask, jsonify
from flask_cors import CORS
import requests
from constants import (
    ESP_SENSOR1_URL, ESP_SENSOR2_URL,
    ESP_BUZZER1_ON_URL, ESP_BUZZER1_OFF_URL,
    ESP_BUZZER2_ON_URL, ESP_BUZZER2_OFF_URL,
    BUZZER_REQUEST_TIMEOUT, FLASK_HOST, FLASK_PORT
)

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# =============================
# SENSOR ENDPOINTS
# =============================
@app.route('/api/sensor1')
def sensor1():
    try:
        r = requests.get(ESP_SENSOR1_URL, timeout=BUZZER_REQUEST_TIMEOUT)
        return jsonify(r.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/sensor2')
def sensor2():
    try:
        r = requests.get(ESP_SENSOR2_URL, timeout=BUZZER_REQUEST_TIMEOUT)
        return jsonify(r.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# =============================
# BUZZER CONTROL ENDPOINTS
# =============================
@app.route('/api/sensor1/buzzon')
def sensor1_buzzon():
    try:
        r = requests.get(ESP_BUZZER1_ON_URL, timeout=BUZZER_REQUEST_TIMEOUT)
        return jsonify({"status": "Buzzer ON (sensor1)", "response": r.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/sensor1/buzzoff')
def sensor1_buzzoff():
    try:
        r = requests.get(ESP_BUZZER1_OFF_URL, timeout=BUZZER_REQUEST_TIMEOUT)
        return jsonify({"status": "Buzzer OFF (sensor1)", "response": r.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/sensor2/buzzon')
def sensor2_buzzon():
    try:
        r = requests.get(ESP_BUZZER2_ON_URL, timeout=BUZZER_REQUEST_TIMEOUT)
        return jsonify({"status": "Buzzer ON (sensor2)", "response": r.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/sensor2/buzzoff')
def sensor2_buzzoff():
    try:
        r = requests.get(ESP_BUZZER2_OFF_URL, timeout=BUZZER_REQUEST_TIMEOUT)
        return jsonify({"status": "Buzzer OFF (sensor2)", "response": r.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# =============================
# RUN SERVER
# =============================
if __name__ == '__main__':
    app.run(host=FLASK_HOST, port=FLASK_PORT)

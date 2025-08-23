from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# =============================
# SENSOR ENDPOINTS
# =============================
@app.route('/api/sensor1')
def sensor1():
    try:
        r = requests.get("http://192.168.1.17/sensor", timeout=3)
        return jsonify(r.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/sensor2')
def sensor2():
    try:
        r = requests.get("http://192.168.1.12/sensor", timeout=3)
        return jsonify(r.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# =============================
# BUZZER CONTROL ENDPOINTS
# =============================
@app.route('/api/sensor1/buzzon')
def sensor1_buzzon():
    try:
        r = requests.get("http://192.168.1.17/buzzon", timeout=3)
        return jsonify({"status": "Buzzer ON (sensor1)", "response": r.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/sensor1/buzzoff')
def sensor1_buzzoff():
    try:
        r = requests.get("http://192.168.1.17/buzzoff", timeout=3)
        return jsonify({"status": "Buzzer OFF (sensor1)", "response": r.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/sensor2/buzzon')
def sensor2_buzzon():
    try:
        r = requests.get("http://192.168.1.12/buzzon", timeout=3)
        return jsonify({"status": "Buzzer ON (sensor2)", "response": r.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/sensor2/buzzoff')
def sensor2_buzzoff():
    try:
        r = requests.get("http://192.168.1.12/buzzoff", timeout=3)
        return jsonify({"status": "Buzzer OFF (sensor2)", "response": r.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# =============================
# RUN SERVER
# =============================
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

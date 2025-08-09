from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

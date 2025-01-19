from flask import Flask, jsonify, request
from prometheus_client import Counter, generate_latest

import requests

app = Flask(__name__)

# Example metric
REQUEST_COUNT = Counter("app_requests_total", "Total number of requests")

@app.route("/metrics", methods=["GET"])
def metrics():
    return generate_latest(), 200, {"Content-Type": "text/plain; charset=utf-8"}

SERVICE_B_URL = "http://service-b/process"

@app.route("/test")
def test():
    REQUEST_COUNT.inc()
    return "Hello, world! from service-b prometheus"

@app.route('/test2', methods=['GET'])
def process():
    return "Hello world from service-a", 200

@app.route("/get-data", methods=["GET"])
def get_data():
    response = requests.get(SERVICE_B_URL)
    return jsonify({"message": "Data fetched from Service B", "data": response.json()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

SERVICE_B_URL = "http://service-b:5000/process"

@app.route("/get-data", methods=["GET"])
def get_data():
    response = requests.get(SERVICE_B_URL)
    return jsonify({"message": "Data fetched from Service B", "data": response.json()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

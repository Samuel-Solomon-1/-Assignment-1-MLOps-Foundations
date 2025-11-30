from flask import Flask, request, jsonify
import joblib
import numpy as np


app = Flask(__name__)
model = joblib.load("model.pkl")


@app.route("/")
def home():
    return "Flask ML App is running!"


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    features = np.array(data["inputs"]).reshape(1, -1)
    prediction = model.predict(features).tolist()
    return jsonify({"prediction": prediction})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)

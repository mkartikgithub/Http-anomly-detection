from flask import Flask, request, jsonify
from utils import preprocess_input, model

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    X_scaled = preprocess_input(data)
    pred = model.predict(X_scaled)[0]
    return jsonify({
        "result": "Anomaly" if pred == -1 else "Normal"
    })

if __name__ == "__main__":
    app.run(debug=True)

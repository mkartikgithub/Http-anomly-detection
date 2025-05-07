import os

# Define folder structure
folders = [
    "anomaly_detector",
    "anomaly_detector/model"
]

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# --------- app.py ---------
app_code = '''from flask import Flask, request, jsonify
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
'''

# --------- utils.py ---------
utils_code = '''import joblib
import numpy as np

# Load model and scaler
scaler = joblib.load("model/scaler.pkl")
model = joblib.load("model/isolation_model.pkl")

def preprocess_input(data_dict):
    features = [
        "url_length", "suspicious_keyword_count", "special_char_count",
        "method_GET", "method_POST", "method_PUT",
        "Method_code", "content_length"
    ]
    input_data = np.array([[data_dict.get(f, 0) for f in features]])
    input_scaled = scaler.transform(input_data)
    return input_scaled
'''

# --------- requirements.txt ---------
requirements = '''flask
scikit-learn
pandas
joblib
numpy
'''

# Write files
with open("anomaly_detector/app.py", "w") as f:
    f.write(app_code)

with open("anomaly_detector/utils.py", "w") as f:
    f.write(utils_code)

with open("anomaly_detector/requirements.txt", "w") as f:
    f.write(requirements)

print("✅ Project structure created in ./anomaly_detector")

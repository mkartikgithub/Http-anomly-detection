import joblib
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

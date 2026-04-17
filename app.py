from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load once
model = joblib.load(r"F:\ml\Big_Mart_Sale\models\lr.save")
scaler = joblib.load(r"F:\ml\Big_Mart_Sale\models\sc.save")

@app.route("/")
def home():
    return "API Running..."

@app.route('/predict', methods=['POST'])
def predict():

    data = request.json

    X = np.array([[
        data['item_weight'],
        data['item_fat_content'],
        data['item_visibility'],
        data['item_type'],
        data['item_mrp'],
        data['outlet_establishment_year'],
        data['outlet_size'],
        data['outlet_location_type'],
        data['outlet_type']
    ]])

    X_scaled = scaler.transform(X)
    prediction = model.predict(X_scaled)

    return jsonify({'prediction': float(prediction[0])})

if __name__ == "__main__":
    app.run(debug=True)
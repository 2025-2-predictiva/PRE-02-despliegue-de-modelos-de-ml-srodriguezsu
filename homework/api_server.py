from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Cargar el modelo entrenado
model = joblib.load('house_price_model.pkl')

# Definir las columnas esperadas
FEATURES = ["bedrooms", "bathrooms", "sqft_living", "sqft_lot", "floors", "waterfront", "condition"]

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    # Extraer los valores en el orden correcto
    try:
        values = [float(data[feature]) for feature in FEATURES]
    except Exception as e:
        return jsonify({'error': f'Error en los datos de entrada: {str(e)}'}), 400
    X = np.array(values).reshape(1, -1)
    pred = model.predict(X)[0]
    return jsonify({'predicted_price': pred})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
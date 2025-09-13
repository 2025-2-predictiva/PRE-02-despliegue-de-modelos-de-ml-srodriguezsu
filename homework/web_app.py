from flask import Flask, render_template_string, request
import requests

app = Flask(__name__)

HTML_FORM = '''
<!doctype html>
<title>House Price Predictor</title>
<h2>Ingrese las características de la casa</h2>
<form method=post>
  Dormitorios: <input type=number name=bedrooms required><br>
  Baños: <input type=number step=0.5 name=bathrooms required><br>
  Sqft Living: <input type=number name=sqft_living required><br>
  Sqft Lot: <input type=number name=sqft_lot required><br>
  Pisos: <input type=number step=0.5 name=floors required><br>
  Waterfront (0/1): <input type=number name=waterfront min=0 max=1 required><br>
  Condición (1-5): <input type=number name=condition min=1 max=5 required><br>
  <input type=submit value=Predecir>
</form>
{% if price is not none %}
  <h3>Precio predicho: {{ price }}</h3>
{% endif %}
'''

@app.route('/', methods=['GET', 'POST'])
def home():
    price = None
    if request.method == 'POST':
        data = {
            'bedrooms': request.form['bedrooms'],
            'bathrooms': request.form['bathrooms'],
            'sqft_living': request.form['sqft_living'],
            'sqft_lot': request.form['sqft_lot'],
            'floors': request.form['floors'],
            'waterfront': request.form['waterfront'],
            'condition': request.form['condition']
        }
        try:
            r = requests.post('http://127.0.0.1:5000/predict', json=data)
            if r.status_code == 200:
                price = r.json()['predicted_price']
            else:
                price = 'Error en la predicción'
        except Exception:
            price = 'No se pudo conectar al API'
    return render_template_string(HTML_FORM, price=price)

if __name__ == '__main__':
    app.run(port=8000, debug=True)
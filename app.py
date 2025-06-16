from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('xgboost_rain_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form
    features = np.array([[float(data['pressure']), float(data['maxtemp']), float(data['temparature']),
                          float(data['mintemp']), float(data['dewpoint']), float(data['humidity']),
                          float(data['cloud']), float(data['sunshine']), float(data['winddirection']),
                          float(data['windspeed'])]])
    
    prediction = model.predict(features)[0]
    result = "Yes" if prediction == 1 else "No"
    return render_template('index.html', prediction_text=f"Rainfall Prediction: {result}")

if __name__ == '__main__':
    app.run(debug=True)

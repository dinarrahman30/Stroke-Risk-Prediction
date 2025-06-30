import os
from flask import Flask, request, render_template
import joblib
import pandas as pd
import traceback

# Inisialisasi Flask
app = Flask(__name__)

# Muat model
try:
    model = joblib.load('artifacts/stroke_model.pkl')
    print("Model loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

# Halaman utama
@app.route('/')
def home():
    return render_template('index.html')

# Halaman prediksi
@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return render_template('index.html', prediction_text='Error: Model not loaded.')

    try:
        form = request.form

        # Mapping input kategorikal
        mappings = {
            'residence_type': {'urban': 1, 'rural': 0},
            'gender': {'female': 0, 'male': 1},
            'ever_married': {'yes': 1, 'no': 0},
            'work_type': {'private': 2, 'govt_job': 0, 'self-employed': 3, 'never_worked': 1},
            'smoking_status': {'unknown': 0, 'formerly smoked': 1, 'never smoked': 2, 'smokes': 3},
            'hypertension': {'yes': 1, 'no': 0},
            'heart_disease': {'yes': 1, 'no': 0}
        }

        # Proses input
        input_data = {
            'age': float(form['age']),
            'avg_glucose_level': float(form['avg_glucose_level']),
            'bmi': float(form['bmi']),
            'gender': mappings['gender'].get(form['gender'].lower(), 0),
            'ever_married': mappings['ever_married'].get(form['ever_married'].lower(), 0),
            'work_type': mappings['work_type'].get(form['work_type'].lower().replace('-', '_'), 0),
            'Residence_type': mappings['residence_type'].get(form['residence_type'].lower(), 0),
            'smoking_status': mappings['smoking_status'].get(form['smoking_status'].lower(), 0),
            'hypertension': mappings['hypertension'].get(form['hypertension'].lower(), 0),
            'heart_disease': mappings['heart_disease'].get(form['heart_disease'].lower(), 0)
        }


        # Buat DataFrame dari input
        df = pd.DataFrame([input_data])

        ordered_columns = [
            'gender', 'age', 'hypertension', 'heart_disease',
            'ever_married', 'work_type', 'Residence_type',
            'avg_glucose_level', 'bmi', 'smoking_status'
        ]
        df = df[ordered_columns]

        # Langsung prediksi (karena model sudah include preprocessing)
        pred = model.predict(df)
        prob = model.predict_proba(df)[0][1] * 100

        # Tampilkan hasil
        if pred[0] == 1:
            result = "High Risk Stroke"
        else:
            result = "Low Risk Stroke"

        return render_template(
            'index.html',
            prediction_text=result,
            probability_text=f"Probability: {prob:.2f}%"
        )

    except Exception as e:
        print(traceback.format_exc())
        return render_template('index.html', prediction_text=f"Error while prediction: {e}")

# Jalankan server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
# Gunakan ini untuk menjalankan aplikasi Flask
# app.run(debug=True) akan menjalankan aplikasi dalam mode debug, yang memberikan informasi lebih detail
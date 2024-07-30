from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load the model and preprocessing objects
model = joblib.load('model.pkl')
label_encoders = joblib.load('label_encoders.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = {
        'gender': request.form['gender'],
        'age': float(request.form['age']),
        'hypertension': int(request.form['hypertension']),
        'heart_disease': int(request.form['heart_disease']),
        'smoking_history': request.form['smoking_history'],
        'bmi': float(request.form['bmi']),
        'HbA1c_level': float(request.form['HbA1c_level']),
        'blood_glucose_level': float(request.form['blood_glucose_level'])
    }
    
    # Preprocessing
    for col in ['gender', 'smoking_history']:
        features[col] = label_encoders[col].transform([features[col]])[0]
    
    feature_df = pd.DataFrame([features])
    feature_scaled = scaler.transform(feature_df)
    
    # Prediction
    prediction = model.predict(feature_scaled)[0]
    
    result = 'Diabetes Detected' if prediction == 1 else 'No Diabetes'
    
    return render_template('result.html', result=result, features=features)

if __name__ == "__main__":
    app.run(debug=True)

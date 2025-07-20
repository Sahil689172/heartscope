from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask("heartscope")

# Load the trained model
model = joblib.load('heart_failure_model.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Extract features from form in the correct order
    features = [
        float(request.form['age']),
        float(request.form['anaemia']),
        float(request.form['creatinine_phosphokinase']),
        float(request.form['diabetes']),
        float(request.form['ejection_fraction']),
        float(request.form['high_blood_pressure']),
        float(request.form['platelets']),
        float(request.form['serum_creatinine']),
        float(request.form['serum_sodium']),
        float(request.form['sex']),
        float(request.form['smoking']),
        float(request.form['time'])
    ]
    # Preprocess if needed (e.g., scaling, encoding)
    # features = preprocess(features)
    features = np.array([features])
    prediction = model.predict(features)[0]
    result = "High Risk" if prediction == 1 else "Low Risk"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    print("Starting Heartscope Flask app...")
    app.run(debug=True) 
    
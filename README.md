Heartscope: Heart Failure Prediction Web App
Project Aim
This project aims to build a machine learning web app to predict heart failure based on clinical records. The workflow includes:

Loading and using a saved .pkl model (trained in Google Colab with tuned hyperparameters, selected features, and optimized threshold)
Taking user input through an HTML form
Preprocessing the input as needed
Predicting the risk of heart failure
Displaying the result on a new web page
This project is a Flask-based web application for predicting the risk of heart failure based on clinical records. It uses a pre-trained machine learning model saved as heart_failure_model.pkl.

Project Structure
heart_failure_app/
├── app.py
├── heart_failure_model.pkl
├── templates/
│   └── index.html
├── static/
│   └── style.css (optional)
Setup Instructions
Clone or Download the Repository

Place all files in the heart_failure_app directory as shown above.
Install Dependencies Open a terminal in the heart_failure_app directory and run:

pip install flask joblib numpy
Add Your Model

Ensure your trained model file is named heart_failure_model.pkl and is in the root of heart_failure_app.
Run the Application

python app.py
The app will start at http://127.0.0.1:5000
Usage

Open the app in your browser.
Fill in the clinical features in the form and submit.
The app will display the predicted risk of heart failure.
Notes
Edit app.py and templates/index.html to match your model's required input features.
Add any preprocessing steps in app.py if your model requires them.
Style the app using static/style.css (optional).
License
This project is for educational purposes.

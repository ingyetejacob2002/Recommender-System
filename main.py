from flask import Flask, render_template, request
import joblib
import numpy as np

model=joblib.load("model.joblib")
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        age = int(request.form['age'])
        gender = int(request.form['gender'])  # Assume gender is encoded as 0/1
        
        # Make prediction
        input_features = np.array([[age, gender]])
        prediction = model.predict(input_features)
        
        return render_template('index.html', prediction_text=f'Predicted Genre: {prediction[0]}')
    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}')

if __name__ == '__main__':
    app.run(debug=True)

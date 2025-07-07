from flask import Flask, request, render_template
import pandas as pd
import pickle

app = Flask(__name__)

# Load model and features
model = pickle.load(open('models/model.pkl', 'rb'))
model_features = model.feature_names_in_

# Age group mapping
def get_age_group(age):
    if 18 <= age <= 30: return '18-30'
    elif age <= 45: return '31-45'
    elif age <= 60: return '46-60'
    elif age <= 75: return '61-75'
    else: return '76-89'

@app.route('/')
def home():
    return render_template('index.html', result=None)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        age = int(request.form['age'])
        los = int(request.form['stay'])
        gender = int(request.form['gender'])
        med = int(request.form['med'])
        diag = request.form['diag_group']
        if diag == 'other':
            diag = request.form['diag_custom']

        age_group = get_age_group(age)

        # Build model input
        input_dict = {col: 0 for col in model_features}
        input_dict['Age'] = age
        input_dict['Length_of_Stay'] = los
        input_dict['Gender'] = gender
        input_dict['Number_of_Procedures'] = med

        # Set one-hot flags if they exist
        diag_key = f'Diagnosis_Group_{diag}'
        age_key = f'Age_Group_{age_group}'

        if diag_key in input_dict:
            input_dict[diag_key] = 1
        if age_key in input_dict:
            input_dict[age_key] = 1

        # Predict
        x_input = pd.DataFrame([input_dict], columns=model_features)
        pred = model.predict(x_input)[0]
        result = "Readmission Risk: High" if pred == 1 else "Readmission Risk: Low"

        return render_template('index.html', result=result)

    except Exception as e:
        return render_template('index.html', result=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request
import joblib

app = Flask(__name__)
model = joblib.load('model.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        features = [float(request.form.get(feat)) for feat in [
            'age','anaemia','creatinine_phosphokinase','diabetes','ejection_fraction',
            'high_blood_pressure','platelets','serum_creatinine','serum_sodium',
            'sex','smoking','time']]
        prediction = model.predict([features])[0]
        prediction = "High Risk of Heart Failure" if prediction == 1 else "Low Risk of Heart Failure"
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)

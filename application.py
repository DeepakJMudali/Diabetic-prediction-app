from flask import Flask, request, app,render_template
from flask import Response
import pickle
import numpy as np
import pandas as pd


application = Flask(__name__)
app=application

with open("./Model/StandardScaler.pkl","rb") as f: 
    scaler = pickle.load(f) 

with open("./Model/modelForPrediction.pkl","rb") as f: 
    clf = pickle.load(f)

## Route for homepage

@app.route('/')
def index():
    return render_template('index.html')

## Route for Single data point prediction
@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    result=""

    if request.method=='POST':

        Pregnancies=int(request.form.get("Pregnancies"))
        Glucose = float(request.form.get('Glucose'))
        BloodPressure = float(request.form.get('BloodPressure'))
        SkinThickness = float(request.form.get('SkinThickness'))
        Insulin = float(request.form.get('Insulin'))
        BMI = float(request.form.get('BMI'))
        DiabetesPedigreeFunction = float(request.form.get('DiabetesPedigreeFunction'))
        Age = float(request.form.get('Age'))

        Glucose = np.log1p(Glucose)
        BloodPressure = np.log1p(BloodPressure)
        SkinThickness = np.log1p(SkinThickness)
        Insulin = np.log1p(Insulin)
        BMI = np.log1p(BMI)
   
        new_data=scaler.transform([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        predict=clf.predict(new_data)
       
        if predict[0] ==1 :
            result = 'Diabetic'
        else:
            result ='Non-Diabetic'
            
        return render_template('single_prediction.html',result=result)

    else:
        return render_template('home.html')


if __name__=="__main__":
    app.run(host="0.0.0.0")
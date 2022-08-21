from flask import Flask,render_template,request,jsonify
import pickle
import numpy as np
import db

with open('model.pkl','rb') as f:

    model = pickle.load(f)


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('iris_data.html')



@app.route('/iris',methods=['POST'])
def predict():
    SepalLengthCm =float(request.form["SL"])
    SepalWidthCm =float(request.form['SW'])
    PetalLengthCm =float(request.form['PL'])
    PetalWidthCm =float(request.form['PW'])

    data=np.array([SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm],ndmin=2)

    result=model.predict(data)

   #print(result)

    if result[0]==0:
        pred='Iris-setosa'
        print('Iris-setosa')
    if result[0]==2:
        pred='Iris-virginica'
        print('Iris-virginica')
    if result[0]==1:
        pred='Iris-versicolour'
        print('Iris-versicolour')
    
    return jsonify(pred)










if __name__=="__main__":

    app.run(debug=True)
from flask import Flask, render_template, request
import joblib
model=joblib.load('hackjun')
stand=joblib.load('stand')

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    left_inputs = {"N": "", "P": "", "K": "", "pH": "", "EC": "", "OC": ""}
    right_inputs = {"S": "", "Zn": "", "Fe": "", "Cu": "", "Mn": "", "B": ""}
    prediction_result = ""
    if request.method == 'POST':
        left_inputs = {key: request.form.get(key) for key in left_inputs.keys()}
        right_inputs = {key: request.form.get(key) for key in right_inputs.keys()}
        prediction_result = predict(left_inputs, right_inputs)
    return render_template('index2.html', left_inputs=left_inputs, right_inputs=right_inputs, prediction_result=prediction_result)
@app.route('/predict')

def predict(left_inputs, right_inputs):
     
     left_inputs=list(left_inputs.values())
     y=list(right_inputs.values())
     left_inputs.extend(y)
     [float(x) for x in left_inputs]
     res=stand.transform([left_inputs])
     print(left_inputs)
     result=model.predict(res)
     if(result[0]==1):
        result='FERTILE'
     else:
        result='NON FERTILE'
     return result

   
if __name__ == '__main__':
    app.run(debug=True)

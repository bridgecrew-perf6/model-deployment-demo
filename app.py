
from crypt import methods
import numpy as np
from flask import Flask, render_template, request, jsonify
import pickle

app = Flask(__name__)
model = pickle.load(open("model.pkl", "rb"))


@app.route("/")
def home():
    return render_template("index.html")


'''
@app.route("/sub", methods = ['POST'])
def submit():
    # HTML to .py
    if request.method == "POST":
        name = request.form["username"]

    # .py to HTML
    return render_template("sub.html", n = name)
'''

@app.route("/predict",methods=["POST"])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    # output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Admission chance is {}'.format(prediction))

if __name__=="__name__":
    app.run(debug=True)
    
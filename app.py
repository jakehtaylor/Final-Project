from flask import Flask, redirect, render_template, request
import numpy as np

app = Flask(__name__)


 
import pickle
filename = "Test_Score_LR_v2.pkl"
model = pickle.load(open(filename, 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/Data')
def data():
    return render_template('Data.html')

@app.route('/Results')
def results():
    return render_template('Results.html')


@app.route('/Model')
def model():
    return render_template('Model.html')

@app.route('/Research')
def research():
    return render_template('Research.html')

@app.route('/Predict', methods=['GET', 'POST'])
def predict():

    if request.method == 'GET':
        return(render_template('Predict.html', pass_='none', fail_='none', inds=[0,0,1,0,0,0,0,0]))

    if request.method == 'POST':
        return (render_template('Predict.html', pass_='flex', fail_='none'))

if __name__ == '__main__':
    app.run()


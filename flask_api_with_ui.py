from copyreg import pickle
from statistics import variance
from flask import Flask, request
import pandas as pd
import numpy as np
import pickle 
import flasgger
from flasgger import Swagger

app=Flask(__name__)
Swagger(app)

pickle_in = open("classfiier.pickle","rb")
classifier = pickle.load(pickle_in)

@app.route('/')
def welcome():
    return "welcome all"

#?variance=2&skewness=3&curtosis=4&entropy=1
@app.route('/predict')
def predict_note_authentication():
    """
    Welcome to Wayne Fintech Solution
    I am Batman
    ---
    parameters:
        - name: variance
          in: query
          type: number
          required: True
        - name: skewness
          in: query
          type: number
          required: True
        - name: curtosis
          in: query
          type: number
          required: True
        - name: entropy
          in: query
          type: number
          required: True
    responses:
        200:
            description: The output values
    """

    variance=request.args.get("variance")
    skewness=request.args.get("skewness")
    curtosis=request.args.get("curtosis")
    entropy=request.args.get("entropy")
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    print(prediction)
    return "Hello The answer is"+str(prediction)

@app.route('/predict_file', methods=["POST"])
def predict_note_file():
    """Let's Authenticate the Bank Note
    This is using docstrings for specification.
    ---
    parameters:
     - name: file
       in: formData
       type: file
       required: true
    responses:
       200:
           descriprion: The output values
    """

    df_test = pd.read_csv(request.files.get("file"))
    prediction=classifier.predict(df_test)
    return "Hello The answer is"+str(list(prediction))



if __name__=='__main__':
    app.run()
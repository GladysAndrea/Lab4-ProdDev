from flask import Flask, json, jsonify, request
import pipeline_predict as pp
import json
import pandas as pd

app = Flask(__name__)

@app.route("/saludar")
def saludar():
    return jsonify({"username": "garg"})

#Ruta para predecir
@app.route("/predecir", methods= ['POST'])
def predict_from_pp():
    json_data = request.get_json()
    json_data = json.dumps(json_data)
    json_data = json.loads(json_data)

    dataFrame = pd.DataFrame.from_dict(json_data , orient="index")

    print(dataFrame)
    resultado = pp.predict(dataFrame)
    return jsonify({"Prediccion": resultado})
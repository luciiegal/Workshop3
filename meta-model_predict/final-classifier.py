from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

url1 = 'ngrok link /predict/'
url2 = 'ngrok link /predict/'
url3 = 'ngrok link /predict/'

@app.route('/predict', methods=['GET'])
def predict():
    L1 = float(request.args.get('L1'))
    W1 = float(request.args.get('W1'))
    L2 = float(request.args.get('L2'))
    W2 = float(request.args.get('W2'))

    params = {
        "L1": L1,
        "W1": W1,
        "L2": L2,
        "W2": W2
    }

    predict1 = requests.get(url1, params=params).json()
    predict2 = requests.get(url2, params=params).json()
    predict3 = requests.get(url3, params=params).json()

    if predict1.status_code != 200 or predict2.status_code != 200 or predict3.status_code != 200:
        return jsonify({"error": "Failed to get predictions from the models"})
    
    setosa = (predict1['setosa'] + predict2['setosa'] + predict3['setosa']) / 3
    versicolor = (predict1['versicolor'] + predict2['versicolor'] + predict3['versicolor']) / 3
    virginica = (predict1['virginica'] + predict2['virginica'] + predict3['virginica']) / 3

    final_prediction = {
        "setosa": setosa,
        "versicolor": versicolor,
        "virginica": virginica
    }

    return jsonify(final_prediction)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
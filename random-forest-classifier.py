# Import necessary libraries
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import numpy as np
from flask import Flask, render_template, request

# Load the iris dataset
iris = load_iris()
X = iris.data
y = iris.target
labelsname = list(iris.target_names)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.9, random_state=42)

# Create a random forest classifier
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the classifier
rf_classifier.fit(X_train, y_train)

# Make predictions on the test set
y_pred = rf_classifier.predict_proba(X_test)
print("Predictions:", y_pred)


app = Flask(__name__)

@app.route("/")
def read_root():
    return render_template("base.html")


@app.route("/predict/")
def make_prediction():
    """
    Makes a prediction based on the input parameters and returns the result.
    """
    try:
        L1 = float(request.args.get('L1'))
        W1 = float(request.args.get('W1'))
        L2 = float(request.args.get('L2'))
        W2 = float(request.args.get('W2'))
        
        testData = np.array([L1, W1, L2, W2]).reshape(-1, 4)
        probalities = rf_classifier.predict_proba(testData)[0]
        predicted = np.argmax(probalities)
        probability = probalities[predicted]
        predicted = labelsname[predicted]

        return render_template("prediction.html", probalities=probalities, predicted=predicted, probability=probability)
    
    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == '__main__':
    app.run(port=8000, host="127.0.0.1")

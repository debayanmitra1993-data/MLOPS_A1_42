from flask import Flask, request, jsonify
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score
import numpy as np

app = Flask(__name__)

# Global variable to store the trained model
model = None


def train_model():
    """Train a DecisionTreeClassifier on the Iris dataset."""
    global model
    data = load_iris()
    X, y = data.data, data.target
    model = DecisionTreeClassifier()
    model.fit(X, y)
    return model


def evaluate_model(model):
    """Evaluate the model using cross-validation and return the scores."""
    data = load_iris()
    X, y = data.data, data.target
    scores = cross_val_score(model, X, y, cv=5)
    return {
        "scores": scores.tolist(),
        "mean_accuracy": scores.mean()
    }


@app.route('/')
def home():
    return "Welcome to the ML Model API!"


@app.route('/train', methods=['GET'])
def train():
    train_model()
    return "Model trained successfully!"


@app.route('/evaluate', methods=['GET'])
def evaluate():
    evaluation = evaluate_model(model)
    return jsonify(evaluation)


@app.route('/predict', methods=['POST'])
def predict():
    if not model:
        return "Model not trained yet!", 400
    data = request.json
    if not data or 'input' not in data:
        return "Invalid input!", 400
    input_data = np.array(data['input']).reshape(1, -1)
    prediction = model.predict(input_data)
    return jsonify({"prediction": prediction.tolist()})


if __name__ == "__main__":
    train_model()
    app.run(host='0.0.0.0', port=5000)

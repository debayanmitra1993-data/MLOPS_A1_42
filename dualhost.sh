#!/bin/bash
# Start the Flask application
python app.py &
# Start the MLflow UI
mlflow ui --host 0.0.0.0 --port 5000
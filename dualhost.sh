#!/bin/bash
# Start the Flask application
python app.py &
# Start the MLflow UI
mlflow ui --host 127.0.0.1 --port 5000
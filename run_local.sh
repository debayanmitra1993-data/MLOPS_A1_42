# /Users/debayanmitra/miniconda3/envs/mlopsenv/bin/pip -> use this pip for conda env installer

IMAGE_NAME="mlops-42-flask-app"

echo "Building Docker image..."
docker build -t $IMAGE_NAME .

echo "Running Docker container..."
docker run -d -p 5000:5000 -p 8000:8000 $IMAGE_NAME
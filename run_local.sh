# /Users/debayanmitra/miniconda3/envs/mlopsenv/bin/pip

IMAGE_NAME="debayan-mlops-flask-app"

echo "Building Docker image..."
docker build -t $IMAGE_NAME .

echo "Running Docker container..."
docker run -d -p 5000:5000 $IMAGE_NAME
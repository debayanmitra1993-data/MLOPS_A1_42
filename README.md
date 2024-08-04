Welcome to our MLOPS project (Group 42)

To run on your local machine -> execute the ./run_local.sh
(ensure you set chmod +x ./run_local.sh)
This hosts flask IRIS predict end point on 8000 port and mlflow UI on 5000 port and contanerizes the Docker image build

CODEBASE - 
DVC -> .dvc/cache contains all the different versions of data version for X_train and y_train using train test split randomization
MLFLOW -> mlruns folder contains all the runs of SVM and Decision Tree experiments
TESTS -> contains unit tests as part of Test along with Lint & Deploy in Github actions in .github/workflows
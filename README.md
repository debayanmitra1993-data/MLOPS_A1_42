Welcome to our MLOPS project (Group 42)

To run on your local machine -> execute the **./run_local.sh** (ensure you set **chmod +x ./run_local.sh**). This hosts flask IRIS predict end point on 8000 port and mlflow UI on 5000 port and contanerizes the Docker image build

**CODEBASE**

**DVC** -> .dvc/cache contains all the different versions of data version for X_train and y_train using train test split randomization. data_dvc/* contains the .dvc files for X_train & y_train respectively. 

**MLFLOW** -> mlruns folder contains all the runs of SVM and Decision Tree experiments with Gridsearch Crossvalidation experiments

**TESTS** -> contains unit tests as part of Test along with Lint & Deploy in Github actions in .github/workflows

**./github/workflows/cicd.yml** -> contains the config file for CI/CD for all 3 parts - lint, test and deploy. Used Github actions to perform the same

**Dockerfile** -> Trains the Model , Exposes 5000 and 8000 ports to host MLFLOW UI and FLASK application respectively

**model_v2.py** -> Performs Hyperparameter search, saves best Model and logs the MLFLOW run - metrics, parameters and artifacts. 
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
import joblib
import mlflow
import mlflow.sklearn
from sklearn.datasets import load_iris

iris = load_iris()
X, y = iris.data, iris.target


# Function to train a DecisionTreeClassifier
def train_decision_tree():
    """Train a DecisionTreeClassifier on the dataset."""
    model = DecisionTreeClassifier()
    model.fit(X, y)
    joblib.dump(model, './models/decision_tree_model.pkl')
    return model


# Function to evaluate a model using cross-validation
def evaluate_model(model):
    """Evaluate the model using cross-validation and return the scores."""
    scores = cross_val_score(model, X, y, cv=5)
    return {
        "scores": scores.tolist(),
        "mean_accuracy": scores.mean()
    }


# Function to train an SVM using GridSearchCV
def train_svm():
    """Train an SVM using GridSearchCV on the dataset."""
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, )
    np.savetxt('./data_dvc/X_train.csv', X_train, delimiter=',', fmt='%d')
    np.savetxt('./data_dvc/y_train.csv', y_train, delimiter=',', fmt='%d')
    param_grid = {
        'C': [0.1, 1, 10, 100],
        'gamma': [1, 0.1, 0.01, 0.001],
        'kernel': ['rbf', 'linear']
    }
    svm = SVC()
    grid_search = GridSearchCV(
        estimator=svm, param_grid=param_grid,
        cv=5, verbose=2, n_jobs=-1
        )
    grid_search.fit(X_train, y_train)
    best_model = grid_search.best_estimator_
    joblib.dump(best_model, './models/best_svm_model.pkl')
    return best_model


# Function to run Decision Tree experiment
def run_decision_tree_experiment():
    experiment_name = "MLflow DVC Integration Experiment"
    mlflow.set_experiment(experiment_name)

    with mlflow.start_run(run_name="Decision Tree Experiment"):
        # Train and evaluate the DecisionTreeClassifier
        decision_tree_model = train_decision_tree()
        decision_tree_evaluation = evaluate_model(decision_tree_model)
        print("Decision Tree Evaluation:", decision_tree_evaluation)

        # Log parameters and metrics
        mlflow.log_param("model_type", "DecisionTreeClassifier")
        mlflow.log_metric(
            "mean_accuracy", 
            decision_tree_evaluation["mean_accuracy"]
            )
        mlflow.sklearn.log_model(decision_tree_model, "model")

    return decision_tree_evaluation


# Function to run SVM experiment
def run_svm_experiment():
    experiment_name = "MLflow DVC Integration Experiment"
    mlflow.set_experiment(experiment_name)

    with mlflow.start_run(run_name="SVM Experiment"):
        # Train and evaluate the SVM
        svm_model = train_svm()
        svm_evaluation = evaluate_model(svm_model)
        print("SVM Evaluation:", svm_evaluation)

        # Log parameters and metrics
        mlflow.log_param("model_type", "SVM")
        mlflow.log_metric("mean_accuracy", svm_evaluation["mean_accuracy"])
        mlflow.sklearn.log_model(svm_model, "model")

    return svm_evaluation


# Function to evaluate a saved DecisionTreeClassifier
def evaluate_saved_decision_tree():
    model = joblib.load('./models/decision_tree_model.pkl')
    return evaluate_model(model)


# Function to evaluate a saved SVM model
def evaluate_saved_svm():
    model = joblib.load('./models/best_svm_model.pkl')
    return evaluate_model(model)


if __name__ == '__main__':
    best_mdl_results = run_svm_experiment()
    print("Best SVM Model results = ", best_mdl_results)

"""This is the training pipeline for the model.
It handles the training process, including loading data, training the model, and saving the model.
"""
# Feel free to import any libraries you need

import mlflow
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier

from src.common import load_data, preprocess_data
from src.tracking_server import configure_server


def _train():

    configure_server()
    mlflow.set_experiment("My experiment")
    model_name = "test_model"

    # 1. Load data
    df = load_data("src/data/train.csv")

    # My target label is "Species"
    # My features are all other columns

    # 2. Preprocess data
    df = preprocess_data(df)

    # TODO: Now I want to split my data 50/50 into a train and evaluation set.
    # TODO: I would like to use the standard scaler to scale the features.
    # TODO: I would like to try the decision tree model with a max depth of 3 and min sample split of 2.
    # TODO: I would like to fit my model and scaler using the test data and evaluate accuracy using the evaluation data.

    # Remember the same process needs to be done in the inference pipeline too
    # Feel free to not only add but also edit the code if you need to

    # 3. Create scaler and model
    scaler = StandardScaler()

    params = {
        "max_depth": 3,
        "min_samples_split": 2,
    }

    model = DecisionTreeClassifier()

    # 4. Train test split
    # Pleae fill in the code to split the data into train and evaluation sets

    # 5. Train
    # Please fill in the code to scale data and train the model

    # 5. Evaluate model
    predictions = model.predict()
    accuracy = accuracy_score()

    # 6. Save model, metrics and parameters
    # Start an MLflow run
    with mlflow.start_run():
        # save model
        # anything else?
        # May be this is useful: https://mlflow.org/docs/latest/getting-started/intro-quickstart/index.html#step-4---log-the-model-and-its-metadata-to-mlflow
        pass
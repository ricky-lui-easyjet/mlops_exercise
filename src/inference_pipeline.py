"""This is the inference pipeline for the model.
It handles the inference process, including loading data, preprocessing data, loading the model and making predictions.
"""

import mlflow
import pandas as pd

from src.common import load_data, preprocess_data
from src.tracking_server import configure_server

def _infer():

    configure_server()

    # 1. Load data
    df = load_data("src/data/inference.csv")

    # 2. Preprocess data
    df = preprocess_data(df)
    df.drop(columns=["Species"], inplace=True)

    # I want to always use the latest version of the model but MLFlow does not support finding the latest version of a model
    # 3. Load model
    model_name = "test_model"
    client = mlflow.MlflowClient()
    # how to get the latest version of the model?
    # Looks like this is useful: https://mlflow.org/docs/latest/model-registry/#listing-and-searching-mlflow-models


    # 4. Make predictions
    predictions = model.predict(df)

    print(predictions)
    # We can worry about saving the predictions later

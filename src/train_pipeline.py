"""This is the training pipeline for the model.
It handles the training process, including loading data, training the model, and saving the model.
"""
import mlflow
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier

from src.common import load_data, preprocess_data
from src.tracking_server import configure_server


def _train():

    configure_server()
    mlflow.set_experiment("My experiment")

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

    # 3. Create pipeline to store scaler with model
    params = {
        "max_depth": 3,
        "min_samples_split": 2,
    }
    pipeline = Pipeline([
        # 3. Scale features
        ("scaler", StandardScaler()),
        # 4. Add model
        ("model", DecisionTreeClassifier(**params)),
    ])

    # 4. Train test split
    X_train, X_test, y_train, y_test = train_test_split(
        df.drop("Species", axis=1), df["Species"], test_size=0.5, random_state=42
    )

    # 5. Train pipeline
    pipeline.fit(X_train, y_train)

    # 5. Evaluate model
    predictions = pipeline.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    # 6. Save model, metrics and parameters
    # Start an MLflow run
    with mlflow.start_run():
        # Log the hyperparameters
        mlflow.log_params(params)

        # Log the loss metric
        mlflow.log_metric("accuracy", accuracy)

        # Log the model
        mlflow.sklearn.log_model(
            sk_model=pipeline,
            artifact_path="test_model",
            input_example=X_train,
            registered_model_name="test_model",
        )

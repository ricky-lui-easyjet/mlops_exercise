# mlops_exercise
This repository contains the exercise to be done by the candidate during the technical interview

## Scenario
The previous engineer in the company has left and he has left this repository unfinished. Your job is to solve the problems that he has left behind.

## Project set up
In order to develop the project it would be beneficial for you to
1. set up and activate a virtual environment
2. install the dependencies from `requirements.txt`

## Using the project
After the dependencies are installed, we can use the following commands to work with the project.

### Start MLFLow server
Use the following command to start a local MLFlow tracking server in the background.
```
python main.py start-server
```

### Run training pipeline
```
python main.py train
```

### Run inference pipeline
```
python main.py infer
```
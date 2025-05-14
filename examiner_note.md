# Examiner Note

## How to use this exercise
This exercise is designed to be worked on in the candidate'scomputer  with their screen shared to the examiner. The candidate would start off with wrong and missing code/config in the beginning. The aim of the exercise is to work with the candidate to walk through the development process. The examiner should encourage candidates to share their thoughts process and proivde guidance and hint if the candidate is stuck.

## Evaluation
This technical exercise test the following abilities of the candidate:

### Git operations
This exercise ensures that the candidate can do the following git operations:
- fork
- clone
- add
- commit
- push
- create pull requests
- review GitHub Actions
- merge pull requests

### Basic ML Pipeline architecture
This exercise ensures that the candidate is aware of the various steps of ML pipelines. The candidate should demonstrate that they can understand and use the following common tools.
- data preprocessing (sklearn StandardScaler)
- basic modelling (sklearn DecisionTree)
- basic model selection technique (sklearn train/test split)
- model, parameters and metrics logging (mlflow)

Apart from the above, the candidate should be able to identify the need of preseving the scaler as well as the model. Ideally he/she should be able to make use of appropriate tools (e.g. sklearn Pipeline) to achieve the purpose.

### Basic CICD Pipeline
The candidate will have to identify and create a step in the GitHub Actions CI pipeline. This checks the candidate's understanding of CI pipelines as well as the ability of implementation when an example is given. We should look for
- candidate can spot the missing of a test step
- candidate can set up dependencies to run tests before deployment

### General trouble shooting
The repository also contains various suboptimal or insecure implementations. The candidate should spot (and fix) the following:
- exposed secrets in CICD deployment step. GitHub repo secret should be used instead.
- MLFlow server start up process contains a bug. Candidate should be able to read the log and identify the problem, then proceed to fix.
- Candidate should be able to read documentation (e.g. in MLFlow) and implement the logic required to get the latest model version.
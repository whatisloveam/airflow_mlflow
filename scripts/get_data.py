import pandas as pd
import mlflow
import os
import wget

os.environ["MLFLOW_REGISTRY_URI"] = "/home/vlad/MLOps3/mlflow/"
mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment("get_data")

with mlflow.start_run():
    if os.path.exists("train.csv"):
        os.remove("train.csv")
    filename = wget.download("https://docs.google.com/uc?export=download&id=1T14YFNbLPIOAEzQPyl-hFJW0JtrpexJT")
    df_full = pd.read_csv(filename, delimiter=',')
    mlflow.log_artifact(local_path="/home/vlad/MLOps3/scripts/get_data.py",
                        artifact_path="get_data code")
    mlflow.end_run()

df_full.to_csv('/home/vlad/MLOps3/datasets/data.csv', index='Row_id')

import mlflow

def configure_mlflow(experiment_name="house_price_prediction"):
    mlflow.set_tracking_uri("file:///./mlruns")  # Change this to your desired location
    if not mlflow.get_experiment_by_name(experiment_name):
        mlflow.create_experiment(experiment_name)
    mlflow.set_experiment(experiment_name)

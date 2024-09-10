from pipelines.house_price_pipeline import HousePricePipeline
from mlflow_config.mlflow_config import configure_mlflow
import pandas as pd
# Configure MLflow
configure_mlflow()

# Define the path to the data
data_path = r'data/house_prices.csv'
df = pd.read_csv(data_path)

# Create pipeline instance
pipeline_instance = HousePricePipeline()

# Run the pipeline
rmse = pipeline_instance.run(data_path=df)
print(f"RMSE: {rmse}")

# pipelines/house_price_pipeline.py

from zenml.steps import BaseStep
from typing import Tuple
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

class IngestDataStep(BaseStep):
    def __call__(self, path: str) -> pd.DataFrame:
        """Load data from a CSV file."""
        return pd.read_csv(path)

class PreprocessDataStep(BaseStep):
    def __call__(self, data: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
        """Preprocess the data."""
        X = data.drop('median_house_value', axis=1)
        y = data['median_house_value']
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        scaler = StandardScaler()
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)
        
        return X_train, X_test, y_train, y_test

class TrainModelStep(BaseStep):
    def __call__(self, X_train: pd.DataFrame, y_train: pd.Series) -> RandomForestRegressor:
        """Train the model."""
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        return model

class EvaluateModelStep(BaseStep):
    def __call__(self, model: RandomForestRegressor, X_test: pd.DataFrame, y_test: pd.Series) -> float:
        """Evaluate the model."""
        predictions = model.predict(X_test)
        rmse = mean_squared_error(y_test, predictions, squared=False)
        return rmse

from zenml.pipelines import BasePipeline

class HousePricePipeline(BasePipeline):
    def __init__(self):
        self.ingest_data_step = IngestDataStep()
        self.preprocess_data_step = PreprocessDataStep()
        self.train_model_step = TrainModelStep()
        self.evaluate_model_step = EvaluateModelStep()
        
    def run(self, data_path: str) -> float:
        data = self.ingest_data_step(path=data_path)
        X_train, X_test, y_train, y_test = self.preprocess_data_step(data)
        model = self.train_model_step(X_train, y_train)
        rmse = self.evaluate_model_step(model, X_test, y_test)
        return rmse

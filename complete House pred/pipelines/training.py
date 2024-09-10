# pipelines/training.py
from zenml.pipelines import pipeline
from zenml.steps import step
from sklearn.ensemble import RandomForestRegressor

@step
def training_step(df):
    # Example ML model training
    X = df.drop('median_house_value', axis=1)
    y = df['median_house_value']
    model = RandomForestRegressor()
    model.fit(X, y)
    return model

@pipeline
def training_pipeline(preprocess_step, training_step):
    processed_df = preprocess_step()
    model = training_step(processed_df)
    return model

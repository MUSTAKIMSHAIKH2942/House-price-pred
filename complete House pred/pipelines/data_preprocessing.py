# from zenml.pipelines import pipeline
# from zenml.steps import step
# import pandas as pd
# from sklearn.preprocessing import StandardScaler, OneHotEncoder
# from sklearn.impute import SimpleImputer
# from sklearn.model_selection import train_test_split

# # Step to preprocess the data
# @step
# def preprocessing_step(df: pd.DataFrame) -> pd.DataFrame:
#     # Handle missing values
#     imputer = SimpleImputer(strategy="median")
#     df["total_bedrooms"] = imputer.fit_transform(df[["total_bedrooms"]])

#     # One-hot encode 'ocean_proximity'
#     encoder = OneHotEncoder()
#     ocean_proximity_encoded = encoder.fit_transform(df[["ocean_proximity"]]).toarray()

#     # Add one-hot encoded columns to the DataFrame
#     ocean_proximity_df = pd.DataFrame(ocean_proximity_encoded, columns=encoder.categories_[0])
#     df = pd.concat([df.drop("ocean_proximity", axis=1), ocean_proximity_df], axis=1)

#     # Feature scaling
#     scaler = StandardScaler()
#     scaled_columns = ["longitude", "latitude", "housing_median_age", "total_rooms", 
#                       "total_bedrooms", "population", "households", "median_income"]
#     df[scaled_columns] = scaler.fit_transform(df[scaled_columns])

#     return df

# # Step to split the data
# @step
# def split_data_step(df: pd.DataFrame):
#     X = df.drop("median_house_value", axis=1)
#     y = df["median_house_value"]
#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#     return X_train, X_test, y_train, y_test

# # Define the preprocessing pipeline
# @pipeline
# def data_preprocessing_pipeline(ingest_step, preprocess_step, split_step):
#     df = ingest_step()
#     processed_df = preprocess_step(df)
#     X_train, X_test, y_train, y_test = split_step(processed_df)
#     return X_train, X_test, y_train, y_test

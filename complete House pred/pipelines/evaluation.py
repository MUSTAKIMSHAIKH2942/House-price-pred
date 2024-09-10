# # pipelines/evaluation.py
# from zenml.pipelines import pipeline
# from zenml.steps import step
# from sklearn.metrics import mean_squared_error

# @step
# def evaluation_step(model, test_data):
#     X_test, y_test = test_data.drop('median_house_value', axis=1), test_data['median_house_value']
#     predictions = model.predict(X_test)
#     mse = mean_squared_error(y_test, predictions)
#     return mse


# @pipeline
# def evaluation_pipeline(training_step, evaluation_step, test_data_step):
#     model = training_step()
#     mse = evaluation_step(model, test_data_step())
#     return mse



from sklearn.metrics import mean_squared_error

def evaluate_model(model, X_test, y_test):
    """Evaluates the performance of the trained model."""
    # Making predictions
    predictions = model.predict(X_test)
    # Calculating Mean Squared Error
    mse = mean_squared_error(y_test, predictions)
    return mse



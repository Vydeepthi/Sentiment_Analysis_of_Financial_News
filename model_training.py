
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def train_model(features):
    """Selects and trains a machine learning model on the features."""
    # Splitting the data into features and target variable
    X = features[['Open', 'High', 'Low', 'Volume']]
    y = features['Close']
    # Splitting the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    # Training a linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model



import data_collection
import data_preprocessing
import feature_engineering
import model_training
import model_evaluation
import deployment
import monitoring_and_maintenance
from sklearn.model_selection import train_test_split

def main():
    # Step 1: Collect data
    data = data_collection.collect_data("TWTR.csv")

    # Step 2: Preprocess data
    preprocessed_data = data_preprocessing.preprocess_data(data)

    # Step 3: Extract features
    features = feature_engineering.extract_features(preprocessed_data)

    # Step 4: Train model
    trained_model = model_training.train_model(features)

    # Step 5: Evaluate model
    X = features[['Open', 'High', 'Low', 'Volume']]
    y = features['Close']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    mse = model_evaluation.evaluate_model(trained_model, X_test, y_test)
    print("Mean Squared Error:", mse)

    # Step 6: Deploy model
    deployment.deploy_model(trained_model)

    # Step 7: Monitor performance and conduct maintenance
    monitoring_and_maintenance.monitor_performance()
    monitoring_and_maintenance.conduct_maintenance()

if __name__ == "__main__":
    main()

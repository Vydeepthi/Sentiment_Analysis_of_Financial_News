import joblib

def deploy_model(trained_model):
    """Integrates and deploys the trained model for real-time analysis."""
    # Saving the trained model
    joblib.dump(trained_model, "trained_model.pkl")

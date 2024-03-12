
def deploy_model(model):
    """Integrates and deploys the trained model for real-time analysis."""
    # deployment involves saving the model for future use
    model.save("trained_model.pkl")

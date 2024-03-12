
def preprocess_data(data):
    """Preprocesses the collected data."""
    # Drop any rows with missing values
    data = data.dropna()
    # Convert Date column to datetime format
    data['Date'] = pd.to_datetime(data['Date'])
    return data



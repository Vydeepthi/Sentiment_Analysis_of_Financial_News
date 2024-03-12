
import pandas as pd

def collect_data(file_path):
    """Collects historical stock market data from CSV file."""
    data = pd.read_csv(file_path)
    return data



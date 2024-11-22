import pandas as pd

def run_analysis():
    # Load data from CSV (add your sample CSV file in the 'data' folder)
    data = pd.read_csv('data/sample.csv')

    # Perform analysis (calculate mean of a column)
    mean_value = data['value'].mean()

    return {'mean': mean_value}

import pandas as pd

def load_data(file):
    try:
        data = pd.read_csv(file)
        print(f"Data loaded successfully from {file}")
        return data

    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def get_basic_summary(df):
    summary = {
        'shape': df.shape,
        'columns': df.columns.tolist(),
        'data_types': df.dtypes,
        'missing_values': df.isnull().sum(),
        'descriptive_stats': df.describe(),
        'duplicates': df.duplicated().sum()
    }
    return summary

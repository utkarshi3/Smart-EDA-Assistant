import pandas as pd

def load_dataset(file_path: str):
    #Load dataset from CSV or JSON file.
    try:
        if file_path.endswith(".csv"):
            df = pd.read_csv(file_path)
        elif file_path.endswith(".json"):
            df = pd.read_json(file_path)
        else:
            raise ValueError("Unsupported file format. Use CSV or JSON.")

        return df

    except Exception as e:
        raise Exception(f"Error loading dataset: {e}")

def get_basic_summary(df: pd.DataFrame):
    #Returns basic dataset information.
    summary = {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "column_names": df.columns.tolist(),
        "dtypes": df.dtypes.astype(str).to_dict(),
        "missing_values": df.isnull().sum().to_dict(),
        "duplicate_count": int(df.duplicated().sum()),
        "memory_usage_MB": round(df.memory_usage(deep=True).sum() / (1024 ** 2), 2)
    }
    return summary

def get_column_types(df: pd.DataFrame):
    #Separates numerical and categorical columns.
    numerical_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
    categorical_cols = df.select_dtypes(include=["object", "category"]).columns.tolist()

    return {
        "numerical_columns": numerical_cols,
        "categorical_columns": categorical_cols
    }

def get_statistical_summary(df: pd.DataFrame):
    #Returns statistical summary for numerical columns.
    return df.describe().to_dict()
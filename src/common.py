import pandas as pd

def load_data(data_path: str, data_format: str = "csv") -> pd.DataFrame:
    """
    Load data from the given path.
    """
    if data_format == "csv":
        return pd.read_csv(data_path)
    else:
        raise ValueError(f"Unsupported data format: {data_format}")


def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Preprocess the data.
    """
    # Example preprocessing steps
    return df.dropna().drop(columns=["Id"]).reset_index(drop=True)

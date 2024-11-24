import pandas as pd

def save_to_csv(data: pd.DataFrame, file_path: str):
    data.to_csv(file_path)
    print(f"Data saved to {file_path}")

def read_from_csv(file_path: str) -> pd.DataFrame:
    try:
        data = pd.read_csv(file_path, index_col=0, parse_dates=True)
        print(f"Data read from {file_path}")
        return data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return pd.DataFrame()
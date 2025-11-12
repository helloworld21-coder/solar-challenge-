# Utility functions for data processing and visualization
import pandas as pd

def load_data(country: str):
    """
    Load dataset for the selected country.
    Replace the path below with your actual data folder path.
    """
    try:
        df = pd.read_csv(f"data/{country.lower()}_cleaned.csv")
        return df
    except FileNotFoundError:
        return pd.DataFrame()

def get_summary(df: pd.DataFrame):
    """
    Return top regions summary or any quick stats.
    """
    if df.empty:
        return pd.DataFrame()
    # Example: top 5 regions by average GHI
    return (
        df.groupby("Region")["GHI"]
        .mean()
        .sort_values(ascending=False)
        .head(5)
        .reset_index()
    )

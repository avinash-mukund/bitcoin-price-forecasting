import pandas as pd
import numpy as np

def load_and_preprocess(filepath: str) -> pd.DataFrame:
    """
    Load minute-level Bitcoin data, clean it, and resample to daily frequency.
    Creates features used in the research paper.
    """
    df = pd.read_csv(filepath)

    # Keep only necessary columns
    df = df[['timestamp', 'open', 'high', 'low', 'close', 'volume']]

    # Convert timestamp and set as index
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df = df.set_index('timestamp').sort_index()

    # Remove duplicates
    df = df[~df.index.duplicated(keep='first')]

    # Resample to daily frequency
    daily = df.resample('D').agg({
        'open': 'first',
        'high': 'max',
        'low': 'min',
        'close': 'last',
        'volume': 'sum'
    }).dropna()

    # Feature Engineering (exactly as used in the paper)
    daily['close_lag1'] = daily['close'].shift(1)
    daily['close_ma7'] = daily['close'].rolling(window=7).mean()
    daily['daily_return'] = daily['close'].pct_change()

    # Target: Next day's closing price
    daily['target'] = daily['close'].shift(-1)

    # Drop rows with NaN values created by shifting/rolling
    daily = daily.dropna()

    return daily

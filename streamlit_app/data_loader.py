import pandas as pd
from pathlib import Path

DATA_PATH = Path("data/raw/01_fund_master.csv")


def load_fund_master():
    return pd.read_csv(DATA_PATH)
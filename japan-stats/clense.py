import os
import sys

import pandas as pd
from dotenv import load_dotenv

load_dotenv()
sys.path.append(os.getenv("APPROOT"))

from common import DATA_PATH

CLENSED_DATA_PATH = DATA_PATH / "clensed"
CLENSED_DATA_PATH.mkdir(parents=True, exist_ok=True)


def social_stats():
    DOWNLOAD_PATH = DATA_PATH / "download"
    df = pd.concat([pd.read_csv(i) for i in DOWNLOAD_PATH.rglob("*.csv")])
    df.to_csv(CLENSED_DATA_PATH / "social_stats.csv", index=False)


if __name__ == "__main__":
    social_stats()

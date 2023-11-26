import pandas as pd
from common import DATA_PATH

CLENSED_DATA_PATH = DATA_PATH / "clensed"
CLENSED_DATA_PATH.mkdir(parents=True, exist_ok=True)


def social_stats():
    DOWNLOAD_PATH = DATA_PATH / "download/social_stats"
    df = pd.concat([pd.read_csv(i) for i in DOWNLOAD_PATH.rglob("*.csv")])

    output = CLENSED_DATA_PATH / "social_stats.csv"
    df.to_csv(output, index=False)
    print(f"saved: {output.name}")


if __name__ == "__main__":
    social_stats()

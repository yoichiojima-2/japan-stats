import os
import sys
import re
from pathlib import Path
import unicodedata

sys.path.append(str(Path(__file__).parent.parent))

import fetch_api
from common_process import cleanup_year, strip_prefix


def main():
    df = fetch_api.main("0000010103")
    df["year"] = df["調査年"].apply(cleanup_year)
    df["feature"] = df["Ｃ　経済基盤"].apply(strip_prefix)
    df = df.rename(columns = {"地域": "area", "@unit": "unit", "$": "value"})
    df = df[["feature", "year", "area", "unit", "value"]]

    df.to_csv(Path(os.getenv("APPROOT")) / "data/economics.csv", index = False)
    print("saved economics.csv")


if __name__ == "__main__":
    main()
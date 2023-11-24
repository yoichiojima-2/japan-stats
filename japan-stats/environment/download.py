import os
import sys
import re
from pathlib import Path
import unicodedata

sys.path.append(str(Path(__file__).parent.parent))

import fetch_api
from common_process import cleanup_year, strip_prefix


def main():
    df = fetch_api.main("0000010102")

    df["feature"] = df["Ｂ　自然環境"].apply(strip_prefix)
    df["year"] = df["調査年"].apply(cleanup_year)
    df["unit"] = df["@unit"].apply(lambda x: unicodedata.normalize("NFKC", x))

    df = df.rename(columns = {"地域": "area", "$": "value"})
    df = df[["feature", "year", "area", "unit", "value"]]

    df.to_csv(Path(os.getenv("APPROOT")) / "data/environment.csv", index = False)
    print("saved environment.csv")


if __name__ == "__main__":
    main()
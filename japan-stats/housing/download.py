import os
import sys
import re
from pathlib import Path
import unicodedata

sys.path.append(str(Path(__file__).parent.parent))

import fetch_api
from common import cleanup_year, strip_prefix, cleanup, extract_sex, DATA_PATH


def main():
    df = fetch_api.main("0000010108")
    df = cleanup(df, "Ｈ　居住")

    df.to_csv(DATA_PATH / "housing.csv", index=False)
    print("saved housing.csv")


if __name__ == "__main__":
    main()

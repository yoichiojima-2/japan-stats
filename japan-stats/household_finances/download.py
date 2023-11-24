import os
import sys
import re
from pathlib import Path
import unicodedata

sys.path.append(str(Path(__file__).parent.parent))

import fetch_api
from common import cleanup_year, strip_prefix, cleanup, DATA_PATH


def main():
    df = fetch_api.main("0000010112")
    df = cleanup(df, "Ｌ　家計")

    df.to_csv(DATA_PATH / "household_finances.csv", index=False)
    print("saved household_finances.csv")


if __name__ == "__main__":
    main()

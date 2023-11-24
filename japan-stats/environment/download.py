import os
import sys
import re
from pathlib import Path
import unicodedata

sys.path.append(str(Path(__file__).parent.parent))

import fetch_api
from common import cleanup_year, strip_prefix, cleanup, DATA_PATH


def main():
    df = fetch_api.main("0000010102")
    df = cleanup(df, "Ｂ　自然環境")

    df.to_csv(DATA_PATH / "environment.csv", index=False)
    print("saved environment.csv")


if __name__ == "__main__":
    main()

import os
import sys
import re
from pathlib import Path
import unicodedata

sys.path.append(str(Path(__file__).parent.parent))

import fetch_api
from common_process import cleanup_year, strip_prefix, cleanup


def main():
    df = fetch_api.main("0000010103")
    df = cleanup(df, "Ｃ　経済基盤")

    df.to_csv(Path(os.getenv("APPROOT")) / "data/economics.csv", index = False)
    print("saved economics.csv")


if __name__ == "__main__":
    main()
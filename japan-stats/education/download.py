import os
import sys
import re
from pathlib import Path
import unicodedata

sys.path.append(str(Path(__file__).parent.parent))

import fetch_api
from common import cleanup_year, strip_prefix, cleanup, DATA_PATH


def main():
    df = fetch_api.main("0000010105")
    df = cleanup(df, "Ｅ　教育")

    df.to_csv(DATA_PATH / "education.csv", index=False)
    print("saved education.csv")


if __name__ == "__main__":
    main()

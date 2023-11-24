import os
import sys
import re
from pathlib import Path
import unicodedata

sys.path.append(str(Path(__file__).parent.parent))

import fetch_api
from common import cleanup_year, strip_prefix, cleanup, DATA_PATH


def main():
    df = fetch_api.main("0000010110")
    df = cleanup(df, "Ｊ　福祉・社会保障")

    df.to_csv(DATA_PATH / "social_security.csv", index=False)
    print("saved social_security.csv")


if __name__ == "__main__":
    main()

import os
import sys
import re
from pathlib import Path
import unicodedata

sys.path.append(str(Path(__file__).parent.parent))

import fetch_api
from common_process import cleanup_year, strip_prefix, cleanup


def main():
    df = fetch_api.main("0000010110")
    df = cleanup(df, "Ｊ　福祉・社会保障")

    df.to_csv(Path(os.getenv("APPROOT")) / "data/social_security.csv", index = False)
    print("saved social_security.csv")


if __name__ == "__main__":
    main()

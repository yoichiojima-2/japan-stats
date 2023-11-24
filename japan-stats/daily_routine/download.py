import os
import sys
import re
from pathlib import Path
import unicodedata

sys.path.append(str(Path(__file__).parent.parent))

import fetch_api
from common_process import cleanup_year, strip_prefix, cleanup, extract_sex


def main():
    df = fetch_api.main("0000010113")
    df = cleanup(df, "Ｍ　生活時間")
    df["sex"] = df["feature"].apply(extract_sex)

    df.to_csv(Path(os.getenv("APPROOT")) / "data/daily_routine.csv", index = False)
    print("saved daily_routine.csv")


if __name__ == "__main__":
    main()
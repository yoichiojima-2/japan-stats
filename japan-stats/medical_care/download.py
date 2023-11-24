import os
import sys
import re
from pathlib import Path
import unicodedata

sys.path.append(str(Path(__file__).parent.parent))

import fetch_api
from common_process import cleanup_year, strip_prefix, cleanup, extract_sex


def main():
    df = fetch_api.main("0000010109")
    df = cleanup(df, "Ｉ　健康・医療")
    df["sex"] = df["feature"].apply(extract_sex)

    df.to_csv(Path(os.getenv("APPROOT")) / "data/medical_care.csv", index = False)
    print("saved medical_care.csv")


if __name__ == "__main__":
    main()

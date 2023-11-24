import os
import sys
from pathlib import Path
import re

sys.path.append(str(Path(__file__).parent.parent))
import fetch_api
from common_process import cleanup_year, cleanup


def main():
    df = fetch_api.main("0000010101")
    df = cleanup(df, "Ａ　人口・世帯")

    df = df[df["area"] != "全国"]

    df["sex"] = df["feature"].apply(extract_sex)
    df["age"] = df["feature"].apply(extract_age)

    df = df[["year", "area", "sex", "age", "value"]].dropna()
    df = df.sort_values(["year", "area", "sex", "age"])

    df.to_csv(Path(os.getenv("APPROOT")) / "data/population.csv", index = False)
    print("saved population.csv")


def extract_sex(feature):
    if "女" in feature:
        return "F"
    elif "男" in feature:
        return "M"
    else:
        return None


def extract_age(feature):
    _match = re.search(r"(\d{2})～(\d{2})", feature)
    if _match:
        return _match.group(1), _match.group(2)


if __name__ == "__main__":
    main()

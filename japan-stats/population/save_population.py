import os
import sys
from pathlib import Path
import re

sys.path.append(str(Path(__file__).parent.parent))
import fetch_estats


def main():
    df = fetch_estats.main("0000010101")

    df = df[df["地域"] != "全国"]

    df["sex"] = df["Ａ　人口・世帯"].apply(extract_sex)
    df["age"] = df["Ａ　人口・世帯"].apply(extract_age)
    df["year"] = df["調査年"].apply(cleanup_year)

    df = df.rename(columns={"地域": "area", "$": "population"})
    df = df[["year", "area", "sex", "age", "population"]].dropna()
    df = df.sort_values(["year", "area", "sex", "age"])

    df.to_csv(Path(os.getenv("APPROOT")) / "data/population.csv")
    print("saved population.csv")


def extract_sex(value):
    if "女" in value:
        return "F"
    elif "男" in value:
        return "M"
    else:
        return None


def extract_age(value):
    _match = re.search(r"(\d{2})～(\d{2})", value)
    if _match:
        return _match.group(1), _match.group(2)


def cleanup_year(year):
    _match = re.search(r"\d*", year)
    if _match:
        return _match.group()


if __name__ == "__main__":
    main()

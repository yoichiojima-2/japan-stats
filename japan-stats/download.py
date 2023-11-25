import os
import sys
import re
from pathlib import Path
from dotenv import load_dotenv

sys.path.append(str(Path(__file__).parent.parent))

import fetch_api

load_dotenv()
DATA_PATH = Path(os.getenv("APPROOT")) / "data"


def population():
    df = fetch_api.main("0000010101")
    df = cleanup(df, "Ａ　人口・世帯")

    df = df[df["area"] != "全国"]

    df["sex"] = df["feature"].apply(extract_sex)
    df["age"] = df["feature"].apply(extract_age)

    df = df[["year", "area", "sex", "age", "value"]].dropna()
    df = df.sort_values(["year", "area", "sex", "age"])

    output = DATA_PATH / "population.csv"
    df.to_csv(output, index=False)
    print(f"saved {output}")


def environment():
    df = fetch_api.main("0000010102")
    df = cleanup(df, "Ｂ　自然環境")

    output = DATA_PATH / "environment.csv"
    df.to_csv(output, index=False)
    print(f"saved {output}")


def economics():
    df = fetch_api.main("0000010103")
    df = cleanup(df, "Ｃ　経済基盤")

    output = DATA_PATH / "economics.csv"
    df.to_csv(output, index=False)
    print(f"saved {output}")


def administration():
    df = fetch_api.main("0000010104")
    df = cleanup(df, "Ｄ　行政基盤")

    output = DATA_PATH / "administration.csv"
    df.to_csv(output, index=False)
    print(f"saved {output}")


def education():
    df = fetch_api.main("0000010105")
    df = cleanup(df, "Ｅ　教育")

    output = DATA_PATH / "education.csv"
    df.to_csv(output, index=False)
    print(f"saved {output}")


def labour():
    df = fetch_api.main("0000010106")
    df = cleanup(df, "Ｆ　労働")
    df["sex"] = df["feature"].apply(extract_sex)

    output = DATA_PATH / "labour.csv"
    df.to_csv(output, index=False)
    print(f"saved {output}")


def culture():
    df = fetch_api.main("0000010107")
    df = cleanup(df, "Ｇ　文化・スポーツ")

    output = DATA_PATH / "culture.csv"
    df.to_csv(output, index=False)
    print(f"saved {output}")


def housing():
    df = fetch_api.main("0000010108")
    df = cleanup(df, "Ｈ　居住")

    output = DATA_PATH / "housing.csv"
    df.to_csv(output, index=False)
    print(f"saved {output}")


def medical_care():
    df = fetch_api.main("0000010109")
    df = cleanup(df, "Ｉ　健康・医療")
    df["sex"] = df["feature"].apply(extract_sex)

    output = DATA_PATH / "medical_care.csv"
    df.to_csv(output, index=False)
    print(f"saved {output}")


def social_security():
    df = fetch_api.main("0000010110")
    df = cleanup(df, "Ｊ　福祉・社会保障")

    output = DATA_PATH / "social_security.csv"
    df.to_csv(output, index=False)
    print(f"saved {output}")


def household_finances():
    df = fetch_api.main("0000010112")
    df = cleanup(df, "Ｌ　家計")

    output = DATA_PATH / "household_finances.csv"
    df.to_csv(output, index=False)
    print(f"saved {output}")


def daily_routine():
    df = fetch_api.main("0000010113")
    df = cleanup(df, "Ｍ　生活時間")
    df["sex"] = df["feature"].apply(extract_sex)

    output = DATA_PATH / "daily_routine.csv"
    df.to_csv(output, index=False)
    print(f"saved {output}")


def download_all():
    population()
    environment()
    economics()
    administration()
    education()
    labour()
    culture()
    housing()
    medical_care()
    social_security()
    household_finances()
    daily_routine()


def cleanup_year(year):
    _match = re.search(r"\d*", year)
    if _match:
        return _match.group()


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


def strip_prefix(feature):
    return re.sub(r"\w\d*_", "", feature)


def cleanup(df, feature_col):
    df["year"] = df["調査年"].apply(cleanup_year)
    df["feature"] = df[feature_col].apply(strip_prefix)
    df = df.rename(columns={"地域": "area", "@unit": "unit", "$": "value"})
    return df[["feature", "year", "area", "unit", "value"]]


if __name__ == "__main__":
    download_all()

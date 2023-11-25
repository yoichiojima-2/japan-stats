import re

import fetch_api
from common import DATA_PATH

DOWNLOAD_PATH = DATA_PATH / "download"
DOWNLOAD_PATH.mkdir(parents=True, exist_ok=True)


def population():
    df = fetch_api.main("0000010101")
    df = cleanup(df, "Ａ　人口・世帯", "population")

    df = df[df["area"] != "全国"]

    df["sex"] = df["feature"].apply(extract_sex)
    df["age"] = df["feature"].apply(extract_age)

    df = df[["feature", "year", "area", "sex", "age", "category", "value"]].dropna()
    df = df.sort_values(["year", "area", "sex", "age"])

    output = DOWNLOAD_PATH / "population.csv"
    df.to_csv(output, index=False)
    print(f"saved {output}")


def environment():
    df = fetch_api.main("0000010102")
    df = cleanup(df, "Ｂ　自然環境", "environment")

    output = DOWNLOAD_PATH / "environment.csv"
    df.to_csv(output, index=False)
    print(f"saved {output}")


def economics():
    df = fetch_api.main("0000010103")
    df = cleanup(df, "Ｃ　経済基盤", "economics")

    output = DOWNLOAD_PATH / "economics.csv"
    df.to_csv(output, index=False)
    print(f"saved {output}")


def administration():
    df = fetch_api.main("0000010104")
    df = cleanup(df, "Ｄ　行政基盤", "administration")

    output = DOWNLOAD_PATH / "administration.csv"
    df.to_csv(output, index=False)
    print(f"saved {output}")


def education():
    df = fetch_api.main("0000010105")
    df = cleanup(df, "Ｅ　教育", "education")

    output = DOWNLOAD_PATH / "education.csv"
    df.to_csv(output, index=False)
    print(f"saved {output}")


def labour():
    df = fetch_api.main("0000010106")
    df = cleanup(df, "Ｆ　労働", "labour")
    df["sex"] = df["feature"].apply(extract_sex)

    output = DOWNLOAD_PATH / "labour.csv"
    df.to_csv(output, index=False)
    print(f"saved {output}")


def culture():
    df = fetch_api.main("0000010107")
    df = cleanup(df, "Ｇ　文化・スポーツ", "culture")

    output = DOWNLOAD_PATH / "culture.csv"
    df.to_csv(output, index=False)
    print(f"saved {output}")


def housing():
    df = fetch_api.main("0000010108")
    df = cleanup(df, "Ｈ　居住", "housing")

    output = DOWNLOAD_PATH / "housing.csv"
    df.to_csv(output, index=False)
    print(f"saved {output}")


def medical_care():
    df = fetch_api.main("0000010109")
    df = cleanup(df, "Ｉ　健康・医療", "medical_care")
    df["sex"] = df["feature"].apply(extract_sex)

    output = DOWNLOAD_PATH / "medical_care.csv"
    df.to_csv(output, index=False)
    print(f"saved {output}")


def social_security():
    df = fetch_api.main("0000010110")
    df = cleanup(df, "Ｊ　福祉・社会保障", "social_security")

    output = DOWNLOAD_PATH / "social_security.csv"
    df.to_csv(output, index=False)
    print(f"saved {output}")


def household_finances():
    df = fetch_api.main("0000010112")
    df = cleanup(df, "Ｌ　家計", "household_finances")

    output = DOWNLOAD_PATH / "household_finances.csv"
    df.to_csv(output, index=False)
    print(f"saved {output}")


def daily_routine():
    df = fetch_api.main("0000010113")
    df = cleanup(df, "Ｍ　生活時間", "daily_routine")
    df["sex"] = df["feature"].apply(extract_sex)

    output = DOWNLOAD_PATH / "daily_routine.csv"
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


def cleanup(df, feature_col, category):
    df["year"] = df["調査年"].apply(cleanup_year)
    df["feature"] = df[feature_col].apply(strip_prefix)
    df["category"] = category
    df = df.rename(columns={"地域": "area", "@unit": "unit", "$": "value"})
    return df[["feature", "year", "area", "category", "unit", "value"]]


if __name__ == "__main__":
    download_all()

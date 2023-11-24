import re


def cleanup_year(year):
    _match = re.search(r"\d*", year)
    if _match:
        return _match.group()


def strip_prefix(metrix_title):
    return re.sub(r"\w\d*_", "", metrix_title)


def cleanup(df, feature_col):
    df["year"] = df["調査年"].apply(cleanup_year)
    df["feature"] = df[feature_col].apply(strip_prefix)
    df = df.rename(columns = {"地域": "area", "@unit": "unit", "$": "value"})
    return df[["feature", "year", "area", "unit", "value"]]
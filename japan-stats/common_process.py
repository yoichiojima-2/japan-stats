import re


def cleanup_year(year):
    _match = re.search(r"\d*", year)
    if _match:
        return _match.group()


def strip_prefix(feature):
    return re.sub(r"\w\d*_", "", feature)


def cleanup(df, feature_col):
    df["year"] = df["調査年"].apply(cleanup_year)
    df["feature"] = df[feature_col].apply(strip_prefix)
    df = df.rename(columns = {"地域": "area", "@unit": "unit", "$": "value"})
    return df[["feature", "year", "area", "unit", "value"]]
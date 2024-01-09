# this setup sqlite in data/ for analysis.

import dataclasses
import enum
import os
from pathlib import Path
import re
import sqlite3
import urllib

import dotenv
import pandas as pd
import requests
from requests.models import Response
import tqdm


def main():
    create_pretables()
    create_clensed_tables()


DATA_DIR = Path("./data")
DATA_DIR.mkdir(exist_ok=True, parents=True)


@dataclasses.dataclass
class ClassData:
    id: str
    name: str
    data: pd.DataFrame


@dataclasses.dataclass
class StatsData:
    response: Response

    def get_values(self) -> pd.DataFrame:
        return pd.DataFrame(self.response.json()["GET_STATS_DATA"]["STATISTICAL_DATA"]["DATA_INF"]["VALUE"])

    def get_class(self) -> list[ClassData]:
        class_list: list[ClassData] = []
        class_obj = self.response.json()["GET_STATS_DATA"]["STATISTICAL_DATA"]["CLASS_INF"]["CLASS_OBJ"]
        for c in class_obj:
            data = c["CLASS"]
            class_list.append(
                ClassData(
                    id=c["@id"],
                    name=c["@name"],
                    data=pd.DataFrame(data if isinstance(data, list) else [data]),
                )
            )
        return class_list


def fetch(endpoint: str, params: dict[str, str]) -> Response:
    base_url: str = f"https://api.e-stat.go.jp/rest/{os.getenv('API_VERSION')}/app/json/"
    url = urllib.parse.urljoin(base_url, endpoint)
    return requests.get(url, params=params)


def create_pretables():
    dotenv.load_dotenv()

    endpoint: str = "getStatsData"
    params_comprehensive: dict[str, str] = {
        "appId": os.getenv("APP_ID"),
        "statsDataId": StatId.population.value,
    }
    print("fetching class data...")
    stats_res = fetch(endpoint, params_comprehensive)
    stats_data = StatsData(stats_res)
    classes = stats_data.get_class()

    for i in classes:
        if i.id == "cat01":
            cat01_df = i.data.copy()

    cat01_df["num_in_code"] = cat01_df["@code"].apply(lambda x: extract_num_from_code(x))
    population_age_gender_codes = cat01_df[cat01_df["num_in_code"].between(120101, 122102)]["@code"].to_list()

    dfs: list[pd.DataFrame] = []
    for i in tqdm.tqdm(population_age_gender_codes, desc="fetching record data..."):
        res = query_by_cat01(i)
        i_stats_data = StatsData(res)
        dfs.append(i_stats_data.get_values())

    conn = sqlite3.connect(str(DATA_DIR / "pre-japan-stats.db"))
    pd.concat(dfs).to_sql("population_record", conn, if_exists="replace", index=False)
    print("record data saved.")

    for i in tqdm.tqdm(classes, desc="saving class data..."):
        i.data.to_sql(i.id, conn, if_exists="replace", index=False)

    print("class data saved")

    print("pre-japan-stats.db preparation created.")


def create_clensed_tables():
    conn_pre = sqlite3.connect("./data/pre-japan-stats.db")

    record = remove_at_sign_from_cols(pd.read_sql("select * from population_record;", conn_pre))

    class_data = {
        "tab": pd.read_sql("select * from tab", conn_pre),
        "cat01": pd.read_sql("select * from cat01", conn_pre).drop(columns="@unit"),
        "area": pd.read_sql("select * from area", conn_pre),
        "time": pd.read_sql("select * from time", conn_pre),
    }

    cat01_codes = cat01_table(class_data)["code"].unique()
    area_codes = area_table(class_data)["code"].unique()

    conn = sqlite3.connect(str(DATA_DIR / "japan-stats.db"))

    clense_record(record, cat01_codes, area_codes).to_sql("population_record", conn, index=False, if_exists="replace")
    cat01_table(class_data).to_sql("cat01", conn, index=False, if_exists="replace")
    area_table(class_data).to_sql("area", conn, index=False, if_exists="replace")
    time_table(class_data).to_sql("time", conn, index=False, if_exists="replace")
    print("japan-stats.db preparation created.")


class StatId(enum.Enum):
    population: str = "0000010101"
    environment: str = "0000010102"
    economics: str = "0000010103"
    administration: str = "0000010104"
    education: str = "0000010105"
    labour: str = "0000010106"
    culture: str = "0000010107"
    housing: str = "0000010108"
    medical_care: str = "0000010109"
    social_security: str = "0000010110"
    household_finance: str = "0000010111"
    daily_routine: str = "0000010112"


def extract_num_from_code(code: str) -> int:
    match_obj = re.search(r"A([0-9]*)", code)
    if match_obj:
        return int(match_obj.group(1))


def query_by_cat01(cat01: str) -> requests.models.Response:
    endpoint: str = "getStatsData"
    params: dict[str, str] = {
        "appId": os.getenv("APP_ID"),
        "statsDataId": StatId.population.value,
        "cdCat01": cat01,
    }
    return fetch(endpoint, params)


def extract_num_from_code(code: str) -> int:
    match_obj = re.search(r"A([0-9]*)", code)
    if match_obj:
        return int(match_obj.group(1))


def get_age_class(code: str) -> int:
    match_obj = re.search(r"A12([0-9]{2})[0-9]{2}", code)
    if match_obj:
        return int(match_obj.group(1)) - 1


def extract_year(year_str: str) -> int:
    match_obj = re.search(r"([0-9]{4}).*", year_str)
    if match_obj:
        return int(match_obj.group(1))


def remove_at_sign_from_cols(df: pd.DataFrame) -> pd.DataFrame:
    return df.rename(columns={c: c.replace("@", "") for c in df.columns})


def cat01_table(class_data: dict[str, pd.DataFrame]) -> pd.DataFrame:
    cat01_df = class_data["cat01"].copy()
    cat01_df["age_class"] = cat01_df["@code"].apply(get_age_class)
    cat01_df["n"] = cat01_df["@code"].apply(extract_num_from_code)
    cat01_df = cat01_df[cat01_df["n"].between(120101, 122102)]
    cat01_df["sex"] = cat01_df["n"].apply(lambda x: "F" if x % 2 == 0 else "M")
    return remove_at_sign_from_cols(
        cat01_df[["@code", "age_class", "sex"]].astype({"@code": str, "age_class": int, "sex": str})
    )


def area_table(class_data: dict[str, pd.DataFrame]) -> pd.DataFrame:
    area_df = class_data["area"].copy()
    area_df = area_df[area_df["@level"] == "2"].drop(columns="@level")
    return remove_at_sign_from_cols(area_df)


def time_table(class_data: dict[str, pd.DataFrame]) -> pd.DataFrame:
    time_df = class_data["time"].copy()
    time_df["year"] = time_df["@name"].apply(extract_year)
    return remove_at_sign_from_cols(time_df[["@code", "year"]])


def clense_record(record: pd.DataFrame, cat01_codes: list[str], area_codes: list[str]) -> pd.DataFrame:
    record = record[(record["cat01"].isin(cat01_codes)) & (record["area"].isin(area_codes))]
    return record.rename(columns={"$": "value"})[["cat01", "time", "area", "value"]]


if __name__ == "__main__":
    main()

import os
import enum
import dataclasses
import pathlib
import re
import sqlite3
import requests
from requests.models import Response
import tqdm
import pandas as pd
import urllib
import dotenv

dotenv.load_dotenv()


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


def fetch(endpoint: str, params: dict[str, str]):
    base_url: str = f"https://api.e-stat.go.jp/rest/{os.getenv('API_VERSION')}/app/json/"
    url = urllib.parse.urljoin(base_url, endpoint)
    return requests.get(url, params=params)


def extract_num_from_code(code: str) -> int:
    match_obj = re.search(r"A([0-9]*)", code)
    if match_obj:
        return int(match_obj.group(1))


def query_by_cat01(cat01: str):
    endpoint: str = "getStatsData"
    params: dict[str, str] = {
        "appId": os.getenv("APP_ID"),
        "statsDataId": StatId.population.value,
        "cdCat01": i,
    }
    return fetch(endpoint, params)


def main():
    endpoint: str = "getStatsData"
    params: dict[str, str] = {
        "appId": os.getenv("APP_ID"),
        "statsDataId": StatId.population.value,
    }
    stats_res = fetch(endpoint, params)
    stats_data = StatsData(stats_res)

    p = pathlib.Path("./data")
    p.mkdir(exist_ok=True, parents=True)

    endpoint: str = "getStatsData"
    params: dict[str, str] = {
        "appId": os.getenv("APP_ID"),
        "statsDataId": StatId.population.value,
    }

    stats_res = fetch(endpoint, params)
    for i in stats_data.get_class():
        if i.id == "cat01":
            cat01_df = i.data

    cat01_df["num_in_code"] = cat01_df["@code"].apply(lambda x: extract_num_from_code(x))
    population_age_gender_codes = cat01_df[cat01_df["num_in_code"].between(120101, 122102)]["@code"].to_list()

    dfs: list[pd.DataFrame] = []

    for i in tqdm.tqdm(population_age_gender_codes, desc="fetching data"):
        res = query_by_cat01(i)
        i_stats_data = StatsData(res)
        dfs.append(i_stats_data.get_values())

    conn = sqlite3.connect("./data/population.db")
    pd.concat(dfs).to_sql("sex_age_area", conn, if_exists="replace")
    print("done.")


if __name__ == "__main__":
    main()

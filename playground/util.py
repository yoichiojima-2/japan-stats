import enum
import os
import pathlib
import re
import sqlite3
import urllib

import dotenv
import pandas as pd
import requests
import stats_data
import tqdm


def main():
    dotenv.load_dotenv()

    endpoint: str = "getStatsData"
    params_conpregensive: dict[str, str] = {
        "appId": os.getenv("APP_ID"),
        "statsDataId": StatId.population.value,
    }
    stats_res = fetch(endpoint, params_conpregensive)
    stats_data = stats_data.StatsData(stats_res)

    for i in stats_data.get_class():
        if i.id == "cat01":
            cat01_df = i.data

    cat01_df["num_in_code"] = cat01_df["@code"].apply(lambda x: extract_num_from_code(x))
    population_age_gender_codes = cat01_df[cat01_df["num_in_code"].between(120101, 122102)]["@code"].to_list()

    dfs: list[pd.DataFrame] = []
    for i in tqdm.tqdm(population_age_gender_codes, desc="fetching data"):
        res = query_by_cat01(i)
        i_stats_data = stats_data.StatsData(res)
        dfs.append(i_stats_data.get_values())

    p = pathlib.Path("./data")
    p.mkdir(exist_ok=True, parents=True)

    conn = sqlite3.connect("./data/population.db")
    pd.concat(dfs).to_sql("sex_age_area", conn, if_exists="replace")
    print("done.")


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


def fetch(endpoint: str, params: dict[str, str]) -> requests.models.Response:
    base_url: str = f"https://api.e-stat.go.jp/rest/{os.getenv('API_VERSION')}/app/json/"
    url = urllib.parse.urljoin(base_url, endpoint)
    return requests.get(url, params=params)


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


if __name__ == "__main__":
    main()

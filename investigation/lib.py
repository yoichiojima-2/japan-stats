import os
from enum import Enum
import dataclasses
import requests
from requests.models import Response
import dotenv
import pandas as pd


class StatId(Enum):
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

def get_data(stat_id: str) -> Response:
    base_url: str = f"https://api.e-stat.go.jp/rest/{os.getenv('API_VERSION')}/app/json/getStatsData"
    params: dict[str, str] = {
      "appId": os.getenv('APP_ID'),
      "statsDataId": stat_id
    }
    return requests.get(base_url, params = params)

def extract_data(res: Response) -> pd.DataFrame:
    return pd.DataFrame(res.json()["GET_STATS_DATA"]["STATISTICAL_DATA"]["DATA_INF"]["VALUE"])

@dataclasses.dataclass
class ClassData:
    id: str
    name: str
    data: pd.DataFrame

def extract_classes(res: Response) -> list[ClassData]:
    class_list: list[ClassData] = []
    class_obj: list[dict]= res.json()["GET_STATS_DATA"]["STATISTICAL_DATA"]["CLASS_INF"]["CLASS_OBJ"]
    for c in class_obj:
        data = c["CLASS"]
        class_list.append(
            ClassData(
                id = c["@id"],
                name = c["@name"],
                data = pd.DataFrame(data if isinstance(data, list) else [data])
            )
        )
    return class_list
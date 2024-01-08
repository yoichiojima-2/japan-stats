import dataclasses

import pandas as pd
import requests


@dataclasses.dataclass
class ClassData:
    id: str
    name: str
    data: pd.DataFrame


@dataclasses.dataclass
class StatsData:
    response: requests.models.Response

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

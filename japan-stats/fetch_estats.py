import os
import sys
from dotenv import load_dotenv
import pandas as pd

load_dotenv()
sys.path.append(os.getenv("APPROOT"))

import api


def fetch_estats(_id):
    """https://www.e-stat.go.jp/stat-search/database?page=1&layout=datalist&toukei=00200502&tstat=000001111375&cycle=8&tclass1=000001111377&result_page=1&tclass2val=0"""

    res = api.get_stats_data(_id, limit = None)

    values = res["GET_STATS_DATA"]["STATISTICAL_DATA"]["DATA_INF"]["VALUE"]
    cls_obj = res["GET_STATS_DATA"]["STATISTICAL_DATA"]["CLASS_INF"]["CLASS_OBJ"]

    df = pd.DataFrame(values)

    rename_hash = {"@" + i["@id"]: i["@name"] for i in cls_obj}

    for i in cls_obj:
        _cls = i["CLASS"]
        col_name = "@" + i["@id"]

        if isinstance(_cls, dict):
            _hash = {_cls["@code"]: _cls["@name"]}
        elif isinstance(_cls, list):
            _hash = {i["@code"]: i["@name"] for i in _cls}
        else:
            pass

        df[col_name] = df[col_name].apply(lambda x: _hash[x])
    
    return df.rename(columns = rename_hash)
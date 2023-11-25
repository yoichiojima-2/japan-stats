import api_wrapper
import pandas as pd


def main(_id):
    """https://www.e-stat.go.jp/stat-search/database"""

    res = api_wrapper.get_stats_data(_id, limit=None)

    values = res["GET_STATS_DATA"]["STATISTICAL_DATA"]["DATA_INF"]["VALUE"]
    cls_obj = res["GET_STATS_DATA"]["STATISTICAL_DATA"]["CLASS_INF"]["CLASS_OBJ"]

    df = pd.DataFrame(values)

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

    return df.rename(columns={"@" + i["@id"]: i["@name"] for i in cls_obj})

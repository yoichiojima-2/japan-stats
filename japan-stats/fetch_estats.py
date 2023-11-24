import os
import sys
from argparse import ArgumentParser
from dotenv import load_dotenv
import pandas as pd

load_dotenv()
sys.path.append(os.getenv("APPROOT"))

import api


def main(_id):
    """https://www.e-stat.go.jp/stat-search/database"""

    res = api.get_stats_data(_id, limit=None)

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


def parse_args():
    parser = ArgumentParser()
    parser.add_argument("--id", type=str)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    main(args.id)

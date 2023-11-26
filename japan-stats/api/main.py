import os
from pathlib import Path
from fastapi import FastAPI

import pandas as pd
from dotenv import load_dotenv

load_dotenv()

CLENSED_PATH = Path(os.getenv("APPROOT")) / "data/clensed"

app = FastAPI()


@app.get("/social_stats/features")
def get_social_stats_features():
    df = pd.read_csv(CLENSED_PATH / "social_stats.csv")
    return {"values": df["feature"].values.tolist()}

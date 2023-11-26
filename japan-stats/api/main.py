import os
from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import pandas as pd
from dotenv import load_dotenv

load_dotenv()

CLENSED_PATH = Path(os.getenv("APPROOT")) / "data/clensed"

app = FastAPI()

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True, 
    allow_methods = ["*"],
    allow_headers = ["*"]
)


@app.get("/social_stats/features")
def get_social_stats_features():
    df = (
        pd.read_csv(CLENSED_PATH / "social_stats.csv")
    )
    features = list({i for i in df["feature"].values})
    return {"values": features}

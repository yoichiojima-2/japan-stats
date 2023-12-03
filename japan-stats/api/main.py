import os
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

CLENSED_PATH = Path(os.getenv("APPROOT")) / "data/clensed"

app = FastAPI()

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/social_stats/categories")
def get_social_stats_category():
    df = pd.read_csv(CLENSED_PATH / "social_stats.csv")
    categories = list({i for i in df["category"].values})
    return list(sorted(categories))

@app.get("/social_stats/features")
def get_social_stats_features(category: str = None):
    df = pd.read_csv(CLENSED_PATH / "social_stats.csv")
    if category:
        df = df[df["category"] == category]
    features = list({i for i in df["feature"].values})
    return list(sorted(features))

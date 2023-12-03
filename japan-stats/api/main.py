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
    categories = (
        pd.read_csv(CLENSED_PATH / "social_stats.csv")
        ["category"]
        .drop_duplicates()
        .sort_values()
    )
    for i in categories:
        yield i


@app.get("/social_stats/features")
def get_social_stats_features(category: str):
    df = pd.read_csv(CLENSED_PATH / "social_stats.csv")
    features = (
        df[df["category"] == category]
        ["feature"]
        .drop_duplicates()
        .sort_values()
    )
    for i in features:
        yield i

@app.get("/social_stats/years")
def get_social_stats_years(feature: str):
    df = pd.read_csv(CLENSED_PATH / "social_stats.csv")
    years = (
        df[df["feature"] == feature]
        ["year"]
        .drop_duplicates()
        .sort_values()
    )
    for i in years:
        yield i

@app.get("/social_stats/area")
def get_social_stats_years(feature: str):
    df = pd.read_csv(CLENSED_PATH / "social_stats.csv")
    area = (
        df[df["feature"] == feature]
        ["area"]
        .drop_duplicates()
        .sort_values()
    )
    for i in area:
        yield i

@app.get("/social_stats/values")
def get_social_stats_values(feature: str, area: str):
    df = pd.read_csv(CLENSED_PATH / "social_stats.csv")
    df = (
        df[(df["feature"] == feature) & (df["area"] == area)]
        [["year", "value"]]
        .drop_duplicates()
        .set_index("year")
        .sort_index()
    )
    for idx, val in df.iterrows():
        yield {"year": idx, "value": int(val["value"])}
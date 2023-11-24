import os

import requests
from dotenv import load_dotenv

VERSION = "3.0"
load_dotenv()


def get_stats_list(
    surveyYears=None,
    openYears=None,
    statsField=None,
    statsCode=None,
    searchWord=None,
    searchKind=None,
    collectArea=None,
    explanationGetFlg=None,
    statsNameList=None,
    startPosition=None,
    limit=20,
    updateDate=None,
    callback=None,
):
    appId = os.getenv("APPID")
    return requests.get(
        f"https://api.e-stat.go.jp/rest/{VERSION}/app/json/getStatsList",
        params=locals(),
    ).json()


def get_meta_info(statsDataId, explanationGetFlg=None, callback=None):
    appId = os.getenv("APPID")
    return requests.get(
        f"https://api.e-stat.go.jp/rest/{VERSION}/app/json/getMetaInfo", params=locals()
    ).json()


def get_stats_data(
    statsDataId=None,
    dataSetId=None,
    lvTab=None,
    cdTab=None,
    colTabFrom=None,
    colTabTo=None,
    lvTime=None,
    cdTime=None,
    cdTimeFrom=None,
    cdTimeTo=None,
    lvArea=None,
    cdArea=None,
    cdAreaFrom=None,
    cdAreaTo=None,
    lvCat01=None,
    cdCat01=None,
    cdCat01From=None,
    cdCat01To=None,
    startPosition=None,
    limit=10,
    metaGetFlg=None,
    cntGetFlg=None,
    explanationGetFlg=None,
    annotationGetFlg=None,
    replaceSpChar=None,
    callback=None,
    sectionHeaderFlg=None,
):
    appId = os.getenv("APPID")
    return requests.get(
        f"https://api.e-stat.go.jp/rest/{VERSION}/app/json/getStatsData",
        params=locals(),
    ).json()


def get_data_catalog(
    surveyYear=None,
    openYears=None,
    statsField=None,
    statsCode=None,
    searchWord=None,
    collectArea=None,
    explanationGetFlg=None,
    dataType="CSV",
    startPosition=None,
    catalogId=None,
    resourceId=None,
    limit=20,
    updatedDate=None,
    callback=None,
):
    appId = os.getenv("APPID")
    return requests.get(
        f"https://api.e-stat.go.jp/rest/{VERSION}/app/json/getDataCatalog",
        params=locals(),
    ).json()

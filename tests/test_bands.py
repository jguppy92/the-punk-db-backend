import json
import pytest
import requests
from graphene_django.utils.testing import graphql_query
from graphene.test import Client
from bands.schema import schema

client = Client(schema)

ENDPOINT = "http://localhost:8000/graphql"

def test_get_all_bands():
    query_all_bands = """
        {
            allBands{
                id
                name
            }
        }
    """
    res = requests.post(
        ENDPOINT,
        json={
            'query': query_all_bands
        },
        timeout=3.0
    )
    res_body = res.json()
    print(res_body)
    assert res.status_code == 200

def test_new_band(band_1):
    print(band_1)
    assert band_1

def test_filter_bands(band_1):
    test_band_id = band_1["data"]["createBand"]["band"]["id"]
    filter_bands = f"""
        \u007b
            filterBands(id:{test_band_id})\u007b
                id
                name
            \u007d
        \u007d
    """
    res = requests.post(
        ENDPOINT,
        json={
            'query': filter_bands
        },
        timeout=3.0
    )
    res_body = res.json()
    print(res_body)
    assert res.status_code == 200 and res_body["data"]["filterBands"]["name"] == "Black Flag"

def test_delete_band_mutation(band_1):
    band_id = band_1["data"]["createBand"]["band"]["id"]
    print(band_id)
    delete_band_mutation = f"""
            mutation \u007b
                deleteBand(id:{band_id})\u007b
                    band \u007b
                        id
                    \u007d
                \u007d
            \u007d
        """
    res = requests.post(
        ENDPOINT,
        json={
            'query': delete_band_mutation
            },
        timeout=3
    )
    print(res.json())
    assert res.status_code == 200

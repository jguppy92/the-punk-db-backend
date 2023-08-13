# import requests

# ENDPOINT = "http://localhost:8000/graphql"

# def test():
#     response = requests.post(ENDPOINT)
#     print(response)
#     assert 1 == 1

import json
import pytest
import requests
from graphene_django.utils.testing import graphql_query
# import conftest

ENDPOINT = "http://localhost:8000/graphql"

def test_create_band():
    res = requests.post(
        ENDPOINT,
        json={
            'mutation': create_band_mutation
        },
        timeout=3.0
    )
    res_body = res.json()
    print(res_body)
    assert res.status_code == 200

def test_get_all_bands():
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

def test_filter_bands():
    res = requests.post(
        ENDPOINT,
        json={
            'query': filter_bands
        },
        timeout=3.0
    )
    res_body = res.json()
    print(res_body)
    assert res.status_code == 200 and res_body["data"]["filterBands"]["name"] == "The Ruts"

def test_delete_band_mutation():
    res = requests.post(
        ENDPOINT,
        json={
            'mutation':"""deleteBand(id: 4){
                band {
                    id
                }
            }
        """},
        timeout=3
    )
    assert res.status_code == 200

query_all_bands = """
    {
    allBands{
        id
        name
        }
    }
"""

filter_bands = """
    {
    filterBands(id:5){
        id
        name
        }
    }
"""

create_band_mutation = """
        {
        createBand(name:"The Ruts"){
            band{
                id
                name
            }
        }
    }
"""

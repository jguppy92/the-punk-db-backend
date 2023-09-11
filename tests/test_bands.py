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
from graphene.test import Client
from bands.schema import schema
# import conftest

client = Client(schema)

ENDPOINT = "http://localhost:8000/graphql"
# test_band_id = conftest["data"]["filterBands"]["id"]

def test_create_band():
    res = requests.post(
        ENDPOINT,
        json={
            'query': create_band_mutation
        },
        timeout=3.0
    )
    res_body = res.json()
    global test_band_id
    test_band_id = res_body["data"]["createBand"]["id"]
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
    assert res.status_code == 200 and res_body["data"]["filterBands"]["name"] == "The Damned"

def test_delete_band_mutation():
    res = requests.post(
        ENDPOINT,
        json={
            'query': delete_band_mutation
            },
        timeout=3
    )
    print(res.json())
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
    filterBands(id:{test_band_id}){
        id
        name
        }
    }
"""

create_band_mutation = """
        mutation {
            createBand(name:"The Damned"){
                band{
                    id
                    name
                }
            }
        }
    """

delete_band_mutation = """
            mutation {
                deleteBand(id:{test_band_id}){
                    band {
                        id
                    }
                }
            }
        """

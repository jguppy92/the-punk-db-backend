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
import conftest

ENDPOINT = "http://localhost:8000/graphql"

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
    filterBands(id:1){
        id
        name
        }
    }
"""

@pytest.fixture(scope="session")
def create_band_1():
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
    res = res = requests.post(
        ENDPOINT,
        json={
            'mutation': create_band_mutation
        }
    )
    res_body = res.json()
    return res_body

def test_get_all_bands(create_band_1):
    res = requests.post(
        ENDPOINT,
        json={
            'query': query_all_bands
        }
    )
    res_body = res.json()
    print(res_body)
    assert res.status_code == 200

def test_filter_bands(create_band_1):
    res = requests.post(
        ENDPOINT,
        json={
            'query': filter_bands
        }
    )
    res_body = res.json()
    print(res_body)
    assert res.status_code == 200 and res_body["data"]["filterBands"]["name"] == "The Clash"

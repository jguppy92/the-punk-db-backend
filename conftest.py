import pytest
import requests

ENDPOINT = "http://localhost:8000/graphql"

@pytest.fixture(scope="session")
def band_1():
    band = """
        mutation {
            createBand(name:"Black Flag"){
                band{
                    id
                    name
                }
            }
    }
    """
    res = requests.post(
        ENDPOINT,
        json={
            'query': band
        },
        timeout=3
    )
    print("create-band")
    res_body = res.json()
    print(res_body)
    return res_body

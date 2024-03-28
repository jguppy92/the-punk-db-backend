import pytest
import requests

ENDPOINT = "http://localhost:8000/graphql"

# @pytest.fixture()
# def band_1():
#     band = """
#         mutation {
#             createBand(name:"Black Flag"){
#                 band{
#                     id
#                     name
#                 }
#             }
#     }
#     """
#     res = requests.post(
#         ENDPOINT,
#         json={
#             'query': band
#         },
#         timeout=3
#     )
#     print("create-band")
#     res_body = res.json()
#     print(res_body)
#     return res_body


@pytest.fixture(scope="session")
def new_band_factory():
    def create_app_band(name: str):
        band = f"""
            mutation \u007b
                createBand(name:"{name}") \u007b
                    band \u007b
                        id
                        name
                    \u007d
                \u007d
            \u007d
        """
        res = requests.post(
            ENDPOINT,
            json={
                'query': band
            },
            timeout=3
        )
        res_body = res.json()
        print(f"create-band {name}")
        return res_body
    return create_app_band

@pytest.fixture(scope="module")
def new_band1(new_band_factory):
    return new_band_factory("Black Flag")

@pytest.fixture(scope="module")
def new_band2(new_band_factory):
    return new_band_factory("Rancid")

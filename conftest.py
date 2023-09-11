# import pytest
# import requests

# ENDPOINT = "http://localhost:8000/graphql"

# @pytest.fixture(scope="session")
# def create_band_1():
#     create_band_mutation = """
#         mutation {
#             createBand(name:"The Damned"){
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
#             'query': create_band_mutation
#         },
#         timeout=3
#     )
#     res_body = res.json()
#     return res_body

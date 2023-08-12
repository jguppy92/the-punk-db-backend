# import pytest
# import requests

# ENDPOINT = "http://localhost:8000/graphql"

# @pytest.fixture(scope="session")
# def create_band_1():
#     create_band_mutation = """
#         {
#             createBand(name:"The Ruts"){
#                 band{
#                     id
#                     name
#                 }
#             }
#     }
#     """
#     res = res = requests.post(
#         ENDPOINT,
#         json={
#             'mutation': create_band_mutation
#         }
#     )
#     res_body = res.json()
#     return res_body

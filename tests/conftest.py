import pytest
from client.tmdb_client import TMDBClient

@pytest.fixture
def tmdb():
    return TMDBClient()


@pytest.fixture
def temp_list(tmdb):
    response = tmdb.create_list("Test List", "A list to test my code.", "en")
    list_id = response.json()["list_id"]
    yield list_id
    tmdb.delete_list(list_id)

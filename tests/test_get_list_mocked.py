from unittest.mock import patch, MagicMock
from client.tmdb_client import TMDBClient


def test_get_list_mocked():
    # 1. Build a fake response object
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "iso_639_1": "en",
        "name": "Test List",
        "description": "A list to test my code.",
        "items": [],
    }

    # 2. Patch requests.get inside the client — while this block runs,
    #    any call to requests.get from tmdb_client returns our fake
    with patch("client.tmdb_client.requests.get", return_value=mock_response):
        tmdb = TMDBClient()
        response = tmdb.get_list("fake_id_doesnt_matter")

        # 3. Same assertions as your real test
        assert response.status_code == 200
        assert response.json()["iso_639_1"] == "en"
        assert "name" in response.json()
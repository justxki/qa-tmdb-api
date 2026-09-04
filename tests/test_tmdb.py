"""
Tests for TMDB

TMDB API quirks documented during testing:
- POST /list requires name, description, language keys in payload (missing → 400)
  but does NOT validate their values (empty string "" and null accepted → 200)
- POST /list/{id}/add_item accepts media_id as string OR int despite docs specifying int
- Delete list status_message wording differs from docs ("was deleted successfully"
  vs docs' "The item/record was deleted successfully")
"""

import json

def test_create_new_req_token(tmdb):
    response = tmdb.create_new_req_token()
    assert response.status_code == 200
    assert "request_token" in response.json()

def test_create_list(tmdb):
    response = tmdb.create_list("Test List", "A list to test my code.", "en")
    list_id = response.json()["list_id"]
    assert response.status_code == 201
    assert response.json()["success"] is True
    assert response.json()["list_id"] > 0

def test_create_list_no_lang(tmdb):
    response = tmdb.create_list("Test List Two", "A list to test my code.")
    list_id = response.json()["list_id"]
    assert response.status_code == 201
    assert response.json()["success"] is True
    assert response.json()["list_id"] > 0
    get_response = tmdb.get_list(list_id)
    assert get_response.json()["iso_639_1"] == "en"

def test_delete_list(tmdb):
    response = tmdb.create_list("Test List", "A list to test my code.", "en")
    list_id = response.json()["list_id"]
    assert response.status_code == 201
    response2 = tmdb.delete_list(list_id)
    assert response2.status_code == 200
    assert "deleted successfully" in response2.json()["status_message"]

def test_get_list(tmdb, temp_list):
    response = tmdb.get_list(temp_list)
    assert response.status_code == 200
    assert response.json()["iso_639_1"] == "en"
    assert "name" in response.json()

def test_add_movie_to_list(tmdb, temp_list):
    med_id = 550
    response = tmdb.add_movie_to_list(temp_list, med_id)
    assert response.status_code == 201
    assert "updated successfully" in response.json()["status_message"]

def test_remove_movie_from_list(tmdb, temp_list):
    med_id = 550
    add_response = tmdb.add_movie_to_list(temp_list, med_id)
    assert add_response.status_code == 201
    response = tmdb.remove_movie_from_list(temp_list, med_id)
    assert response.status_code == 200
    assert "deleted successfully" in response.json()["status_message"]

def test_get_nonexistent_list(tmdb):
    nonexistent_list = "My fake list"
    response = tmdb.get_list(nonexistent_list)
    assert response.status_code == 404
    assert "Invalid id" in response.json()["status_message"]
    assert response.json()["success"] == False

def test_v3_session_with_bad_request_token(tmdb):
    bad_req_token = "000000"
    response = tmdb.create_new_v3_session(bad_req_token)
    assert response.status_code == 401
    assert "Session denied" in response.json()["status_message"]
    assert response.json()["success"] == False


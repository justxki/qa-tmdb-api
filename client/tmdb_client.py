import requests
from config import (HEADERS, CONTENT_HEADERS, LIST_URI,
                    CREATE_REQ_TOKEN_URI, CREATE_V3_SESSION_URI)

class TMDBClient:
    def __init__(self):
        self.headers = HEADERS
        self.content_headers = CONTENT_HEADERS
        self.list_uri = LIST_URI
        self.create_req_token_uri = CREATE_REQ_TOKEN_URI
        self.create_v3_session_uri = CREATE_V3_SESSION_URI

    def create_new_req_token(self):
        response = requests.get(self.create_req_token_uri, headers=self.headers)
        return response

    def create_new_v3_session(self, req_token):
        payload = {"request_token": req_token}
        response = requests.post(self.create_v3_session_uri, headers=self.content_headers, json=payload)
        return response

    def create_list(self, name, descr, lang="en"):
        payload = {"name": name, "description": descr, "language": lang}
        response = requests.post(self.list_uri, headers=self.content_headers, json=payload)
        return response

    def delete_list(self, list_id):
        response = requests.delete(f"{self.list_uri}/{list_id}", headers=self.content_headers)
        return response

    def get_list(self, list_id):
        response = requests.get(f"{self.list_uri}/{list_id}", headers=self.headers)
        return response

    def add_movie_to_list(self, list_id, med_id):
        payload = {"media_id": med_id}
        response = requests.post(f"{self.list_uri}/{list_id}/add_item", headers=self.content_headers, json=payload)
        return response

    def remove_movie_from_list(self, list_id, med_id):
        payload = {"media_id": med_id}
        response = requests.post(f"{self.list_uri}/{list_id}/remove_item", headers=self.content_headers, json=payload)
        return response
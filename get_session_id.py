from client.tmdb_client import TMDBClient
import json
import os

print(f"Token loaded: {os.getenv('TMDB_TOKEN')[:20] if os.getenv('TMDB_TOKEN') else 'NONE'}...")

tmdb = TMDBClient()

token_response = tmdb.create_new_req_token()
print(f"Status: {token_response.status_code}")
req_token = token_response.json()["request_token"]

print(f"\nAPPROVE THIS TOKEN IN BROWSER:")
print(f"https://www.themoviedb.org/authenticate/{req_token}\n")

input("Press Enter after you've approved the token in browser...")

response = tmdb.create_new_v3_session(req_token)
print(json.dumps(response.json(), indent=2))
print(f"\nYOUR SESSION ID: {response.json()['session_id']}")
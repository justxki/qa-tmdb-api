from dotenv import load_dotenv
load_dotenv()
import os

BASE_URI = "https://api.themoviedb.org/3"
TMDB_TOKEN = os.getenv("TMDB_TOKEN")
TMDB_SESSION_ID = os.getenv("TMDB_SESSION_ID")
ACCOUNT_ID = "23652335"
HEADERS = {"accept": "application/json", "Authorization": f"Bearer {TMDB_TOKEN}"}
CONTENT_HEADERS = {"accept": "application/json", "content-type": "application/json",
    "Authorization": f"Bearer {TMDB_TOKEN}"}
CREATE_REQ_TOKEN_URI = "https://api.themoviedb.org/3/authentication/token/new"
CREATE_V3_SESSION_URI = "https://api.themoviedb.org/3/authentication/session/new"
LIST_URI = "https://api.themoviedb.org/3/list"
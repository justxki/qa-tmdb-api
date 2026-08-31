# qa-tmdb-api

QA automation suite for [TMDB's public API](https://developer.themoviedb.org/reference/intro/getting-started) using pytest and requests. Covers list CRUD operations, auth flow, and negative cases.

## Setup

#### 1. Clone the repo and cd into it:

git clone https://github.com/justxki/qa-tmdb-api.git
cd qa-tmdb-api


#### 2. Create and activate a virtual environment:

python -m venv .venv
.venv\Scripts\activate # windows
source .venv/bin/activate # mac/linux


#### 3. Install dependencies:

pip install -r requirements.txt


#### 4. Create a `.env` file in the project root with your TMDB credentials:

TMDB_TOKEN=your_v4_read_access_token_here
TMDB_SESSION_ID=your_session_id_here


   - Get your v4 Read Access Token from [TMDB API settings](https://www.themoviedb.org/settings/api).
   - To get your session_id, run `python get_session_id.py` — it will print a URL to approve in browser, then hand back a session_id to paste into `.env`.

## Running tests

From the project root:

pytest # run all tests
pytest -v # verbose output
pytest tests/test_tmdb.py::test_create_list # single test


## Project structure

```
qa-tmdb-api/
├── client/
│   └── tmdb_client.py       # TMDBClient — wraps requests to TMDB endpoints
├── tests/
│   ├── conftest.py          # shared fixtures (temp_list)
│   └── test_tmdb.py         # test suite
├── config.py                # env vars, headers, URIs
├── get_session_id.py        # one-time script to generate session_id
├── requirements.txt
└── .env                     # credentials (gitignored)
```

## Coverage

- Create a new request token
- Create a new list
- Create a new list without language provided
- Delete a list
- Get a list
- Add a movie to a list
- Remove a movie from a list
- Get a list that does not exist (negative)
- Use a bad request token for v3 session (negative)

## API quirks documented during testing

- `POST /list` requires `name`, `description`, `language` keys in payload (missing → 400), but does NOT validate their values (empty string `""` and `null` are accepted → 200).
- `POST /list/{id}/add_item` accepts `media_id` as string OR int despite docs specifying int.
- Delete list `status_message` wording differs from docs ("was deleted successfully" vs docs' "The item/record was deleted successfully").
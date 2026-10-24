# Final Project — Post API Client

A small, complete Python API client built with `requests`. It demonstrates API
communication, JSON processing, environment-based credential configuration,
status-code handling, typed errors, timeouts and rate-limit awareness, and
documents how the operation can later become an agent tool.

## Endpoint documentation

| Item | Value |
|---|---|
| Base URL | `https://jsonplaceholder.typicode.com` |
| Primary endpoint | `GET /posts/{post_id}` |
| Collection endpoint | `GET /posts` |
| Create endpoint | `POST /posts` |
| Update endpoint | `PUT /posts/{post_id}` |
| Delete endpoint | `DELETE /posts/{post_id}` |
| HTTP method (primary) | `GET` |
| Required parameters | `post_id` — integer path parameter (valid ids: 1–100) |
| Query parameters | none |
| Headers | `Accept: application/json`; `Authorization: Bearer <token>` only when `API_KEY` is configured |
| Request body (POST) | `{"title": "My API Lab", "body": "Testing POST request", "userId": 1}` |
| Response structure | `{"userId": 1, "id": 1, "title": "...", "body": "..."}` |
| Timeout | 10 seconds, configurable with `TIMEOUT` |

## Possible errors

| Status / failure | Meaning | Client behaviour |
|---|---|---|
| 200 / 201 / 204 | Success | Returns parsed JSON (or `None` for 204) |
| 400 | Bad request | Raises `APIError` with the status code |
| 401 / 403 | Authentication failed / forbidden | Raises `AuthError` |
| 404 | Resource does not exist | Raises `NotFoundError` |
| 429 | Rate limited | Waits (`Retry-After`) and retries up to `MAX_RETRIES`, then raises `RateLimitError` |
| 500–599 | Server failure | Raises `ServerError` |
| Timeout | Server did not answer in time | Raises `RequestTimeoutError` |
| Connection failure | Host unreachable / network down | Raises `NetworkError` |

The CLI catches `APIError` and reports the failure without a traceback, so the
program never crashes on an API failure.

## Setup

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env        # optional; the defaults work without .env
```

## Usage

Run from the `final_project` directory:

```bash
python -m src.main           # full demonstration (list, get, create, 404)
python -m src.main list      # collection: count + first five titles
python -m src.main post 1    # single post
python -m src.main create    # create a post
```

## Configuration

| Variable | Default | Purpose |
|---|---|---|
| `BASE_URL` | `https://jsonplaceholder.typicode.com` | API host |
| `TIMEOUT` | `10` | Request timeout in seconds |
| `MAX_RETRIES` | `2` | Retries when the API returns 429 |
| `API_KEY` | empty | Bearer token for protected APIs; sent as `Authorization: Bearer ...` |

Credentials are read from `.env` / environment variables and never appear in
source code, logs or output. `.env` is gitignored.

## How this operation could become an agent tool

The client already exposes Python methods with clear inputs and outputs, which
is most of a tool definition. Wrapping `get_post` with a name, a description, a
JSON schema for `post_id`, and structured errors gives an agent everything it
needs to select and call it:

```json
{
  "name": "get_post",
  "description": "Retrieve a blog post by its numeric id",
  "parameters": {"type": "object", "properties": {"post_id": {"type": "integer"}}, "required": ["post_id"]}
}
```

The runtime, not the model, would hold the API key. Errors such as
`NotFoundError`, `RateLimitError` and timeout are returned as observations the
agent can reason about (for example, stop retrying a 404 instead of looping).

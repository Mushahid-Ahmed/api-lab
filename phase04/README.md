# Phase 04 — Authentication & Secure Configuration

## Task 16 — Public vs Protected API

| Aspect | Public API | Protected API |
|---|---|---|
| Credentials required | No | Yes — an API key, bearer token, basic auth or OAuth flow |
| Why authentication is used | Not needed; the data is open | Identifies the caller, enforces quotas, protects private data, enables auditing |
| Example mechanism | None (JSONPlaceholder) | `Authorization: Bearer TOKEN` |
| What happens with invalid credentials | Not applicable | The server rejects the request with `401 Unauthorized` (or `403 Forbidden` when the caller is known but not allowed) |

## Task 17 — Authorization Header

`api_client.py` builds:

```python
headers = {"Authorization": f"Bearer {api_key}", "Accept": "application/json"}
```

The script prints the request configuration with the credential replaced by
`Bearer ***`, then calls `https://httpbin.org/bearer`, which accepts any bearer
token and returns `200`. No real credential is used anywhere in this lab.

## Task 18 — Credentials in .env

```text
API_KEY=your_key_here     # .env.example (committed)
API_KEY=<local value>     # .env (gitignored, never committed)
```

The program loads the key with `python-dotenv` and `os.getenv("API_KEY")`. The
key never appears in Python source code. `.env` is listed in both the top-level
`.gitignore` and `phase04/.gitignore`, and the lab evidence shows
`git check-ignore` confirming the file is excluded from version control.

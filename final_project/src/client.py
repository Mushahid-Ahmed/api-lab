"""JSONPlaceholder API client with typed errors and 429 retries."""

import time

import requests

from . import config
from .errors import (
    APIError,
    AuthError,
    NetworkError,
    NotFoundError,
    RateLimitError,
    RequestTimeoutError,
    ServerError,
)


class PostAPIClient:
    def __init__(self, base_url=None, timeout=None, api_key=None, max_retries=None):
        self.base_url = (base_url or config.BASE_URL).rstrip("/")
        self.timeout = timeout if timeout is not None else config.TIMEOUT
        self.max_retries = config.MAX_RETRIES if max_retries is None else max_retries
        self.session = requests.Session()
        self.session.headers.update({"Accept": "application/json"})
        api_key = api_key or config.API_KEY
        if api_key:
            self.session.headers["Authorization"] = f"Bearer {api_key}"

    def request(self, method, path, **kwargs):
        url = f"{self.base_url}{path}"
        for attempt in range(self.max_retries + 1):
            try:
                response = self.session.request(method, url, timeout=self.timeout, **kwargs)
            except requests.exceptions.Timeout as exc:
                raise RequestTimeoutError(
                    f"Request timed out after {self.timeout}s: {url}"
                ) from exc
            except requests.exceptions.ConnectionError as exc:
                raise NetworkError(f"Network failure while calling {url}") from exc
            except requests.exceptions.RequestException as exc:
                raise APIError(f"Request failed: {exc}") from exc

            if response.status_code == 429 and attempt < self.max_retries:
                time.sleep(float(response.headers.get("Retry-After", 1)))
                continue

            return self._handle(response)

        raise RateLimitError("Rate limit exceeded (HTTP 429)", status_code=429)

    def _handle(self, response):
        code = response.status_code
        if 200 <= code < 300:
            if code == 204 or not response.content:
                return None
            return response.json()
        if code == 404:
            raise NotFoundError(f"Resource not found: {response.url}", status_code=404)
        if code in (401, 403):
            raise AuthError(f"Authentication failed (HTTP {code}): {response.url}", status_code=code)
        if code == 429:
            raise RateLimitError("Rate limit exceeded (HTTP 429)", status_code=429)
        if 500 <= code < 600:
            raise ServerError(f"Server error (HTTP {code}): {response.url}", status_code=code)
        raise APIError(f"Request failed (HTTP {code}): {response.url}", status_code=code)

    def list_posts(self):
        return self.request("GET", "/posts")

    def get_post(self, post_id):
        return self.request("GET", f"/posts/{post_id}")

    def create_post(self, title, body, user_id=1):
        payload = {"title": title, "body": body, "userId": user_id}
        return self.request("POST", "/posts", json=payload)

    def update_post(self, post_id, title, body, user_id=1):
        payload = {"id": post_id, "title": title, "body": body, "userId": user_id}
        return self.request("PUT", f"/posts/{post_id}", json=payload)

    def delete_post(self, post_id):
        return self.request("DELETE", f"/posts/{post_id}")

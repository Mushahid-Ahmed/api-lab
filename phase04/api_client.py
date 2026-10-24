"""Phase 04 - Authorization header and credentials loaded from the environment."""

import os

import requests
from dotenv import load_dotenv

load_dotenv()

HTTPBIN = "https://httpbin.org"
TIMEOUT = 10


def build_headers(api_key):
    return {
        "Authorization": f"Bearer {api_key}",
        "Accept": "application/json",
    }


def main():
    api_key = os.getenv("API_KEY")

    print("Task 17 - build an Authorization header")
    print(f"API key loaded from environment: {'yes' if api_key else 'no'}")
    if not api_key:
        print("Set API_KEY in .env (copy .env.example) and run again.")
        return

    headers = build_headers(api_key)
    sanitized = {
        name: ("Bearer ***" if name == "Authorization" else value)
        for name, value in headers.items()
    }
    print(f"Request headers (sanitized): {sanitized}")

    print("\nTask 18 - send the header to a protected-style endpoint")
    response = requests.get(f"{HTTPBIN}/bearer", headers=headers, timeout=TIMEOUT)
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        print("Authenticated: yes, the server accepted the bearer token.")
    else:
        print("Authenticated: no, the server rejected the credentials.")
    print("The API key is loaded from .env and is never hardcoded or printed.")


if __name__ == "__main__":
    main()

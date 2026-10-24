"""Final project - complete API client demonstration.

Run from the final_project directory:

    python -m src.main           # full demonstration
    python -m src.main list      # first five posts
    python -m src.main post 1    # one post
    python -m src.main create    # POST a new post
"""

import argparse

from . import config
from .client import PostAPIClient
from .errors import APIError


def show_post(post):
    print(f"Post ID : {post['id']}")
    print(f"Title   : {post['title']}")
    print(f"Body    : {post['body']}")
    print(f"User ID : {post['userId']}")


def run_demo(client):
    print("== 1. Connection and configuration ==")
    print(f"Base URL: {client.base_url}")
    print(f"Timeout : {client.timeout}s (configurable via .env)")
    key_state = "configured (loaded from environment)" if config.API_KEY else "not required for this public API"
    print(f"API key : {key_state}")
    print(f"Retries on 429: {client.max_retries}")

    print("\n== 2. Retrieve a collection ==")
    posts = client.list_posts()
    print(f"Posts returned: {len(posts)}")
    print("First five titles:")
    for post in posts[:5]:
        print(f"  - {post['title']}")

    print("\n== 3. Retrieve one resource ==")
    show_post(client.get_post(1))

    print("\n== 4. Create a resource (POST) ==")
    created = client.create_post("My API Lab", "Testing POST request", user_id=1)
    print(f"Created post id: {created['id']} (HTTP 201)")
    print(f"Title: {created['title']}")

    print("\n== 5. Error handling ==")
    try:
        client.get_post(99999)
    except APIError as error:
        print(f"Handled {type(error).__name__}: HTTP {error.status_code}")
        print(f"Message: {error}")

    print("\nDemo finished. All failures were handled as typed errors.")


def main():
    parser = argparse.ArgumentParser(description="JSONPlaceholder API client")
    parser.add_argument(
        "command",
        nargs="?",
        default="demo",
        choices=["demo", "list", "post", "create"],
        help="operation to run (default: demo)",
    )
    parser.add_argument("post_id", nargs="?", type=int, default=1, help="post id for the post command")
    args = parser.parse_args()

    client = PostAPIClient()
    try:
        if args.command == "demo":
            run_demo(client)
        elif args.command == "list":
            posts = client.list_posts()
            print(f"Posts returned: {len(posts)}")
            for post in posts[:5]:
                print(f"  - {post['id']}: {post['title']}")
        elif args.command == "post":
            show_post(client.get_post(args.post_id))
        elif args.command == "create":
            created = client.create_post("My API Lab", "Testing POST request", user_id=1)
            print(f"Created post id: {created['id']} (HTTP 201)")
    except APIError as error:
        print(f"Request failed: {type(error).__name__} (HTTP {error.status_code})")
        print(error)


if __name__ == "__main__":
    main()

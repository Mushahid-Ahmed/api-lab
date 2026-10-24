"""Phase 03 - First Python API client for JSONPlaceholder."""

import requests

BASE_URL = "https://jsonplaceholder.typicode.com"
TIMEOUT = 15


def get_post(post_id):
    response = requests.get(f"{BASE_URL}/posts/{post_id}", timeout=TIMEOUT)
    if response.status_code != 200:
        print(f"Request failed. Status: {response.status_code}")
        return None
    return response.json()


def main():
    print("Task 13 - single post")
    post = get_post(1)
    print(f"Status: 200")
    print(f"Post ID: {post['id']}")
    print(f"Title: {post['title']}")
    print(f"Body: {post['body']}")

    print("\nTask 14 - retrieve multiple posts with a loop")
    for post_id in (1, 2, 3):
        post = get_post(post_id)
        print(f"Post {post_id}: {post['title']}")

    print("\nTask 15 - retrieve and process a collection")
    response = requests.get(f"{BASE_URL}/posts", timeout=TIMEOUT)
    print(f"Status: {response.status_code}")
    posts = response.json()
    print(f"Number of posts returned: {len(posts)}")
    print("First five post titles:")
    for post in posts[:5]:
        print(f"  - {post['title']}")


if __name__ == "__main__":
    main()

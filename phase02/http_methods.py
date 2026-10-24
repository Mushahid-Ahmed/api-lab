"""Phase 02 - HTTP methods and status codes against JSONPlaceholder."""

import argparse
import json

import requests

BASE_URL = "https://jsonplaceholder.typicode.com"
TIMEOUT = 15

POST_BODY = {
    "title": "My API Lab",
    "body": "Testing POST request",
    "userId": 1,
}

PUT_BODY = {
    "id": 1,
    "title": "My API Lab (updated)",
    "body": "Testing PUT request",
    "userId": 1,
}


def describe(response):
    print(f"HTTP method : {response.request.method}")
    print(f"Endpoint    : {response.url}")
    print(f"Status code : {response.status_code}")
    print(f"Response    : {response.text.strip()[:500]}")


def task_06():
    print("Task 06 - GET /posts/1, /posts/2, /posts/3")
    for post_id in (1, 2, 3):
        response = requests.get(f"{BASE_URL}/posts/{post_id}", timeout=TIMEOUT)
        data = response.json()
        print(f"\nGET /posts/{post_id}")
        print(f"  Status code : {response.status_code}")
        print(f"  Post id     : {data['id']}")
        print(f"  Title       : {data['title'][:60]}")


def task_07():
    print("Task 07 - POST /posts")
    print(f"Request body: {json.dumps(POST_BODY)}")
    response = requests.post(f"{BASE_URL}/posts", json=POST_BODY, timeout=TIMEOUT)
    describe(response)


def task_08():
    print("Task 08 - PUT /posts/1")
    print(f"Request body: {json.dumps(PUT_BODY)}")
    response = requests.put(f"{BASE_URL}/posts/1", json=PUT_BODY, timeout=TIMEOUT)
    describe(response)


def task_09():
    print("Task 09 - DELETE /posts/1")
    response = requests.delete(f"{BASE_URL}/posts/1", timeout=TIMEOUT)
    print(f"HTTP method : {response.request.method}")
    print(f"Endpoint    : {response.url}")
    print(f"Status code : {response.status_code}")
    print(f"Response    : {response.text.strip() or '(empty body)'}")
    print("DELETE asks the server to remove the addressed resource.")


def task_10():
    print("Task 10 - Observe status codes 200, 201 and 404")
    get_response = requests.get(f"{BASE_URL}/posts/1", timeout=TIMEOUT)
    print(f"200 -> GET /posts/1 returned {get_response.status_code}: the post exists")
    post_response = requests.post(f"{BASE_URL}/posts", json=POST_BODY, timeout=TIMEOUT)
    print(f"201 -> POST /posts returned {post_response.status_code}: a post was created")
    missing = requests.get(f"{BASE_URL}/posts/99999", timeout=TIMEOUT)
    print(f"404 -> GET /posts/99999 returned {missing.status_code}: no resource with that id")
    print()
    print("200 and 201 are 2xx success codes. 404 is a 4xx client error:")
    print("the server responded correctly, but the requested resource does not exist.")


TASKS = {
    "06": task_06,
    "07": task_07,
    "08": task_08,
    "09": task_09,
    "10": task_10,
}


def main():
    parser = argparse.ArgumentParser(description="Phase 02 HTTP method demonstrations")
    parser.add_argument("--task", choices=sorted(TASKS), help="run a single task")
    args = parser.parse_args()

    selected = [args.task] if args.task else sorted(TASKS)
    for task in selected:
        print("=" * 60)
        TASKS[task]()
        print()


if __name__ == "__main__":
    main()

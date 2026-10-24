"""Phase 05 - HTTP errors, timeouts and rate-limit awareness."""

import argparse

import requests

BASE_URL = "https://jsonplaceholder.typicode.com"
HTTPBIN = "https://httpbin.org"
TIMEOUT = 5

STATUS_MESSAGES = {
    200: "Success. The request completed and the response contains the resource.",
    201: "Created. A new resource was created.",
    400: "Bad request. The server could not understand the request.",
    401: "Unauthorized. Valid credentials are required.",
    403: "Forbidden. The credentials are valid but access is not allowed.",
    404: "Resource not found.",
    429: "Too many requests. The client is being rate limited.",
    500: "Server error. The server failed to complete the request.",
}


def message_for(status_code):
    if status_code in STATUS_MESSAGES:
        return STATUS_MESSAGES[status_code]
    if 200 <= status_code < 300:
        return "Success."
    if 400 <= status_code < 500:
        return "Client error."
    if 500 <= status_code < 600:
        return "Server error."
    return "Unexpected status."


def task_19():
    print("Task 19 - handle a 404 for a resource that does not exist")
    response = requests.get(f"{BASE_URL}/posts/99999", timeout=TIMEOUT)
    print(f"GET {response.url}")
    if response.status_code == 404:
        print("Request failed.")
        print(f"Status Code: {response.status_code}")
        print("Resource not found.")
    else:
        print(f"Unexpected status: {response.status_code}")
    print("The program handled the missing resource without an unhandled exception.")


def task_20():
    print("Task 20 - distinguish HTTP status categories")
    cases = [
        (f"{HTTPBIN}/get", "success"),
        (f"{HTTPBIN}/status/400", "invalid request"),
        (f"{HTTPBIN}/status/401", "unauthorized"),
        (f"{HTTPBIN}/status/403", "forbidden"),
        (f"{BASE_URL}/posts/99999", "missing resource"),
        (f"{HTTPBIN}/status/429", "rate limited"),
        (f"{HTTPBIN}/status/500", "server failure"),
    ]
    for url, label in cases:
        response = requests.get(url, timeout=10)
        print(f"{response.status_code:>3}  {label:<16} {message_for(response.status_code)}")


def task_21():
    print("Task 21 - request timeout")
    print("Requesting https://httpbin.org/delay/10 with timeout=2 ...")
    try:
        requests.get(f"{HTTPBIN}/delay/10", timeout=2)
        print("Unexpected: the request completed within 2 seconds.")
    except requests.exceptions.Timeout:
        print("Timed out after 2 seconds. requests raised requests.exceptions.Timeout.")
        print("A timeout prevents the program from waiting indefinitely for a response.")


def task_22():
    print("Task 22 - distinguish the four outcomes")

    response = requests.get(f"{BASE_URL}/posts/1", timeout=TIMEOUT)
    print(f"Success            : status {response.status_code}, post title received")

    response = requests.get(f"{BASE_URL}/posts/99999", timeout=TIMEOUT)
    print(f"API error          : status {response.status_code}, {message_for(response.status_code)}")

    try:
        requests.get(f"{HTTPBIN}/delay/10", timeout=2)
        print("Timeout            : not triggered")
    except requests.exceptions.Timeout:
        print("Timeout            : requests.exceptions.Timeout after 2 seconds")

    try:
        requests.get("http://127.0.0.1:9/", timeout=3)
        print("Network failure    : unexpected success")
    except requests.exceptions.ConnectionError:
        print("Network failure    : requests.exceptions.ConnectionError (host unreachable)")


TASKS = {
    "19": task_19,
    "20": task_20,
    "21": task_21,
    "22": task_22,
}


def main():
    parser = argparse.ArgumentParser(description="Phase 05 error-handling demonstrations")
    parser.add_argument("--task", choices=sorted(TASKS), help="run a single task")
    args = parser.parse_args()

    selected = [args.task] if args.task else sorted(TASKS)
    for task in selected:
        print("=" * 60)
        TASKS[task]()
        print()


if __name__ == "__main__":
    main()

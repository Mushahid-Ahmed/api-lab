# Phase 02 — HTTP Requests, Responses & REST

## Task 04 — Analyze a URL

URL: `https://api.example.com/students/101`

| Part | Value | Meaning |
|---|---|---|
| Protocol | `https` | HTTP over TLS; the request/response is encrypted |
| Host | `api.example.com` | The server (domain) that receives the request |
| Path | `/students/101` | The resource being addressed |
| Resource | `students` | The collection of student records |
| Resource identifier | `101` | The specific student inside that collection |

## Task 05 — REST API Operation Table

| Operation | HTTP Method | Endpoint |
|---|---|---|
| Retrieve all students | GET | `/students` |
| Create a student | POST | `/students` |
| Retrieve student 101 | GET | `/students/101` |
| Update student 101 | PUT | `/students/101` |
| Delete student 101 | DELETE | `/students/101` |

Different HTTP methods are used because each describes a different intent on the
same resource. The URL identifies *what* is being operated on; the method states
*what operation* is being requested. `GET` must not change data, `POST` creates a
new record in a collection, `PUT` replaces an existing record, and `DELETE`
removes it. Using the method correctly lets servers, proxies and clients apply
the right rules (for example GET is safe, and PUT and DELETE are idempotent).

## Task 10 — HTTP Status Codes

| Status Code | Meaning | Your test |
|---|---|---|
| 200 | OK — request succeeded and the response contains the resource | `GET /posts/1` (Task 06) |
| 201 | Created — a new resource was created | `POST /posts` with the lab body (Task 07) |
| 404 | Not Found — the server responded, but the resource does not exist | `GET /posts/99999` |

A successful request (2xx) means the server understood the request and performed
it. A 404 is also a valid HTTP response — the server worked correctly and told
the client that the requested resource does not exist, which is why receiving a
response is not the same as the operation succeeding.

## Scripts

`http_methods.py` performs all requests and prints method, URL, status code and
response body. Run a single task with `--task NN`:

```bash
python phase02/http_methods.py            # tasks 06-10
python phase02/http_methods.py --task 07  # POST only
```

Evidence: `evidence/task06.png` … `evidence/task10.png`.

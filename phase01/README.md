# Phase 01 — API & Client-Server Fundamentals

## Task 01 — Explore an API Using a Browser

Endpoint: `https://jsonplaceholder.typicode.com/posts/1`

The browser shows a JSON object. Changing the last part of the path to `/2` and
`/3` returns a different post with the same structure.

| Field | /posts/1 | /posts/2 | /posts/3 |
|---|---|---|---|
| userId | 1 | 1 | 1 |
| id | 1 | 2 | 3 |
| title | sunt aut facere repellat provident occaecati excepturi optio reprehenderit | qui est esse | ea molestias quasi exercitationem repellat qui ipsa sit aut |
| body | quia et suscipit ... | est rerum tempore vitae ... | et iusto sed quo iure ... |

Screenshots: `evidence/task01.png`, `evidence/task01-b.png`, `evidence/task01-c.png`.

### Why does the response change for /1, /2 and /3?

The path segment after `/posts/` is the resource identifier. The server looks up
the post whose `id` matches that number and returns only that record. `/1`
returns post 1, `/2` returns post 2, and `/3` returns post 3. The JSON structure
is identical, but the values belong to different resources. A request for an id
that does not exist (for example `/posts/99999`) returns `404 Not Found` instead
of a post.

## Task 02 — Identify the Client, API and Server

```text
   Browser (client)                     API server
  ┌────────────────┐   GET /posts/1   ┌──────────────────────────┐
  │  Address bar   │ ───────────────► │ JSONPlaceholder API      │
  │  (Chrome)      │                  │  (routes + data + logic) │
  └────────────────┘ ◄─────────────── └──────────────────────────┘
         ▲             200 OK + JSON              │
         │                                        │
         └────────── response rendered ───────────┘
```

1. The browser is the client. It builds an HTTP request for the URL in the
   address bar: method `GET`, host `jsonplaceholder.typicode.com`, path
   `/posts/1`.
2. The request travels over HTTPS to the API server. The server receives the
   request, reads the path and determines that the client wants the post whose
   id is 1.
3. The server finds the record in its data store, serializes it as JSON and
   sends back an HTTP response with status `200 OK` and the JSON body.
4. The browser receives the response, checks the status code and content type,
   and displays the JSON. The client never needed to know how the server stores
   or finds the data; it only used the API contract.

Diagram image: `evidence/task02.png`.

## Task 03 — Identify API Resources

| Endpoint | Resource | Specific resource? |
|---|---|---|
| `/posts` | The collection of all posts (100 records) | No — returns the whole collection |
| `/posts/1` | The single post with id 1 | Yes — one record |
| `/posts/2` | The single post with id 2 | Yes — one record |

`/posts` is a collection endpoint. Adding an identifier (`/posts/{id}`) selects
one item out of that collection.

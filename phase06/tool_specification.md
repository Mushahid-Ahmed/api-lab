# Phase 06 — From API Integration to Agent Tools

## Task 24 — API Tool Specification

**Tool Name:** `get_post`

**Description:** Retrieve a single blog post by its numeric identifier from the
JSONPlaceholder public API.

**HTTP Method:** `GET`

**Endpoint:** `https://jsonplaceholder.typicode.com/posts/{post_id}`

**Required Inputs:**

| Input | Type | Description |
|---|---|---|
| `post_id` | integer | Identifier of the post to retrieve (1-100 exist) |

**Optional Inputs:** none (the client applies a fixed request timeout)

**Expected Output:** a JSON object with the fields `userId`, `id`, `title`,
`body`.

**Possible Errors:**

| Error | Meaning | Tool response |
|---|---|---|
| `404` | No post with that id | Report that the resource was not found |
| `429` | Rate limited | Wait and retry later |
| `500` | Server failure | Report a temporary service error |
| Timeout | Server did not answer in time | Report a timeout and suggest retrying |
| Network failure | Host unreachable | Report a connection problem |

**Authentication Required:** No. JSONPlaceholder is a public API. If this tool
targeted a protected API, the credential would come from an environment
variable and would never appear in the tool arguments or logs.

## Task 25 — Agent-Oriented Tool Interface

```yaml
tool:
  name: get_post
  purpose: Retrieve a post using its ID.
  input:
    post_id: integer   # required
  output:
    id: integer
    title: string
    body: string
    userId: integer
  possible_errors: [404, 429, 500, Timeout, NetworkError]
```

In an agent loop the flow would be: the model decides it needs post 1, selects
the `get_post` tool, fills `post_id=1`, the runtime performs the HTTP request and
returns the JSON object or a structured error, and the agent continues from the
observation.

### Why authentication and error handling still matter when an API becomes a tool

A tool is still an HTTP call, so all the failure modes remain: rejected
credentials, missing resources, rate limits, timeouts and server errors. An
agent cannot see a stack trace, so each failure must be returned as structured,
readable information the model can reason about. If a rate-limit error looks the
same as a missing record, the agent may retry forever or invent data.

Credentials must stay outside the tool interface. The model should never receive
or produce the API key; the runtime attaches the header from environment
configuration, the same way `phase04` does. This keeps secrets out of prompts,
logs and conversation history.

# Phase 05 — Errors, Timeouts & Rate Limits

## Task 23 — Rate Limiting

**What is a rate limit?**
A rate limit is a cap on how many requests a client may send in a time window
(for example 60 requests per minute). Requests beyond the cap are rejected,
usually with HTTP `429 Too Many Requests`.

**Why do APIs impose rate limits?**
To keep the service available for everyone: they protect servers from overload,
prevent abuse and scraping, guarantee fair usage across clients, and control
infrastructure cost.

**What does HTTP 429 mean?**
`429 Too Many Requests` is a 4xx client error: the request was well formed and
the client was authenticated (if required), but it exceeded the allowed request
rate. It is temporary — the client should wait and retry, respecting a
`Retry-After` header when the server sends one.

**Why can an automated program generate too many requests?**
A loop, a polling job or a retry policy can send hundreds of requests per second
without any human involvement. A bug such as retrying immediately on failure, or
polling in a tight loop, multiplies the request count far beyond what a person
would produce.

**Why is this especially important for agentic systems?**
An agent runs its own loop: it decides, calls tools, observes results and may
retry automatically. A single task can trigger dozens of API calls, and several
agents or retries multiply that further. Without rate-limit awareness an agent
can exhaust quotas, incur unexpected cost, trigger bans, or enter a retry storm.
That is why production agents implement backoff, respect `Retry-After`, cache
results, and enforce call budgets.

## Demonstrations

`api_client.py` shows a 404 (Task 19), a table of 200/400/401/403/404/429/500
responses (Task 20), a real timeout against `httpbin.org/delay/10` (Task 21),
and the four outcomes success / API error / timeout / network failure (Task 22).
Evidence: `evidence/task19.png` … `evidence/task22.png`.

The final project also retries once on `429` while respecting `Retry-After`, so
rate limiting is considered in automated code rather than only described.

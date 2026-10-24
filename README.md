# API Lab — Week 02

A small API lab for the Agentic AI Systems Engineering course. It progresses
from browser exploration of a public API to a complete, error-resistant Python
API client that is documented as a future agent tool.

All requests target [JSONPlaceholder](https://jsonplaceholder.typicode.com), a
free fake REST API, and [httpbin.org](https://httpbin.org) for authentication,
status-code and timeout demonstrations. No real credentials are used.

## Structure

```text
API-Lab/
├── phase01/                  # API & client-server fundamentals
│   └── README.md             # Browser exploration, diagram, resources
├── phase02/                  # HTTP, REST, status codes
│   ├── rest_operations.md    # URL analysis, REST operation table
│   └── http_methods.py       # GET / POST / PUT / DELETE runs
├── phase03/                  # JSON & first Python API client
│   ├── json_basics.py
│   └── api_client.py
├── phase04/                  # Authentication & secure configuration
│   ├── api_client.py
│   ├── README.md
│   ├── .env.example
│   └── .gitignore
├── phase05/                  # Errors, timeouts, rate limits
│   ├── api_client.py
│   └── README.md
├── phase06/                  # API as an agent tool
│   └── tool_specification.md
├── final_project/            # Complete API client application
│   ├── src/
│   ├── README.md
│   └── requirements.txt
└── evidence/                 # Screenshots and terminal logs
```

## Setup

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
pip install -r final_project/requirements.txt
```

## Run

```bash
python phase02/http_methods.py              # all HTTP method tasks
python phase03/json_basics.py
python phase03/api_client.py
python phase04/api_client.py
python phase05/api_client.py
python -m src.main                          # final project (run from final_project/)
```

Phase scripts accept `--task NN` to run a single task, for example
`python phase02/http_methods.py --task 07`.

## Documentation

- [Phase 01 notes](phase01/README.md)
- [Phase 02 REST analysis](phase02/rest_operations.md)
- [Phase 04 authentication notes](phase04/README.md)
- [Phase 05 error handling notes](phase05/README.md)
- [Phase 06 tool specification](phase06/tool_specification.md)
- [Final project documentation](final_project/README.md)

## Agentic AI connection

Every API operation used here is described with a name, inputs, output and
possible errors. That is exactly the information an agent needs to select and
call a tool. Phase 06 turns the `get_post` operation into a tool specification,
and the final project shows how the same operation would be exposed to an agent
in a later week.

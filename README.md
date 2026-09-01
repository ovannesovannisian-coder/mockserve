# MockServe

**Zero-dependency JSON-configured API mock server for testing and development.**

[![Python 3.9+](https://img.shields.io/pypi/pyversions/mockserve)](https://pypi.org/project/mockserve/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)

No dependencies — only Python stdlib. Define your API mocks in JSON and run them instantly.

## Install

```bash
pip install mockserve
```

Or from source:

```bash
git clone https://github.com/ovannesovannisian-coder/mockserve.git
cd mockserve
python -m src.cli examples/config.json --port 8080
```

## Quick Start

```bash
# Start a mock server from config
mockserve config.json --port 8080

# Your API is now running at http://localhost:8080
curl http://localhost:8080/api/users
```

## JSON Config

```json
{
  "port": 8080,
  "routes": {
    "/api/users": {
      "method": "GET",
      "response": {
        "status": 200,
        "body": {"users": [{"id": 1, "name": "John"}]}
      }
    },
    "/api/users": {
      "method": "POST",
      "response": {
        "status": 201,
        "body": {"message": "User created"}
      }
    }
  }
}
```

## Features

- **JSON configuration** — define routes and responses in JSON
- **Zero dependencies** — pure stdlib, no external packages
- **Fast startup** — ready in milliseconds
- **CORS support** — built-in CORS headers for frontend testing
- **Logging** — request/response logging for debugging

## Use Cases

- Frontend development without backend
- API contract testing
- Integration test environments
- Prototyping and demos

## License

MIT — use it commercially, modify it, ship it in your products.

---

**Need a custom API mock setup?** [Open a request](https://github.com/ovannesovannisian-coder/ovannesovannisian-coder.github.io/issues) and get a fixed USDT quote within 24h.

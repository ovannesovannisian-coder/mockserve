# MockServe

Lightweight API mock server from JSON files. Pure Python standard library.

## Quick Start

```bash
python -m src.cli examples/config.json --port 8080
```

Then hit `http://localhost:8080/api/users` in your browser or frontend app.

## Config Format

```json
{
  "routes": {
    "GET:/api/users": {
      "status": 200,
      "body": [{"id": 1, "name": "Alice"}]
    }
  }
}
```

## License

MIT

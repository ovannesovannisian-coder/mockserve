"""MockServe — lightweight API mock server from JSON files. Pure Python stdlib."""

import json
import threading
import http.server
import socketserver
import urllib.parse
from pathlib import Path
from typing import Dict, Optional


class MockHandler(http.server.BaseHTTPRequestHandler):
    """HTTP request handler that serves mocked responses from JSON config."""

    routes: Dict[str, Dict] = {}
    default_response = {"status": 404, "body": {"error": "Not Found"}, "headers": {"Content-Type": "application/json"}}

    def log_message(self, format, *args):
        pass  # Suppress default logging

    def _match_route(self, path: str, method: str):
        key = f"{method}:{path}"
        if key in self.routes:
            return self.routes[key]
        # Try prefix matching
        for route_key, route in self.routes.items():
            rmethod, rpath = route_key.split(":", 1)
            if rmethod == method and path.startswith(rpath):
                return route
        return None

    def _send_response(self, route: Dict):
        status = route.get("status", 200)
        body = route.get("body", {})
        headers = route.get("headers", {"Content-Type": "application/json"})
        delay = route.get("delay", 0)

        if delay:
            import time
            time.sleep(delay)

        body_text = json.dumps(body, ensure_ascii=False, indent=2) if not isinstance(body, str) else body
        self.send_response(status)
        for k, v in headers.items():
            self.send_header(k, v)
        self.send_header("Content-Length", str(len(body_text.encode("utf-8"))))
        self.end_headers()
        self.wfile.write(body_text.encode("utf-8"))

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        route = self._match_route(parsed.path, "GET")
        if route:
            self._send_response(route)
        else:
            self._send_response(self.default_response)

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        route = self._match_route(parsed.path, "POST")
        if route:
            self._send_response(route)
        else:
            self._send_response(self.default_response)

    def do_PUT(self):
        parsed = urllib.parse.urlparse(self.path)
        route = self._match_route(parsed.path, "PUT")
        if route:
            self._send_response(route)
        else:
            self._send_response(self.default_response)

    def do_DELETE(self):
        parsed = urllib.parse.urlparse(self.path)
        route = self._match_route(parsed.path, "DELETE")
        if route:
            self._send_response(route)
        else:
            self._send_response(self.default_response)


class MockServer:
    def __init__(self, config_path: str, port: int = 8080):
        with open(config_path, encoding="utf-8") as f:
            config = json.load(f)
        MockHandler.routes = config.get("routes", {})
        MockHandler.default_response = config.get("default", MockHandler.default_response)
        self.port = port
        self.server = socketserver.TCPServer(("", port), MockHandler)
        self.thread: Optional[threading.Thread] = None

    def start(self):
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()
        print(f"Mock server running on http://localhost:{self.port}")

    def stop(self):
        self.server.shutdown()
        print("Mock server stopped")

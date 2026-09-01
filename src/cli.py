#!/usr/bin/env python3
"""MockServe CLI entry point."""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from mockserve import MockServer


def main():
    parser = argparse.ArgumentParser(description="MockServe — mock API server from JSON config")
    parser.add_argument("config", help="Path to JSON config file")
    parser.add_argument("--port", type=int, default=8080)
    args = parser.parse_args()

    server = MockServer(args.config, port=args.port)
    server.start()
    try:
        while True:
            pass
    except KeyboardInterrupt:
        server.stop()


if __name__ == "__main__":
    main()

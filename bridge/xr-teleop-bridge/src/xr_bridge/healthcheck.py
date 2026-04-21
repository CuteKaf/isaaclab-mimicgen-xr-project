"""Connectivity checks for Ubuntu A -> Ubuntu B."""

from __future__ import annotations

import argparse
import asyncio
import os

from .transport import ping_server


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check Ubuntu B WebSocket reachability.")
    parser.add_argument(
        "--server",
        default=os.environ.get("XR_BRIDGE_SERVER", "ws://127.0.0.1:8765/xr"),
        help="Ubuntu B WebSocket URL.",
    )
    parser.add_argument("--timeout", type=float, default=3.0, help="Connection timeout in seconds.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    try:
        asyncio.run(ping_server(args.server, timeout=args.timeout))
    except Exception as exc:
        raise SystemExit(f"FAILED: cannot connect to {args.server}: {exc}") from exc
    print(f"OK: connected to {args.server}")


if __name__ == "__main__":
    main()


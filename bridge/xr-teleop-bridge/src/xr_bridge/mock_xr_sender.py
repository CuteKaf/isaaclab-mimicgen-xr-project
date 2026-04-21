"""Mock XR sender used before real PICO / XRoboToolkit input is available."""

from __future__ import annotations

import argparse
import asyncio
import logging
import os

from .schema import make_mock_frame
from .transport import send_json_frames


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Send mock XR frames to Ubuntu B.")
    parser.add_argument(
        "--server",
        default=os.environ.get("XR_BRIDGE_SERVER", "ws://127.0.0.1:8765/xr"),
        help="Ubuntu B WebSocket URL.",
    )
    parser.add_argument("--hz", type=float, default=60.0, help="Send rate in Hz.")
    parser.add_argument("--log-level", default="INFO", help="Python logging level.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    logging.basicConfig(level=getattr(logging, args.log_level.upper()), format="%(asctime)s %(levelname)s %(message)s")
    asyncio.run(send_json_frames(args.server, lambda frame_id: make_mock_frame(frame_id).to_dict(), hz=args.hz))


if __name__ == "__main__":
    main()


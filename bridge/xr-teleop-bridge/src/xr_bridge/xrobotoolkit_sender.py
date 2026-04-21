"""XRoboToolkit sender placeholder.

Ubuntu A should replace `read_xrobotoolkit_frame` with the real local
XRoboToolkit / Teleop Sample integration once the exact Python bindings or
sample output format are available on that machine.
"""

from __future__ import annotations

import argparse
import asyncio
import logging
import os

from .transport import send_json_frames


def read_xrobotoolkit_frame(frame_id: int) -> dict:
    """Read one real XR frame.

    This is intentionally not implemented in the coordination repository. The
    Ubuntu A Codex should inspect the local XRoboToolkit installation and wire
    this function to the actual API.
    """
    raise RuntimeError(
        "XRoboToolkit input is not wired yet. Use scripts/run_mock_sender.py for network tests first."
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Send real XRoboToolkit frames to Ubuntu B.")
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
    asyncio.run(send_json_frames(args.server, read_xrobotoolkit_frame, hz=args.hz))


if __name__ == "__main__":
    main()


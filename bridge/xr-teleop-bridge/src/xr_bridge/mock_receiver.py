"""Mock WebSocket receiver for Ubuntu A sender tests."""

from __future__ import annotations

import argparse
import asyncio
import json
import time

import websockets

from .schema import validate_frame


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Receive and print XR frames.")
    parser.add_argument("--host", default="0.0.0.0", help="Bind host.")
    parser.add_argument("--port", type=int, default=8765, help="Bind port.")
    parser.add_argument("--print-every", type=int, default=30, help="Print every N frames.")
    return parser.parse_args()


async def handle_client(websocket):
    count = 0
    start = time.time()
    async for message in websocket:
        frame = json.loads(message)
        validate_frame(frame)
        count += 1
        if count == 1 or count % ARGS.print_every == 0:
            elapsed = max(time.time() - start, 1e-6)
            right = frame["right_controller_pose"]["position"]
            buttons = frame["buttons"]
            print(
                f"frames={count} rate={count / elapsed:.1f}Hz "
                f"frame_id={frame['frame_id']} right_pos={right} "
                f"right_grip={buttons.get('right_grip')} right_trigger={buttons.get('right_trigger')}",
                flush=True,
            )


async def run_server() -> None:
    async with websockets.serve(handle_client, ARGS.host, ARGS.port):
        print(f"listening on ws://{ARGS.host}:{ARGS.port}/xr", flush=True)
        await asyncio.Future()


ARGS = parse_args()


def main() -> None:
    asyncio.run(run_server())


if __name__ == "__main__":
    main()


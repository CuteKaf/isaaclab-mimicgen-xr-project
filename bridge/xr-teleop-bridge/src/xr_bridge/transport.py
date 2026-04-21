"""WebSocket transport helpers."""

from __future__ import annotations

import asyncio
import json
import logging
from collections.abc import Callable
from typing import Any

import websockets

LOGGER = logging.getLogger(__name__)


async def send_json_frames(
    server: str,
    frame_factory: Callable[[int], dict[str, Any]],
    hz: float = 60.0,
    reconnect_delay: float = 1.0,
) -> None:
    """Continuously send JSON frames to a WebSocket server."""
    if hz <= 0:
        raise ValueError("hz must be positive")

    frame_id = 0
    period = 1.0 / hz
    while True:
        try:
            async with websockets.connect(server) as websocket:
                LOGGER.info("connected to %s", server)
                while True:
                    frame = frame_factory(frame_id)
                    await websocket.send(json.dumps(frame, separators=(",", ":")))
                    frame_id += 1
                    await asyncio.sleep(period)
        except (OSError, websockets.WebSocketException) as exc:
            LOGGER.warning("connection lost: %s; retrying in %.1fs", exc, reconnect_delay)
            await asyncio.sleep(reconnect_delay)


async def ping_server(server: str, timeout: float = 3.0) -> None:
    """Open and close a WebSocket connection to check reachability."""
    async with asyncio.timeout(timeout):
        async with websockets.connect(server):
            return


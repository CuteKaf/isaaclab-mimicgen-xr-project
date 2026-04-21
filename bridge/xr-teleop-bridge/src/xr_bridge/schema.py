"""Schema helpers for XR teleoperation frames."""

from __future__ import annotations

from dataclasses import asdict, dataclass
import math
import time
from typing import Any

SCHEMA_NAME = "isaaclab_xr_teleop_v1"


@dataclass
class Pose:
    """Tracked XR pose."""

    position: list[float]
    orientation_xyzw: list[float]
    tracking_valid: bool = True


@dataclass
class Buttons:
    """Controller button and axis state."""

    a: bool = False
    b: bool = False
    right_grip: bool = False
    right_trigger: float = 0.0
    right_axis_click: bool = False
    left_grip: bool = False
    left_trigger: float = 0.0
    left_axis_click: bool = False


@dataclass
class XRFrame:
    """Full XR frame sent from Ubuntu A to Ubuntu B."""

    schema: str
    timestamp: float
    frame_id: int
    head_pose: Pose
    right_controller_pose: Pose
    left_controller_pose: Pose
    buttons: Buttons

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


def make_mock_frame(frame_id: int) -> XRFrame:
    """Create a deterministic moving frame for network and receiver tests."""
    t = time.time()
    phase = frame_id / 60.0
    x = 0.25 + 0.05 * math.sin(phase)
    z = -0.35 + 0.05 * math.cos(phase)
    trigger = 0.5 + 0.5 * math.sin(phase * 0.5)
    return XRFrame(
        schema=SCHEMA_NAME,
        timestamp=t,
        frame_id=frame_id,
        head_pose=Pose(
            position=[0.0, 1.6, 0.0],
            orientation_xyzw=[0.0, 0.0, 0.0, 1.0],
            tracking_valid=True,
        ),
        right_controller_pose=Pose(
            position=[x, 1.25, z],
            orientation_xyzw=[0.0, 0.0, 0.0, 1.0],
            tracking_valid=True,
        ),
        left_controller_pose=Pose(
            position=[-0.25, 1.25, -0.35],
            orientation_xyzw=[0.0, 0.0, 0.0, 1.0],
            tracking_valid=True,
        ),
        buttons=Buttons(
            right_grip=True,
            right_trigger=max(0.0, min(1.0, trigger)),
        ),
    )


def validate_frame(frame: dict[str, Any]) -> None:
    """Validate the minimal shape of an XR frame."""
    required = [
        "schema",
        "timestamp",
        "frame_id",
        "head_pose",
        "right_controller_pose",
        "left_controller_pose",
        "buttons",
    ]
    for key in required:
        if key not in frame:
            raise ValueError(f"missing required key: {key}")
    if frame["schema"] != SCHEMA_NAME:
        raise ValueError(f"unsupported schema: {frame['schema']!r}")
    for pose_key in ["head_pose", "right_controller_pose", "left_controller_pose"]:
        pose = frame[pose_key]
        if len(pose.get("position", [])) != 3:
            raise ValueError(f"{pose_key}.position must have length 3")
        if len(pose.get("orientation_xyzw", [])) != 4:
            raise ValueError(f"{pose_key}.orientation_xyzw must have length 4")


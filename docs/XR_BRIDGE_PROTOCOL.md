# XR Bridge Protocol

The first bridge version uses WebSocket JSON.

Ubuntu A is the client. Ubuntu B is the server.

Default server URL:

```text
ws://<ubuntu-b-host>:8765/xr
```

Environment variable:

```text
XR_BRIDGE_SERVER=ws://<ubuntu-b-host>:8765/xr
```

Default sending rate: `60 Hz`.

## Schema

Every message must contain:

```json
{
  "schema": "isaaclab_xr_teleop_v1",
  "timestamp": 1710000000.123,
  "frame_id": 12345,
  "head_pose": {
    "position": [0.0, 1.6, 0.0],
    "orientation_xyzw": [0.0, 0.0, 0.0, 1.0],
    "tracking_valid": true
  },
  "right_controller_pose": {
    "position": [0.25, 1.25, -0.35],
    "orientation_xyzw": [0.0, 0.0, 0.0, 1.0],
    "tracking_valid": true
  },
  "left_controller_pose": {
    "position": [-0.25, 1.25, -0.35],
    "orientation_xyzw": [0.0, 0.0, 0.0, 1.0],
    "tracking_valid": true
  },
  "buttons": {
    "a": false,
    "b": false,
    "right_grip": true,
    "right_trigger": 0.72,
    "right_axis_click": false,
    "left_grip": false,
    "left_trigger": 0.0,
    "left_axis_click": false
  }
}
```

## Semantics

- `position`: meters, XR source coordinate frame before Ubuntu B calibration.
- `orientation_xyzw`: unit quaternion in XYZW order.
- `tracking_valid`: false means Ubuntu B must ignore that pose for robot control.
- `right_grip`: enables arm control in the first teleop mapping.
- `right_trigger`: controls gripper open/close.
- `b`: start/end recording.
- `a`: recalibrate.
- `right_axis_click`: reset/discard.

## Ubuntu B Responsibilities

Ubuntu B must not assume the XR coordinate frame equals the robot base frame. It should:

1. Wait for a calibration event.
2. Store reference controller pose and current robot EEF pose.
3. Convert controller deltas to target EEF deltas.
4. Clamp translation and rotation rates.
5. Convert target EEF pose to Isaac Lab action.


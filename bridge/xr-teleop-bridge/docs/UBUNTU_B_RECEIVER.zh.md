# Ubuntu B Receiver Contract

Ubuntu B should expose a WebSocket endpoint:

```text
ws://<ubuntu-b-host>:8765/xr
```

The endpoint should:

1. Accept JSON frames.
2. Validate `schema == isaaclab_xr_teleop_v1`.
3. Print recent frame rate and latest button state during smoke tests.
4. Feed valid frames to the Isaac Lab Teleop Adapter.

Ubuntu B should ignore controller poses with `tracking_valid=false`.


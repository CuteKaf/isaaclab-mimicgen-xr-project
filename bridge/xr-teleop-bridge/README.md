# XR Teleop Bridge

Ubuntu A bridge for forwarding PICO / XRoboToolkit input to Ubuntu B.

This package intentionally does not depend on Isaac Sim or Isaac Lab.

## Install

```bash
cd bridge/xr-teleop-bridge
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Mock Sender

```bash
python scripts/run_mock_sender.py --server ws://<ubuntu-b-host>:8765/xr --hz 60
```

## Healthcheck

```bash
python scripts/check_lab_connection.py --server ws://<ubuntu-b-host>:8765/xr
```

## Real XR Sender

`scripts/run_xrobotoolkit_sender.py` is a placeholder entry point. Ubuntu A should wire it to the local XRoboToolkit / Teleop Sample API once the exact local package and sample output are available.


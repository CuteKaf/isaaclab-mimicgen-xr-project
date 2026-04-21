# Ubuntu A Setup

```bash
cd xr-teleop-bridge
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

检查 Ubuntu B 是否可连：

```bash
python scripts/check_lab_connection.py --server ws://<ubuntu-b-host>:8765/xr
```

发送 mock XR 数据：

```bash
python scripts/run_mock_sender.py --server ws://<ubuntu-b-host>:8765/xr --hz 60
```

真实 XRoboToolkit 接入前，先确保 mock sender 能被 Ubuntu B receiver 收到。


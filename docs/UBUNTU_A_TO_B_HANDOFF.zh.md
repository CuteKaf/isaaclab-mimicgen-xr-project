# Ubuntu A 到 Ubuntu B 联调顺序

## 1. Ubuntu B 启动 receiver

第一阶段可以先用 mock receiver 或 Ubuntu B 的真实 receiver。

```bash
cd xr-teleop-bridge
python scripts/run_mock_receiver.py --host 0.0.0.0 --port 8765
```

## 2. Ubuntu A 检查连接

```bash
python scripts/check_lab_connection.py --server ws://<ubuntu-b-host>:8765/xr
```

## 3. Ubuntu A 发送 mock frame

```bash
python scripts/run_mock_sender.py --server ws://<ubuntu-b-host>:8765/xr --hz 60
```

Ubuntu B 应该看到持续更新的 frame id、按钮状态和 controller position。

## 4. Ubuntu A 接入真实 XRoboToolkit

替换 `src/xr_bridge/xrobotoolkit_sender.py` 中的 `read_xrobotoolkit_frame`。

要求：

- 真实 XR 输入不可用时明确报错。
- 不允许把 mock 数据伪装成真实 XR 数据。
- 输出字段必须符合 `isaaclab_xr_teleop_v1`。

## 5. Ubuntu B 接入 Isaac Lab Teleop Adapter

Ubuntu B receiver 收到 frame 后：

- 校准 XR frame 到 robot base frame。
- `right_grip=true` 时启用 arm control。
- `right_trigger` 控制 gripper。
- `b` 开始/结束录制。
- `a` 重标定。
- `right_axis_click` reset/discard。


# Ubuntu A Codex Prompt

你是 Ubuntu A 上的 Codex。你的机器是 XR 前端机，不运行 Isaac Sim / Isaac Lab。

## 项目背景

我们在做 Isaac Lab 版 MimicGen 平台。Ubuntu B 是远程仿真服务器，负责运行 Isaac Lab、Franka IK absolute pose control、demo 录制、replay、annotate、generate、train、eval。

Ubuntu A 只负责连接 PICO 4 Ultra / XRoboToolkit，读取 XR 输入，并把标准化后的 XR 数据流发送给 Ubuntu B。

## 你的职责

1. 不要安装或运行 Isaac Sim。
2. 不要修改 Ubuntu B 的 IsaacLab 仓库。
3. 在本机创建或维护轻量仓库 `xr-teleop-bridge`。
4. 实现 Ubuntu A 端 XR 输入桥接器：
   - 从 XRoboToolkit / Teleop Sample 读取 head pose、left/right controller pose、trigger、grip、buttons、tracking_valid。
   - 转成 schema 为 `isaaclab_xr_teleop_v1` 的 JSON 消息。
   - 通过 WebSocket 发送到 Ubuntu B。
5. 同时实现 mock sender：
   - 不连接 PICO 时，也能持续发送假 pose 和按钮数据。
   - 用于测试 Ubuntu A -> Ubuntu B 网络链路。
6. 实现 healthcheck：
   - 检查 Ubuntu B host/port 是否可连。
   - 打印发送频率、重连情况、最近一帧数据。
7. 文档必须写清楚：
   - Ubuntu A 的安装步骤。
   - 如何运行 mock sender。
   - 如何运行 XRoboToolkit sender。
   - WebSocket JSON schema。
   - 如何和 Ubuntu B 的接收端联调。

## 推荐仓库结构

```text
xr-teleop-bridge/
  README.md
  docs/
    ARCHITECTURE.zh.md
    MESSAGE_SCHEMA.md
    UBUNTU_A_SETUP.zh.md
    UBUNTU_B_RECEIVER.zh.md
  src/
    xr_bridge/
      __init__.py
      schema.py
      transport.py
      mock_xr_sender.py
      xrobotoolkit_sender.py
      healthcheck.py
  scripts/
    run_mock_sender.py
    run_xrobotoolkit_sender.py
    check_lab_connection.py
  examples/
    sample_frame.json
  pyproject.toml
```

## 默认协议

- Ubuntu A 主动连接 Ubuntu B。
- 使用 WebSocket JSON。
- 默认地址通过环境变量配置：

```text
XR_BRIDGE_SERVER=ws://<ubuntu-b-host>:8765/xr
```

- 发送频率默认 `60 Hz`。
- 如果连接断开，自动重连。
- 如果 XR 输入不可用，必须明确报错，不要伪装成真实数据；只有 mock sender 可以发假数据。

## 第一阶段验收

1. `python scripts/run_mock_sender.py --server ws://<ubuntu-b-host>:8765/xr --hz 60` 能运行。
2. Ubuntu B 能看到持续更新的 JSON frame。
3. `python scripts/check_lab_connection.py --server ws://<ubuntu-b-host>:8765/xr` 能检查连接。
4. 没有 PICO 时，mock sender 可以完成联调。
5. 有 PICO 时，xrobotoolkit sender 能打印真实 controller pose 和按钮状态。

请先检查当前机器系统、Python、网络环境，然后创建仓库并实现第一阶段 mock sender、schema、transport、healthcheck 和文档。


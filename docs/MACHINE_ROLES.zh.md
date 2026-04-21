# 机器分工

## Mac

Mac 是控制面，不跑仿真，也不接 XR 设备的核心服务。

职责：

- SSH 到 Ubuntu A / Ubuntu B。
- 运行 Codex 管理项目。
- 查看日志、整理文档、发起命令。
- 作为项目协调入口。

## Ubuntu A: XR 前端机

Ubuntu A 是 XR 输入前端，只负责采集和转发。

职责：

- 连接 PICO 4 Ultra。
- 运行 XRoboToolkit / PC Service / Teleop Sample。
- 读取 head pose、controller pose、trigger、grip、buttons、tracking_valid。
- 转成 `isaaclab_xr_teleop_v1` JSON frame。
- 通过 WebSocket 主动连接 Ubuntu B。
- 提供 mock sender 和 healthcheck。

明确不做：

- 不安装或运行 Isaac Sim。
- 不训练模型。
- 不做 MimicGen 数据生成。
- 不直接修改 Ubuntu B 的 IsaacLab 仓库。

## Ubuntu B: Isaac Lab 后端机

Ubuntu B 是仿真和学习后端。

职责：

- 运行 `/home/fanzhen/projects/IsaacLab-latest`。
- 运行 Isaac Lab / Isaac Sim。
- 接收 Ubuntu A 的 XR frame。
- 将 XR frame 映射为 Franka IK absolute pose action。
- 录制标准 Isaac Lab HDF5 demo。
- 执行 replay、annotate、generate、train、eval。

## 网络关系

推荐方向：

```text
PICO 4 Ultra <-> Ubuntu A
Ubuntu A     -> Ubuntu B websocket
Mac          -> Ubuntu A / Ubuntu B via ssh
```

Ubuntu A 主动连接 Ubuntu B，默认地址：

```text
XR_BRIDGE_SERVER=ws://<ubuntu-b-host>:8765/xr
```


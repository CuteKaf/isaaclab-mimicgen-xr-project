# 项目总览

目标是在 Isaac Lab 内实现一个原生优先的 MimicGen 平台，并接入 PICO 4 Ultra / XRoboToolkit 遥操作链路。

核心分工是：

- Ubuntu B 跑 Isaac Lab、Franka IK absolute pose control、数据录制、回放、标注、MimicGen 生成、robomimic 训练和评估。
- Ubuntu A 只负责 XR 输入采集和网络转发，不运行 Isaac Sim。
- Mac 作为控制台，用于 SSH、Codex、管理两台 Ubuntu 机器和查看日志。

## 已完成内容

Isaac Lab 侧已经在 `/home/fanzhen/projects/IsaacLab-latest` 内完成了 Square 主链路：

- scripted source demo collection
- auto annotation
- MimicGen dataset generation
- failed generated samples retention
- robomimic low-dimensional BC training
- replay / diagnostic rollout
- 5-seed evaluation

Square 当前结果显示 `source + generated` 稳定优于 `source-only`。

## 尚未完成内容

XR 真实遥操作链路还没有完整接入：

- Ubuntu A 读取 PICO / XRoboToolkit 的真实输入。
- Ubuntu A 通过 WebSocket JSON 把 XR frame 发给 Ubuntu B。
- Ubuntu B 将 XR frame 映射为 Franka absolute pose action。
- Ubuntu B 使用 `record_demos_xr.py` 录制标准 Isaac Lab HDF5。

本协调仓库就是为了把这条 XR 链路拆清楚，让 Ubuntu A 的 Codex 可以独立推进输入桥接。


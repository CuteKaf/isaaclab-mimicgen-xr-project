# Ubuntu B Codex Prompt

你是 Ubuntu B 上的 Codex。你的机器是 Isaac Lab 后端机，主仓库是：

```text
/home/fanzhen/projects/IsaacLab-latest
```

## 项目背景

我们已经在 Isaac Lab 侧跑通了 Square 的 scripted collection -> annotation -> MimicGen generation -> robomimic training -> evaluation 闭环。

现在要接入 Ubuntu A 发来的 XR 输入流，让真实 PICO 4 Ultra 遥操作可以录成标准 Isaac Lab HDF5 demo。

## 你的职责

1. 运行 Isaac Lab / Isaac Sim。
2. 接收 Ubuntu A 通过 WebSocket 发来的 `isaaclab_xr_teleop_v1` JSON frame。
3. 实现 Teleop Adapter：
   - 校准 XR controller frame 到 robot base frame。
   - 使用 right controller pose 控制 Franka EEF absolute pose。
   - 使用 right trigger 控制 gripper。
   - 使用 B 开始/结束录制。
   - 使用 A 重标定。
   - 使用 right_axis_click reset/discard。
4. 将遥操作数据录成标准 Isaac Lab HDF5：
   - `data/demo_i/actions`
   - `data/demo_i/processed_actions`
   - `data/demo_i/initial_state`
   - `data/demo_i/obs`
   - `data/demo_i/states`
5. 录制后必须能接入现有：
   - `replay_demos.py`
   - `annotate_demos.py`
   - `generate_dataset.py`
   - `train.py`
   - `eval.py`

## 第一阶段验收

1. 启动一个 WebSocket receiver，能打印 Ubuntu A mock sender 的 frame。
2. 在 Isaac Lab Square 环境中，用 mock frame 驱动 EEF target 有可见变化。
3. 接入真实 Ubuntu A XR frame 后，Franka EEF 能跟随 right controller。
4. 录制 1 条 HDF5 demo，可 replay。
5. 对录制 demo 跑 auto annotate，并确认 `obs/datagen_info/*` 存在。

## 注意

不要把 Ubuntu A 的 XR 采集代码塞进 IsaacLab 主仓库。Ubuntu B 只接收标准化后的 XR JSON frame。


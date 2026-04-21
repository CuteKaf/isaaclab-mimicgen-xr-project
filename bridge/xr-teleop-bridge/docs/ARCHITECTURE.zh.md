# XR Teleop Bridge 架构

Ubuntu A 只做输入采集和转发。

```text
PICO 4 Ultra / XRoboToolkit
        |
        v
Ubuntu A xr-teleop-bridge
        |
        | WebSocket JSON, isaaclab_xr_teleop_v1
        v
Ubuntu B Isaac Lab receiver / Teleop Adapter
        |
        v
Franka IK absolute pose control
```

第一阶段先用 mock sender 联调网络和 Ubuntu B receiver。真实 PICO 接入只替换输入源，不改变网络协议。


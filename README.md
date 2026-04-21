# Isaac Lab MimicGen XR Project

This repository is the coordination package for the Isaac Lab native MimicGen migration and XR teleoperation bridge.

It does not vendor the full `IsaacLab-latest` workspace. The real Isaac Lab implementation remains in:

```text
/home/fanzhen/projects/IsaacLab-latest
```

This repository records the project architecture, machine roles, protocol contracts, Codex prompts for each machine, key commands, and current Square experiment results. It is meant to be copied or pushed to GitHub so another Codex instance, especially on Ubuntu A, can understand the whole project without reading the full Isaac Lab codebase first.

## Machine Roles

- Mac: control plane, SSH, Codex, project management, logs.
- Ubuntu A: XR front-end. Connects to PICO 4 Ultra / XRoboToolkit, normalizes XR input, sends JSON frames to Ubuntu B.
- Ubuntu B: simulation back-end. Runs Isaac Lab, MimicGen, dataset recording, replay, annotation, generation, robomimic training, and evaluation.

## Current Status

- Isaac Lab side Square scripted collection, annotation, generation, training, and 5-seed evaluation are working.
- `source + generated` consistently outperforms `source-only` on Square.
- XR live teleoperation is not yet wired into Isaac Lab. This repository defines the bridge contract and Ubuntu A task.

## Start Here

1. Read [docs/PROJECT_OVERVIEW.zh.md](docs/PROJECT_OVERVIEW.zh.md).
2. Read [docs/MACHINE_ROLES.zh.md](docs/MACHINE_ROLES.zh.md).
3. For Ubuntu A Codex, use [prompts/ubuntu_a_codex_prompt.zh.md](prompts/ubuntu_a_codex_prompt.zh.md).
4. For Ubuntu B Codex, use [prompts/ubuntu_b_codex_prompt.zh.md](prompts/ubuntu_b_codex_prompt.zh.md).
5. XR bridge message schema is in [docs/XR_BRIDGE_PROTOCOL.md](docs/XR_BRIDGE_PROTOCOL.md).

## Bridge Skeleton

A minimal Python package lives in:

```text
bridge/xr-teleop-bridge
```

It provides a mock sender, schema helpers, WebSocket transport, and healthcheck command. Ubuntu A should extend `xrobotoolkit_sender.py` to read real XRoboToolkit data.


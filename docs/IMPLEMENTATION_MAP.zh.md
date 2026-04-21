# Isaac Lab 实现映射

本仓库是协调仓库，真实实现仍在：

```text
/home/fanzhen/projects/IsaacLab-latest
```

## Square / Assembly 任务

```text
source/isaaclab_tasks/isaaclab_tasks/manager_based/manipulation/assembly/
```

用途：

- Square / NutAssembly 近似任务。
- 刚体资产、reset 随机化、成功判定、失败条件。
- Square 当前主验收环境：`Isaac-Square-Franka-IK-Abs-Mimic-v0`。

## Mimic 环境注册与 wrapper

```text
source/isaaclab_mimic/isaaclab_mimic/envs/
```

用途：

- 注册 Mimic env。
- 提供 Mimic API：
  - `get_robot_eef_pose`
  - `target_eef_pose_to_action`
  - `action_to_target_eef_pose`
  - `actions_to_gripper_actions`
  - `get_object_poses`
  - `get_subtask_term_signals`

## 对外脚本

```text
scripts/imitation_learning/isaaclab_mimic/
```

关键脚本：

- `record_demos_scripted.py`
- `annotate_demos.py`
- `generate_dataset.py`
- `replay_demos.py`
- `train.py`
- `eval.py`

## robomimic 训练 / 评估

```text
scripts/imitation_learning/robomimic/
```

关键脚本：

- `train.py`
- `play.py`
- `robust_eval.py`

`play.py` 已加入 Square 调试输出能力：

- `--print_every`
- `--square_debug`
- `--debug_file`

## Square 数据与结果

```text
datasets/square/
```

代表文件：

- `source_dataset.hdf5`: 10 条 source demo。
- `source_dataset_22.hdf5`: 22 条 source demo。
- `annotated_dataset_22.hdf5`: 21 条 annotated demo。
- `generated_dataset_240.hdf5`: 240 条 generated success demo。
- `generated_dataset_240_failed.hdf5`: 22 条 generated failed demo。
- `source_plus_generated_240_dataset.hdf5`: 262 条训练 demo。

## Square 训练结果

```text
logs/robomimic_square/Isaac-Square-Franka-IK-Abs-Mimic-v0/
```

代表 run：

- `square_source_only_22/20260417205806`
- `square_source_plus_generated_240/20260417210125`

## Square 评估结果

```text
datasets/square/eval/
```

代表目录：

- `play_source_only_22_5seeds`
- `play_source_plus_generated_240_5seeds`

当前结论：

- `source-only_22` mean success rate: `0.34`
- `source+generated_240` mean success rate: `0.58`


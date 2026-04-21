# 当前进度

## Isaac Lab 实现位置

主实现仓库：

```text
/home/fanzhen/projects/IsaacLab-latest
```

核心落点：

- `source/isaaclab_mimic`
- `source/isaaclab_tasks`
- `scripts/imitation_learning/isaaclab_mimic`
- `scripts/imitation_learning/robomimic`

## 已跑通任务

Square 已完成：

- scripted collection
- annotation
- generation
- training
- replay / diagnostic rollout
- 5-seed evaluation

## 代表数据产物

```text
datasets/square/source_dataset.hdf5
datasets/square/source_dataset_22.hdf5
datasets/square/annotated_dataset_22.hdf5
datasets/square/generated_dataset_120.hdf5
datasets/square/generated_dataset_240.hdf5
datasets/square/generated_dataset_240_failed.hdf5
datasets/square/source_plus_generated_240_dataset.hdf5
```

注意：`source_dataset_22.hdf5` 有 22 条 demo，但 `annotated_dataset_22.hdf5` 当前只有 21 条。缺失的是 `demo_21`，应后续排查自动标注逻辑为什么跳过该 demo。

## 当前最重要结论

在 Square 上，`source + generated` 已经稳定优于 `source-only`，并且不是单个 seed 的偶然结果。


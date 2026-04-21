# 数据流水线

当前 Isaac Lab 侧主格式是 HDF5。

标准 episode 结构：

```text
data/demo_i/actions
data/demo_i/processed_actions
data/demo_i/initial_state
data/demo_i/obs
data/demo_i/states
data/demo_i/obs/datagen_info/eef_pose
data/demo_i/obs/datagen_info/target_eef_pose
data/demo_i/obs/datagen_info/object_pose
data/demo_i/obs/datagen_info/subtask_term_signals
```

Square 已跑通流程：

```text
record_demos_scripted.py
  -> source_dataset.hdf5
annotate_demos.py --auto
  -> annotated_dataset.hdf5
generate_dataset.py
  -> generated_dataset.hdf5
  -> generated_dataset_failed.hdf5
merge_hdf5_datasets.py
  -> source_plus_generated_dataset.hdf5
train.py
  -> robomimic checkpoint
play.py / eval.py
  -> success-rate summary
```

XR 接入后的目标流程：

```text
Ubuntu A XR input
  -> WebSocket JSON
Ubuntu B Teleop Adapter
  -> record_demos_xr.py
  -> source_dataset_xr.hdf5
  -> annotate / generate / train / eval
```


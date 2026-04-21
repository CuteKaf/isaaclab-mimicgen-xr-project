# Square 实验结果

评估口径：

- Environment: `Isaac-Square-Franka-IK-Abs-Mimic-v0`
- Horizon: `260`
- Rollouts per seed: `20`
- Seeds: `101, 202, 303, 404, 505`
- Evaluation runner: `scripts/imitation_learning/robomimic/play.py`

## 10 source + 120 generated

`source-only`:

| seed | success rate |
| --- | ---: |
| 101 | 0.05 |
| 202 | 0.10 |
| 303 | 0.00 |
| 404 | 0.15 |
| 505 | 0.00 |

Average: `0.06`

`source + generated_120`:

| seed | success rate |
| --- | ---: |
| 101 | 0.30 |
| 202 | 0.30 |
| 303 | 0.50 |
| 404 | 0.50 |
| 505 | 0.30 |

Average: `0.38`

## 22 source + 240 generated

`source-only_22`:

| seed | success rate |
| --- | ---: |
| 101 | 0.45 |
| 202 | 0.10 |
| 303 | 0.35 |
| 404 | 0.50 |
| 505 | 0.30 |

Average: `0.34`

`source + generated_240`:

| seed | success rate |
| --- | ---: |
| 101 | 0.70 |
| 202 | 0.40 |
| 303 | 0.75 |
| 404 | 0.60 |
| 505 | 0.45 |

Average: `0.58`

## Interpretation

The larger generated dataset improves the policy over both the original 10-demo baseline and the expanded 22-demo source-only baseline. The improvement is visible across all five seeds.


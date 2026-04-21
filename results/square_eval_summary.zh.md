# Square 评估摘要

评估任务：`Isaac-Square-Franka-IK-Abs-Mimic-v0`

评估设置：

- horizon: `260`
- 每个 seed: `20` rollouts
- seeds: `101, 202, 303, 404, 505`

## 结果

| dataset | mean success rate |
| --- | ---: |
| source-only 10 | 0.06 |
| source + generated 120 | 0.38 |
| source-only 22 | 0.34 |
| source + generated 240 | 0.58 |

结论：在 Square 上，MimicGen generated data 稳定提升策略成功率。


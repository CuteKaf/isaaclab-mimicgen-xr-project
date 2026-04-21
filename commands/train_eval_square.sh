#!/usr/bin/env bash
set -euo pipefail

cd /home/fanzhen/projects/IsaacLab-latest
source /home/fanzhen/miniconda3/etc/profile.d/conda.sh
conda activate env_isaaclab_migrate

./isaaclab.sh -p scripts/imitation_learning/isaaclab_mimic/train.py \
  --task Isaac-Square-Franka-IK-Abs-Mimic-v0 \
  --algo bc \
  --dataset datasets/square/source_plus_generated_240_dataset.hdf5 \
  --name square_source_plus_generated_240 \
  --log_dir robomimic_square \
  --epochs 200

./isaaclab.sh -p scripts/imitation_learning/robomimic/play.py \
  --task Isaac-Square-Franka-IK-Abs-Mimic-v0 \
  --checkpoint logs/robomimic_square/Isaac-Square-Franka-IK-Abs-Mimic-v0/square_source_plus_generated_240/20260417210125/models/model_epoch_200.pth \
  --horizon 260 \
  --num_rollouts 20 \
  --seed 101 \
  --headless \
  --device cuda:0


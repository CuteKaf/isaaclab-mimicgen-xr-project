#!/usr/bin/env bash
set -euo pipefail

cd /home/fanzhen/projects/IsaacLab-latest
source /home/fanzhen/miniconda3/etc/profile.d/conda.sh
conda activate env_isaaclab_migrate

./isaaclab.sh -p scripts/imitation_learning/isaaclab_mimic/record_demos_scripted.py \
  --task Isaac-Square-Franka-IK-Abs-Mimic-v0 \
  --dataset_file datasets/square/source_dataset.hdf5 \
  --num_demos 10 \
  --max_attempts 120 \
  --max_steps_per_attempt 260 \
  --num_success_steps 4 \
  --headless \
  --device cuda:0

./isaaclab.sh -p scripts/imitation_learning/isaaclab_mimic/annotate_demos.py \
  --task Isaac-Square-Franka-IK-Abs-Mimic-v0 \
  --input_file datasets/square/source_dataset.hdf5 \
  --output_file datasets/square/annotated_dataset.hdf5 \
  --auto \
  --headless \
  --device cuda:0

./isaaclab.sh -p scripts/imitation_learning/isaaclab_mimic/generate_dataset.py \
  --task Isaac-Square-Franka-IK-Abs-Mimic-v0 \
  --input_file datasets/square/annotated_dataset.hdf5 \
  --output_file datasets/square/generated_dataset.hdf5 \
  --generation_num_trials 20 \
  --num_envs 1 \
  --headless \
  --device cuda:0


---

title: Manufacturing Process Optimization
emoji: ⚙️
colorFrom: blue
colorTo: green
sdk: docker
app_file: inference.py
pinned: false
-------------

# Manufacturing Process Optimization (OpenEnv RL)

## Overview

This project implements a reinforcement learning environment for manufacturing process optimization using OpenEnv. The environment simulates a factory where jobs must be assigned to machines efficiently to minimize delays and maximize utilization.

## Motivation

Efficient scheduling is essential in manufacturing systems. This environment models real-world constraints such as machine availability, job priorities, and machine breakdowns, enabling the development of intelligent scheduling strategies.

## Observation Space

The state includes:

* machines: list of machines with id, status (idle, busy, broken), remaining_time, breakdown probability
* job_queue: list of jobs with id, processing_time, and priority
* current_time: current timestep

## Action Space

An action consists of:

* machine_id: selected machine
* job_id: selected job

The agent assigns a job to a machine.

## Tasks

Three tasks are defined:

1. Minimize Idle Time (Easy)
   Score = 1 - (idle machines / total machines)

2. Optimize Completion Time (Medium)
   Score = optimal_time / actual_time

3. Handle Machine Failures (Hard)
   Score = working machines / total machines

The overall score is the average of all three tasks.

## Reward Function

The reward provides:

* positive reward for job completion
* penalty for idle machines
* penalty for delay based on time

Rewards are normalized between 0 and 1.

## Setup

Install dependencies:

```
pip install -r requirements.txt
```

Set environment variable:

```
set HF_TOKEN=dummy
```

Run inference:

```
python inference.py
```

## Docker

Build:

```
docker build -t openenv-rl .
```

Run:

```
docker run openenv-rl
```

## Baseline Performance

Typical results using the baseline agent:

* Task 1: 1.0
* Task 2: 1.0
* Task 3: 1.0
* Overall: 1.0

Scores may vary due to randomness.

## Project Structure

```
env/
  env.py
  models.py
  tasks.py
  openenv.yaml

agent.py
inference.py
test_env.py
requirements.txt
Dockerfile
README.md
```

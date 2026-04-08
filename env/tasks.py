def clamp_score(score):
    return max(0.01, min(0.99, score))


def task_idle_time(env):
    total_machines = len(env.state.machines)

    if total_machines == 0:
        return 0.5  # neutral

    idle_machines = sum(1 for m in env.state.machines if m.status == "idle")

    utilization = 1 - (idle_machines / total_machines)

    return clamp_score(utilization)


def task_completion_time(env, optimal_time=5):
    actual_time = env.state.current_time

    if actual_time == 0:
        return 0.5

    score = optimal_time / actual_time

    return clamp_score(score)


def task_breakdown_handling(env):
    total_machines = len(env.state.machines)

    if total_machines == 0:
        return 0.5

    working_machines = sum(1 for m in env.state.machines if m.status != "broken")

    efficiency = working_machines / total_machines

    return clamp_score(efficiency)


def overall_score(env):
    t1 = task_idle_time(env)
    t2 = task_completion_time(env)
    t3 = task_breakdown_handling(env)

    score = 0.4 * t1 + 0.4 * t2 + 0.2 * t3

    return clamp_score(score)
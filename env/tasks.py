def task_idle_time(env):
    #maximize machine utilization
    total_machines = len(env.state.machines)

    if total_machines == 0:
        return 0.0

    idle_machines = sum(1 for m in env.state.machines if m.status == "idle")

    utilization = 1 - (idle_machines / total_machines)

    return max(0.0, min(1.0, utilization))


def task_completion_time(env, optimal_time=5):
    #minimize total completion
    actual_time = env.state.current_time

    if actual_time == 0:
        return 0.0

    score = optimal_time / actual_time

    return max(0.0, min(1.0, score))


def task_breakdown_handling(env):
    #handle machine failure
    total_machines = len(env.state.machines)

    if total_machines == 0:
        return 0.0

    working_machines = sum(1 for m in env.state.machines if m.status != "broken")

    efficiency = working_machines / total_machines

    return max(0.0, min(1.0, efficiency))


def overall_score(env):
    #weighted overall performance score
    t1 = task_idle_time(env)
    t2 = task_completion_time(env)
    t3 = task_breakdown_handling(env)


    score = 0.4 * t1 + 0.4 * t2 + 0.2 * t3

    return max(0.0, min(1.0, score))
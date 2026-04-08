def safe_score(numerator, denominator):
    if denominator == 0:
        return 0.5

    score = (numerator + 0.1) / (denominator + 0.2)
    return float(score)


def task_idle_time(env):
    total = len(env.state.machines)
    idle = sum(1 for m in env.state.machines if m.status == "idle")

    utilization = 1 - safe_score(idle, total)
    return utilization


def task_completion_time(env, optimal_time=5):
    actual = env.state.current_time

    if actual == 0:
        return 0.5

    score = optimal_time / (actual + 1)  # avoids 1.0
    return float(max(0.01, min(0.99, score)))


def task_breakdown_handling(env):
    total = len(env.state.machines)
    working = sum(1 for m in env.state.machines if m.status != "broken")

    efficiency = safe_score(working, total)
    return efficiency


def overall_score(env):
    t1 = task_idle_time(env)
    t2 = task_completion_time(env)
    t3 = task_breakdown_handling(env)

    score = 0.4 * t1 + 0.4 * t2 + 0.2 * t3
    return float(max(0.01, min(0.99, score)))
EPSILON = 1e-3


def strict_unit_interval(value):
    """Keep all grader outputs strictly inside (0, 1)."""
    return float(min(1.0 - EPSILON, max(EPSILON, value)))


def safe_score(numerator, denominator):
    if denominator <= 0:
        return 0.5

    score = (numerator + 0.1) / (denominator + 0.2)
    return strict_unit_interval(score)


def task_idle_time(env):
    total = len(env.state.machines)
    idle = sum(1 for m in env.state.machines if m.status == "idle")

    utilization = 1 - safe_score(idle, total)
    return strict_unit_interval(utilization)


def task_completion_time(env, optimal_time=5):
    actual = env.state.current_time

    if actual == 0:
        return 0.5

    score = optimal_time / (actual + 1)
    return strict_unit_interval(score)


def task_breakdown_handling(env):
    total = len(env.state.machines)
    working = sum(1 for m in env.state.machines if m.status != "broken")

    efficiency = safe_score(working, total)
    return strict_unit_interval(efficiency)


def overall_score(env):
    t1 = task_idle_time(env)
    t2 = task_completion_time(env)
    t3 = task_breakdown_handling(env)

    score = 0.4 * t1 + 0.4 * t2 + 0.2 * t3
    return strict_unit_interval(score)

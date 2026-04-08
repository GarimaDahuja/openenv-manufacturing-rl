EPSILON = 1e-3


def strict_unit_interval(value):
    """Keep all grader outputs strictly inside (0, 1)."""
    return float(min(1.0 - EPSILON, max(EPSILON, value)))


def _default_state():
    from env.env import ManufacturingEnv

    return ManufacturingEnv().reset()


def _resolve_state(subject):
    """Accept an env instance, a state object, or None from validators."""
    if subject is None:
        return _default_state()

    if hasattr(subject, "state"):
        state = getattr(subject, "state")
        return state if state is not None else _default_state()

    if hasattr(subject, "machines") and hasattr(subject, "job_queue"):
        return subject

    if isinstance(subject, dict):
        return _default_state()

    return _default_state()


def safe_score(numerator, denominator):
    if denominator <= 0:
        return 0.5

    score = (numerator + 0.1) / (denominator + 0.2)
    return strict_unit_interval(score)


def task_idle_time(env):
    state = _resolve_state(env)
    total = len(state.machines)
    idle = sum(1 for m in state.machines if m.status == "idle")

    utilization = 1 - safe_score(idle, total)
    return strict_unit_interval(utilization)


def task_completion_time(env, optimal_time=5):
    state = _resolve_state(env)
    actual = state.current_time

    if actual == 0:
        return 0.5

    score = optimal_time / (actual + 1)
    return strict_unit_interval(score)


def task_breakdown_handling(env):
    state = _resolve_state(env)
    total = len(state.machines)
    working = sum(1 for m in state.machines if m.status != "broken")

    efficiency = safe_score(working, total)
    return strict_unit_interval(efficiency)


def overall_score(env):
    t1 = task_idle_time(env)
    t2 = task_completion_time(env)
    t3 = task_breakdown_handling(env)

    score = 0.4 * t1 + 0.4 * t2 + 0.2 * t3
    return strict_unit_interval(score)

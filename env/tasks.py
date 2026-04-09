EPSILON = 1e-3

TASKS = {
    "easy": {
        "name": "minimize_idle_time",
        "description": "Keep machines busy and avoid idle capacity.",
        "target": "high_utilization",
    },
    "medium": {
        "name": "optimize_completion_time",
        "description": "Finish work quickly with balanced machine usage.",
        "target": "low_elapsed_time",
    },
    "hard": {
        "name": "handle_machine_failures",
        "description": "Maintain throughput despite breakdowns.",
        "target": "resilient_operation",
    },
}


def strict_unit_interval(value):
    return float(min(1.0 - EPSILON, max(EPSILON, value)))


def _default_state():
    from env.env import ManufacturingEnv
    return ManufacturingEnv().reset()


def _resolve_state(subject):
    if subject is None:
        return _default_state()

    if hasattr(subject, "state"):
        state = getattr(subject, "state")
        return state if state is not None else _default_state()

    if hasattr(subject, "machines") and hasattr(subject, "job_queue"):
        return subject

    return _default_state()


def _safe_ratio(numerator, denominator, default=0.5):
    if denominator <= 0:
        return default
    return strict_unit_interval((numerator + 0.1) / (denominator + 0.2))


def _state_metrics(subject):
    state = _resolve_state(subject)
    total_machines = len(state.machines)
    idle_machines = sum(1 for machine in state.machines if machine.status == "idle")
    working_machines = sum(
        1 for machine in state.machines if machine.status != "broken"
    )
    queue_size = len(state.job_queue)
    elapsed_time = state.current_time

    return {
        "state": state,
        "total_machines": total_machines,
        "idle_machines": idle_machines,
        "working_machines": working_machines,
        "queue_size": queue_size,
        "elapsed_time": elapsed_time,
    }


def task_idle_time(subject):
    metrics = _state_metrics(subject)
    utilization = 1.0 - _safe_ratio(
        metrics["idle_machines"], metrics["total_machines"]
    )
    return strict_unit_interval(utilization)


def task_completion_time(subject):
    metrics = _state_metrics(subject)
    queue_pressure = 1.0 / (metrics["queue_size"] + 2.0)
    time_efficiency = 1.0 / (metrics["elapsed_time"] + 2.0)
    score = 0.6 * queue_pressure + 0.4 * time_efficiency
    return strict_unit_interval(score)


def task_breakdown_handling(subject):
    metrics = _state_metrics(subject)
    resilience = _safe_ratio(metrics["working_machines"], metrics["total_machines"])
    return strict_unit_interval(resilience)


def overall_score(subject):
    idle_score = task_idle_time(subject)
    completion_score = task_completion_time(subject)
    breakdown_score = task_breakdown_handling(subject)
    score = 0.4 * idle_score + 0.35 * completion_score + 0.25 * breakdown_score
    return strict_unit_interval(score)

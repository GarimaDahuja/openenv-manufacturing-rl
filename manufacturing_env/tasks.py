"""Compatibility wrapper for task graders."""

from env.tasks import overall_score, task_breakdown_handling, task_completion_time, task_idle_time

__all__ = [
    "overall_score",
    "task_breakdown_handling",
    "task_completion_time",
    "task_idle_time",
]

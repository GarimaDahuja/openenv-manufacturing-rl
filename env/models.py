from pydantic import BaseModel
from typing import List, Optional

class Machine(BaseModel):
    id: int
    status: str  # "idle", "busy", "broken"
    remaining_time: int = 0
    breakdown_prob: float = 0.05  # probability of failure

class Job(BaseModel):
    id: int
    processing_time: int
    priority: int  # higher = more important

class State(BaseModel):
    machines: List[Machine]
    job_queue: List[Job]
    current_time: int

class Action(BaseModel):
    machine_id: int
    job_id: int
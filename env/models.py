from pydantic import BaseModel
from typing import List

class State(BaseModel):
    machines: List[str]   # placeholder
    job_queue: List[str]  # placeholder
    current_time: int

class Action(BaseModel):
    machine_id: int
    job_id: int
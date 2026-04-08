from fastapi import FastAPI
from env.env import ManufacturingEnv
from env.models import Action

app = FastAPI(
    title="Manufacturing OpenEnv Server",
    version="1.0.0",
    description="Manufacturing process optimization environment",
)

env = ManufacturingEnv()


def _state_schema():
    return {
        "type": "object",
        "properties": {
            "machines": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer"},
                        "status": {"type": "string"},
                        "remaining_time": {"type": "integer"},
                        "breakdown_prob": {"type": "number"},
                    },
                    "required": ["id", "status", "remaining_time", "breakdown_prob"],
                },
            },
            "job_queue": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "integer"},
                        "processing_time": {"type": "integer"},
                        "priority": {"type": "integer"},
                    },
                    "required": ["id", "processing_time", "priority"],
                },
            },
            "current_time": {"type": "integer"},
        },
        "required": ["machines", "job_queue", "current_time"],
    }


def _action_schema():
    return {
        "type": "object",
        "properties": {
            "machine_id": {"type": "integer"},
            "job_id": {"type": "integer"},
        },
        "required": ["machine_id", "job_id"],
    }


@app.get("/")
def root():
    return {
        "name": "manufacturing_env",
        "status": "ok",
        "message": "Manufacturing OpenEnv server is running",
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/metadata")
def metadata():
    return {
        "name": "manufacturing_env",
        "description": "Manufacturing process optimization environment",
    }


@app.get("/schema")
def schema():
    state_schema = _state_schema()
    return {
        "action": _action_schema(),
        "observation": state_schema,
        "state": state_schema,
    }


@app.post("/reset")
def reset():
    state = env.reset()
    return {
        "observation": state
    }


@app.post("/step")
def step(action: Action):
    state, reward, done, info = env.step(action)
    return {
        "observation": state,
        "reward": float(reward),
        "done": bool(done),
        "info": info if info else {}
    }


@app.get("/state")
def get_state():
    return env.state if env.state is not None else env.reset()

from fastapi import FastAPI
import uvicorn
from env.env import ManufacturingEnv
from env.models import Action

app = FastAPI()
env = ManufacturingEnv()


@app.post("/reset")
def reset():
    state = env.reset()
    return {"observation": state}


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
    return env.state

def main():
    uvicorn.run(app, host="0.0.0.0", port=7860)

if __name__ == "__main__":
    main()
import os
import time
from openai import OpenAI
from env.env import ManufacturingEnv
from agent import BaselineAgent

#req  env variables
API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4.1-mini")
HF_TOKEN = os.getenv("HF_TOKEN", "dummy")

#OpenAI client
client = OpenAI(
    base_url=API_BASE_URL,
    api_key=HF_TOKEN
)

def run_inference():
    env = ManufacturingEnv()
    agent = BaselineAgent()

    state = env.reset()

    print(f"[START] task=manufacturing env=openenv model={MODEL_NAME}")

    done = False
    step_count = 0
    rewards = []
    success = True

    try:
        while not done:
            action = agent.select_action(state)

            state, reward, done, _ = env.step(action)

            step_count += 1

            reward = round(float(reward), 2)
            rewards.append(f"{reward:.2f}")

            print(
                f"[STEP] step={step_count} "
                f"action=machine={action.machine_id},job={action.job_id} "
                f"reward={reward:.2f} "
                f"done={str(done).lower()} "
                f"error=null"
            )

    except Exception as e:
        success = False
        print(
            f"[STEP] step={step_count} action=null "
            f"reward=0.00 done=true error={str(e)}"
        )

    print(
        f"[END] success={str(success).lower()} "
        f"steps={step_count} "
        f"rewards={','.join(rewards) if rewards else '0.00'}"
    )


if __name__ == "__main__":
    run_inference()

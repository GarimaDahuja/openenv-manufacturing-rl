from env.env import ManufacturingEnv
from agent import BaselineAgent
from env.tasks import overall_score

def run_inference():
    env = ManufacturingEnv()
    agent = BaselineAgent()

    state = env.reset()

    print("[START]")

    done = False

    while not done:
        action = agent.select_action(state)

        state, reward, done, _ = env.step(action)

        print(f"[STEP] time={state.current_time}, machine={action.machine_id}, job={action.job_id}, reward={reward}")

    score = overall_score(env)

    print(f"[END] final_score={score}")


if __name__ == "__main__":
    run_inference()
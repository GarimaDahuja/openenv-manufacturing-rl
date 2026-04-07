from env.env import ManufacturingEnv
from env.tasks import task_idle_time, task_completion_time, task_breakdown_handling, overall_score
from agent import BaselineAgent

env = ManufacturingEnv()
agent = BaselineAgent()

state = env.reset()

print("Initial State:", state)

for _ in range(10):
    action = agent.select_action(state)

    state, reward, done, _ = env.step(action)

    print("Time:", state.current_time)
    print("Action:", action)
    print("Machines:", state.machines)
    print("Queue:", state.job_queue)
    print("Reward:", reward)
    print("------")

    if done:
        break

print("Task 1:", task_idle_time(env))
print("Task 2:", task_completion_time(env))
print("Task 3:", task_breakdown_handling(env))
print("Overall:", overall_score(env))
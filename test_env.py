from env.env import ManufacturingEnv
from env.models import Action
from env.tasks import task_idle_time, task_completion_time, task_breakdown_handling, overall_score

env = ManufacturingEnv()
state = env.reset()

print("Initial State:", state)

for _ in range(10):
    if len(state.job_queue) > 0:
        job_id = state.job_queue[0].id
    else:
        job_id = 0

    action = Action(machine_id=0, job_id=job_id)

    state, reward, done, _ = env.step(action)

    print("Time:", state.current_time)
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
from env.env import ManufacturingEnv
from env.models import Action

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
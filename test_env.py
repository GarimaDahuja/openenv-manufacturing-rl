from env.env import ManufacturingEnv
from env.models import Action

env = ManufacturingEnv()
state = env.reset()

print("Initial State:", state)

for _ in range(3):
    action = Action(machine_id=0, job_id=0)
    state, reward, done, _ = env.step(action)
    print("Step:", state)
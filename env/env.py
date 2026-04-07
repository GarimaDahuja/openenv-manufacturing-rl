from env.models import State, Machine, Job, Action
import random

class ManufacturingEnv:
    def __init__(self):
        self.state = None
        self.current_step = 0

    def reset(self):
        """Initialize environment"""

        machines = [
            Machine(id=0, status="idle"),
            Machine(id=1, status="idle")
        ]

        jobs = [
            Job(id=0, processing_time=5, priority=2),
            Job(id=1, processing_time=3, priority=1)
        ]

        self.state = State(
            machines=machines,
            job_queue=jobs,
            current_time=0
        )

        self.current_step = 0
        return self.state

    def step(self, action):
        reward = 0.0
        done = False
        completed_jobs = 0

        machine = next((m for m in self.state.machines if m.id == action.machine_id), None)
        job = next((j for j in self.state.job_queue if j.id == action.job_id), None)

        #assign job if machine is idle
        if machine and job and machine.status == "idle":
            machine.status = "busy"
            machine.remaining_time = job.processing_time
            self.state.job_queue.remove(job)

        #update machines
        for m in self.state.machines:

            #breakdown logic
            if m.status != "broken" and random.random() < m.breakdown_prob:
                m.status = "broken"
                m.remaining_time = 0
                continue

            if m.status == "busy":
                m.remaining_time -= 1

                if m.remaining_time <= 0:
                    m.status = "idle"
                    completed_jobs += 1 #job completed reward

            elif m.status == "broken":
                #simple recovery
                if random.random() < 0.3:
                    m.status = "idle"

        idle_machines = 0
        for m in self.state.machines:
            if m.status == "idle":
                idle_machines += 1

        #time update
        self.state.current_time += 1
        self.current_step += 1

        #end condition
        if self.current_step >= 20 or len(self.state.job_queue) == 0:
            done = True

        #completed jobs reward
        reward += completed_jobs * 1.0

        #idle machines penalty
        reward -= idle_machines * 0.2

        #delay penalty
        reward -= self.state.current_time * 0.01

        #normalize reward b/w 0-1
        reward = max(0.0, min(1.0, reward))

        return self.state, reward, done, {}

    def get_state(self):
        return self.state
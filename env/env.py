from env.models import State, Machine, Job, Action

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
        """Apply action"""

        reward = 0.0
        done = False

        self.current_step += 1

        if self.current_step >= 10:
            done = True

        return self.state, reward, done, {}

    def get_state(self):
        return self.state
class ManufacturingEnv:
    def __init__(self):
        self.state = None
        self.current_step = 0

    def reset(self):
        """Initialize environment"""
        self.state = {
            "machines": ["idle", "idle"],
            "job_queue": ["job1", "job2"],
            "current_time": 0
        }
        self.current_step = 0
        return self.state

    def step(self, action):
        """
        Apply action and return:
        state, reward, done, info
        """
        reward = 0.0
        done = False

        # Placeholder logic (no real simulation yet)
        self.current_step += 1

        if self.current_step >= 10:
            done = True

        return self.state, reward, done, {}

    def get_state(self):
        return self.state
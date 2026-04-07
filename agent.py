from env.models import Action

class BaselineAgent:
    def select_action(self, state):
        """
        Select action based on:
        - Find idle machine
        - Assign shortest job
        """

        #find idle machine
        idle_machine = None
        for m in state.machines:
            if m.status == "idle":
                idle_machine = m
                break

        #if no idle machine-> no action
        if idle_machine is None:
            return Action(machine_id=0, job_id=0)

        #if no jobs-> no action
        if len(state.job_queue) == 0:
            return Action(machine_id=0, job_id=0)

        #select job with shortest processing time
        job = min(state.job_queue, key=lambda j: j.processing_time)

        return Action(
            machine_id=idle_machine.id,
            job_id=job.id
        )
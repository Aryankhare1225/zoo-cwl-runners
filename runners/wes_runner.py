from common.base_runner import BaseRunner

class WESRunner(BaseRunner):
    def __init__(self, config):
        super().__init__(config)

    def execute(self, input_data):
        self.validate(input_data)  # Using the validate method from BaseRunner
        self.log("Executing WES Runner...")  # Using the log method from BaseRunner
        # Add WES-specific execution logic here
        return "WES Runner Execution Complete"

# at the top of each of the four files
import pytest
pytestmark = pytest.mark.integration


import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../zoo-argowf-runner")))


from zoo_argowf_runner.runner import ZooArgoWorkflowsRunner

# Dummy CWL workflow (minimal viable structure)
dummy_cwl = {
    "cwlVersion": "v1.0",
    "class": "Workflow",
    "inputs": [],
    "outputs": [],
    "steps": []
}

# Required config dictionary
conf = {
    "lenv": {
        "Identifier": "demo",
        "usid": "1234",
        "cwd": ".",
        "message": "",
    },
    "auth_env": {
        "user": "test-user"
    },
    "main": {
        "tmpPath": "/tmp"
    }
}

# Dummy processing input/output
inputs = {}
outputs = {}

# Optional dummy execution handler with mocked hooks
class DummyExecutionHandler:
    def pre_execution_hook(self):
        print("🧪 Pre-execution hook triggered")
    
    def post_execution_hook(self, **kwargs):
        print("🧪 Post-execution hook triggered")

    def handle_outputs(self, **kwargs):
        print("🧪 Handling outputs")

    def get_additional_parameters(self):
        return {}

handler = DummyExecutionHandler()

# Set required env vars
import os
os.environ["STORAGE_CLASS"] = "standard"
os.environ["DEFAULT_VOLUME_SIZE"] = "10Gi"
os.environ["DEFAULT_MAX_CORES"] = "4"
os.environ["DEFAULT_MAX_RAM"] = "4096"

# Instantiate runner
runner = ZooArgoWorkflowsRunner(
    cwl=dummy_cwl,
    conf=conf,
    inputs=inputs,
    outputs=outputs,
    execution_handler=handler
)

# Just test parameter parsing (do not call .execute)
print("✅ ZooArgoWorkflowsRunner initialized successfully")
print("Volume size:", runner.get_volume_size())
print("Max cores:", runner.get_max_cores())
print("Max RAM:", runner.get_max_ram())

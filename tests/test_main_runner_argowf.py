import os
import sys
import subprocess
import json

# 👇 Add these lines to fix import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../zoo-argowf-runner')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../zoo-calrissian-runner')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../zoo-wes-runner')))

from zoo_argowf_runner.runner import ZooArgoWorkflowsRunner



# ✅ Dummy handler that mocks the real ExecutionHandler
class DummyHandler:
    def pre_execution_hook(self): pass
    def post_execution_hook(self, **kwargs): pass
    def get_secrets(self): return None
    def get_additional_parameters(self): return {}
    def get_pod_env_vars(self): return None
    def get_pod_node_selector(self): return None
    def handle_outputs(self, **kwargs): pass
    def set_job_id(self, job_id): pass


def test_zoo_argowf_runner_initialization(tmp_path):
    # ✅ Dummy input files
    dummy_cwl = {
        "cwlVersion": "v1.0",
        "class": "Workflow",
        "id": "#main",
        "inputs": [],
        "outputs": [],
        "steps": []
    }

    dummy_conf = {
        "lenv": {
            "Identifier": "main",
            "usid": "test123",
            "message": "",
            "cwd": str(tmp_path)
        },
        "main": {
            "tmpPath": str(tmp_path)
        },
        "auth_env": {
            "user": "testuser"
        }
    }

    dummy_inputs = {}
    dummy_outputs = {"stac": {"value": None}}

    # ✅ Instantiate the runner with dummy handler
    runner = ZooArgoWorkflowsRunner(
        cwl=dummy_cwl,
        conf=dummy_conf,
        inputs=dummy_inputs,
        outputs=dummy_outputs,
        execution_handler=DummyHandler()
    )

    # ✅ Assertions (basic checks)
    assert runner.get_workflow_id() == "main"
    assert runner.get_processing_parameters() == {}
    assert runner.get_volume_size().endswith("Gi") or runner.get_volume_size().endswith("Mi")
    assert isinstance(runner.get_max_cores(), int)
    assert runner.get_max_ram().endswith("Mi")

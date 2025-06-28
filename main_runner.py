import os
import sys
import argparse
import json
from typing import Dict

# Extend sys path to access runner directories
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../zoo-calrissian-runner')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../zoo-argowf-runner')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../zoo-wes-runner')))

# Import runner classes
from zoo_calrissian_runner import ZooCalrissianRunner
from zoo_argowf_runner.runner import ZooArgoWorkflowsRunner
from zoo_wes_runner.wes_runner import ZooWESRunner



def load_json(path: str) -> Dict:
    with open(path, 'r') as f:
        return json.load(f)

def select_runner(runner_type: str):
    if runner_type == "calrissian":
        return ZooCalrissianRunner
    elif runner_type == "argowf":
        return ZooArgoWorkflowsRunner
    elif runner_type == "wes":
        return ZooWESRunner
    else:
        raise ValueError(f"Unsupported runner type: {runner_type}")

# Dummy execution handler for unit testing
class DummyHandler:
    def pre_execution_hook(self): pass
    def post_execution_hook(self, **kwargs): pass
    def get_secrets(self): return None
    def get_additional_parameters(self): return {}
    def get_pod_env_vars(self): return None
    def get_pod_node_selector(self): return None
    def handle_outputs(self, **kwargs): pass
    def set_job_id(self, job_id): pass



def main():
    parser = argparse.ArgumentParser(description="Main runner entry point for CWL workflows")
    parser.add_argument("--runner", type=str, required=True, help="Runner type: calrissian, argo, wes")
    parser.add_argument("--cwl", type=str, required=True, help="Path to CWL file (JSON)")
    parser.add_argument("--conf", type=str, required=True, help="Path to conf file (JSON)")
    parser.add_argument("--inputs", type=str, required=True, help="Path to inputs file (JSON)")
    parser.add_argument("--outputs", type=str, required=True, help="Path to outputs file (JSON)")

    args = parser.parse_args()

    RunnerClass = select_runner(args.runner)

    cwl = load_json(args.cwl)
    conf = load_json(args.conf)
    inputs = load_json(args.inputs)
    outputs = load_json(args.outputs)

    runner = RunnerClass(
        cwl=cwl,
        conf=conf,
        inputs=inputs,
        outputs=outputs,
        execution_handler=DummyHandler(),  # Replace with handler logic if needed
    )

    print(f"Initialized {args.runner} runner")
    result = runner.execute()
    print(f"Execution finished with result: {result}")


if __name__ == "__main__":
    main()

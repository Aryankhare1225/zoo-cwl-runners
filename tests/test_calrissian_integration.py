import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../zoo-calrissian-runner")))

from zoo_calrissian_runner import ZooCalrissianRunner

conf = {"lenv": {"Identifier": "demo", "usid": "1234", "cwd": "."}}
inputs = {}
outputs = {}

# Minimal valid CWL for testing (will likely need to be improved based on loader)
dummy_cwl_dict = {
    "class": "Workflow",
    "cwlVersion": "v1.0",
    "inputs": {},
    "outputs": {},
    "steps": {}
}

try:
    runner = ZooCalrissianRunner(
        cwl=dummy_cwl_dict,
        conf=conf,
        inputs=inputs,
        outputs=outputs
    )
    print("✅ ZooCalrissianRunner initialized successfully!")
except Exception as e:
    print("❌ Error during initialization:", e)


import sys
import os
import logging

# Setup logging to print INFO-level logs
logging.basicConfig(level=logging.INFO)

sys.path.append("eoepca-zoo-wes-runner/zoo_wes_runner")
sys.path.append("zoo-calrissian-runner/zoo_calrissian_runner")
sys.path.append("common")

from wes_runner import ZooWESRunner

runner = ZooWESRunner(inputs={}, conf={"lenv": {}}, outputs={})
runner.update_status(10, "Refactored status test")
runner.log_output({"hello": "world"})


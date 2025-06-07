import sys
import os
sys.path.append("zoo-argowf-runner")

from zoo_argowf_runner import runner

print("ZooStub from Argo loaded successfully!")
print("SERVICE_SUCCEEDED:", runner.zoo.SERVICE_SUCCEEDED)


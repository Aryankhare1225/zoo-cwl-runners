import sys
import os
sys.path.append("eoepca-zoo-wes-runner/zoo_wes_runner")

# Add Calrissian runner path so it can import base
sys.path.append("zoo-calrissian-runner")

import wes_runner

print("ZooStub from WES loaded successfully!")
print("SERVICE_SUCCEEDED:", wes_runner.base.zoo.SERVICE_SUCCEEDED)


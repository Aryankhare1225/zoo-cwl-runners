import sys
import os

# Add the outer folder where the runner lives
sys.path.append(os.path.abspath('zoo-calrissian-runner'))

from zoo_calrissian_runner import zoo

print("ZooStub loaded successfully!")
print("SERVICE_SUCCEEDED:", zoo.SERVICE_SUCCEEDED)


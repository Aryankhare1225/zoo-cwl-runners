import sys
import os

# Add zoo-wes-runner path to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../zoo-wes-runner")))

from zoo_wes_runner.wes_runner import ZooWESRunner

# Set required environment variables
os.environ["WES_USER"] = "dummy_user"
os.environ["WES_PASSWORD"] = "dummy_password"
os.environ["WES_URL"] = "https://dummy-url.com"

conf = {"lenv": {"Identifier": "demo", "usid": "1234", "cwd": "."}}
inputs = {}
outputs = {}

try:
    runner = ZooWESRunner(conf=conf, inputs=inputs, outputs=outputs)
    print("✅ ZooWESRunner initialized successfully!")
except Exception as e:
    print("❌ Error during WES initialization:", e)


import json
import subprocess
import os

def test_calrissian_runner_invocation(tmp_path):
    # Dummy CWL Workflow JSON
    dummy_cwl = {
  "cwlVersion": "v1.2",
  "$graph": [
    {
      "class": "Workflow",
      "id": "#main",
      "inputs": [],
      "outputs": [],
      "steps": []
    }
  ]
}


    dummy_conf = {
        "lenv": {"Identifier": "main", "usid": "test456", "message": "", "cwd": str(tmp_path)},
        "main": {"tmpPath": str(tmp_path)}
    }

    dummy_inputs = {}
    dummy_outputs = {"stac": {"value": None}}

    # Save to temporary JSON files
    cwl_path = tmp_path / "cwl.json"
    conf_path = tmp_path / "conf.json"
    inputs_path = tmp_path / "inputs.json"
    outputs_path = tmp_path / "outputs.json"

    for path, data in [
        (cwl_path, dummy_cwl),
        (conf_path, dummy_conf),
        (inputs_path, dummy_inputs),
        (outputs_path, dummy_outputs)
    ]:
        with open(path, "w") as f:
            json.dump(data, f)

    # ✅ Set environment variables for Calrissian wrapper assets
    zoo_calrissian_assets = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../zoo-calrissian-runner/assets"))

    os.environ["WRAPPER_RULES"] = os.path.join(zoo_calrissian_assets, "rules.yaml")
    os.environ["WRAPPER_MAIN"] = os.path.join(zoo_calrissian_assets, "maincwl.yaml")
    os.environ["WRAPPER_STAGE_IN"] = os.path.join(zoo_calrissian_assets, "stagein.yaml")
    os.environ["WRAPPER_STAGE_OUT"] = os.path.join(zoo_calrissian_assets, "stageout.yaml")

    # 🏃 Execute main_runner with Calrissian
    result = subprocess.run(
        [
            "python3", "../main_runner.py",
            "--runner", "calrissian",
            "--cwl", str(cwl_path),
            "--conf", str(conf_path),
            "--inputs", str(inputs_path),
            "--outputs", str(outputs_path)
        ],
        capture_output=True,
        text=True
    )

    print("STDOUT:", result.stdout)
    print("STDERR:", result.stderr)

    # ✅ Assert it initializes
    assert "Initialized calrissian runner" in result.stdout

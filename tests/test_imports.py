import importlib

def test_main_runner_import():
    mod = importlib.import_module("main_runner")
    assert mod is not None

def test_runners_import():
    for runner in ["zoo_wes_runner", "zoo_argowf_runner", "zoo_calrissian_runner"]:
        mod = importlib.import_module(runner)
        assert mod is not None

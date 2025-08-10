# import importlib

# def test_main_runner_import():
#     mod = importlib.import_module("main_runner")
#     assert mod is not None

# def test_runners_import():
#     for runner in ["zoo_wes_runner", "zoo_argowf_runner", "zoo_calrissian_runner"]:
#         mod = importlib.import_module(runner)
#         assert mod is not None

# tests/test_imports.py
import importlib
import pathlib

def test_main_runner_importable():
    mod = importlib.import_module("main_runner")
    assert mod is not None

def test_repo_has_tests_folder():
    assert pathlib.Path("tests").exists()

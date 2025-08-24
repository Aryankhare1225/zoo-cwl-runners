import importlib
import pathlib
import inspect

def test_main_runner_importable():
    mod = importlib.import_module("main_runner")
    assert hasattr(mod, "select_runner")
    assert callable(getattr(mod, "select_runner"))
    # Optional: verify main() exists and is callable
    assert hasattr(mod, "main") and inspect.isfunction(mod.main)

def test_tests_folder_exists():
    assert pathlib.Path("tests").exists()

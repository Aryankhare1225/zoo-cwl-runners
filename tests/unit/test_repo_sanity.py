import importlib
import pathlib

def test_main_runner_importable():
    assert importlib.import_module("main_runner")

def test_tests_folder_exists():
    assert pathlib.Path("tests").exists()

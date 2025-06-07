import sys
import os
import pytest


sys.path.append("common")

from base_runner import BaseRunner

class DummyRunner(BaseRunner):
    def execute(self):
        return "executed"

def test_status_update(capsys):
    runner = DummyRunner(inputs={}, conf={"lenv": {}}, outputs={})
    runner.update_status(10, "testing")
    captured = capsys.readouterr()
    assert "Status 10" in captured.out

def test_log_output(caplog):
    runner = DummyRunner(inputs={}, conf={}, outputs={})
    with caplog.at_level("INFO"):
        runner.log_output({"test": "value"})
    assert "test" in caplog.text


def test_execute():
    runner = DummyRunner(inputs={}, conf={}, outputs={})
    assert runner.execute() == "executed"


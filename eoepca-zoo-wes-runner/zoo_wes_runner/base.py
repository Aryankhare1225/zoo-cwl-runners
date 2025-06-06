"""Bases classes for Zoo runners.

These are derived here from the zoo-calrissian-runner because no generic abstract classes exist.
"""

import logging
import types


import zoo_calrissian_runner

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../common')))

from zoostub import ZooStub
zoo = ZooStub()


logger = logging.getLogger()


class BaseZooRunner(zoo_calrissian_runner.ZooCalrissianRunner):
    """Mangle the ZooCalrissianRunner to be a base class to inherit from."""

    def prepare(self):
        """Generic pre-execution which applies to all handlers."""

        logger.info("execution started")
        self.update_status(progress=2, message="starting execution")

        logger.info("wrap CWL workflow with stage-in/out steps")

        processing_parameters = {
            **self.get_processing_parameters(),
            **self.handler.get_additional_parameters(),
        }
        return types.SimpleNamespace(cwl=self.wrap(), params=processing_parameters)

    def execute(self):
        """This function should be implmented to provide job exection logic."""
        raise NotImplementedError

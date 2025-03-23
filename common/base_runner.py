from abc import ABC, abstractmethod

class BaseRunner(ABC):
    def __init__(self, config):
        self.config = config

    @abstractmethod
    def execute(self, input_data):
        """Method to be implemented by specific runners"""
        pass

    def validate(self, input_data):
        """Basic validation logic"""
        if not input_data:
            raise ValueError("Input data cannot be empty.")
        return True

    def log(self, message):
        """Common logging method"""
        print(f"[LOG]: {message}")

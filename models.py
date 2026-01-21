"""
Data models for the application.
"""

import logging

logger = logging.getLogger(__name__)


class DataModel:
    """Basic data model class."""

    def __init__(self, name: str, value: int):
        self.name = name
        self.value = value
        logger.debug(f"DataModel initialized: {self.name}")

    def __repr__(self):
        return f"DataModel(name='{self.name}', value={self.value})"

    def process(self):
        """Process the data."""
        logger.debug(f"Processing data for {self.name}")
        return f"Processing {self.name} with value {self.value}"

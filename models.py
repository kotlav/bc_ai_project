"""
Data models for the application.
"""

class DataModel:
    """Basic data model class."""

    def __init__(self, name: str, value: int):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"DataModel(name='{self.name}', value={self.value})"

    def process(self):
        """Process the data."""
        return f"Processing {self.name} with value {self.value}"

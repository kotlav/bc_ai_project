"""
Main application entry point.
"""

from models import DataModel


def main():
    """Main function."""
    print("Starting application...")

    # Create a sample model
    model = DataModel(name="sample", value=42)
    print(model)
    print(model.process())

    print("Application finished.")


if __name__ == "__main__":
    main()

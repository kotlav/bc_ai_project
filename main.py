"""
Main application entry point.
"""

import logging
from models import DataModel


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger = logging.getLogger(__name__)


def main():
    """Main function."""
    logger.info("Starting application...")

    # Create a sample model
    model = DataModel(name="sample", value=42)
    logger.info(f"Created model: {model}")
    logger.info(model.process())

    logger.info("Application finished.")


if __name__ == "__main__":
    main()

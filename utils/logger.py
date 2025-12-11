import logging

def setup_logger():
    logging.basicConfig(
        filename='agent.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    return logging.getLogger(__name__)

# Create a global logger instance
logger = setup_logger()
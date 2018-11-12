import sys
import logging

logger = logging.getLogger()

FORMATTER = logging.Formatter('[%(asctime)s][%(name)s][%(module)s][%(levelname)s] %(message)s')
HANDLER = logging.StreamHandler(stream=sys.stdout)
HANDLER.setFormatter(FORMATTER)
HANDLER.setLevel(logging.INFO)

LOGGER = logging.getLogger("tp-isae")
LOGGER.setLevel(logging.INFO)
LOGGER.handlers = [HANDLER]

import logging

logger = logging.getLogger(name="llms_selenium_atomation")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("automation.log")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
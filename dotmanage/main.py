import logging
import sys
from dotmanage import commands
from exitstatus import ExitStatus
import fire

def configure_logging():
    log_format = "%(asctime)s [%(levelname)s] %(module)s.%(funcName)s(): %(message)s"
    logging.basicConfig(level=logging.INFO, format=log_format) 

def main():
    configure_logging()

    try:
        fire.Fire(commands)
    except Exception as exception:
        logging.exception(exception)
        sys.exit(ExitStatus.failure)
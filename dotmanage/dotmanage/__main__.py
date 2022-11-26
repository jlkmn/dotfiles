import logging
import sys
from exitstatus import ExitStatus
import fire

class CmdHandler:
    def __init__(self):
        self.a = a
        
def a():
    logging.info("HI")

def configure_logging():
    log_format = "%(asctime)s [%(levelname)s] %(module)s.%(funcName)s(): %(message)s"
    logging.basicConfig(level=logging.INFO, format=log_format)
    
def main():
    configure_logging()

    try:
        fire.Fire(CmdHandler)
    except Exception as exception:
        logging.exception(exception)
        sys.exit(ExitStatus.failure)

if __name__ == '__main__':
    fire.Fire([a,b])
import logging
import logging.config
import pathlib
import json

logger = logging.getLogger("my_app")

def setup_logging():
    config_file = pathlib.Path("config.json") 
    with open(config_file) as f_in:
        config = json.load(f_in)
    logging.config.dictConfig(config)

def main():
    setup_logging()
    logger.addHandler(logging.StreamHandler())
    logger.debug("debug message", extra={"x":"hello"})
    logger.warning("warning message")
    logger.error("error message")
    logger.critical("critical message")



if __name__ == '__main__':
    main()
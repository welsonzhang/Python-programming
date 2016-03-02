import logging
import sys

logger=logging.getLogger("simple sample")
logger.setLevel(logging.DEBUG)

fh=logging.FileHandler("spam.log")
fh.setLevel(logging.DEBUG)

ch=logging.StreamHandler()
ch.setLevel(logging.ERROR)

formatter=logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
ch.setFormatter(formatter)
fh.setFormatter(formatter)

logger.addHandler(ch)
logger.addHandler(fh)

logger.debug("debug message")
logger.info("info message")
logger.warn("warn message")
logger.error("error message")
logger.critical("critical message")

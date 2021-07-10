import logging

def test_loggingDemo():

    logger=logging.getLogger(__name__)

    fileHandler=logging.FileHandler('logfile.txt')
    formatter=logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    logger.setLevel(logging.INFO)
    logger.debug("A Debug Statement Is Executed")
    logger.info("A Info Statement Is Executed")
    logger.warning("A warning Statement Is Executed")
    logger.error("A Error Statement Is Executed")
    logger.critical("A Critical Statement Is Executed")
import logging


def produce_logger(name):
    logging.basicConfig(
        level=logging.INFO,
        format='%(levelname)s: [%(asctime)s.%(msecs)03d] %(name)s:  %(message)s',
        datefmt='%d-%m-%Y %H:%M:%S'
    )
    logger = logging.getLogger(name)

    return logger

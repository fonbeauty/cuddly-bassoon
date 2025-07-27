import logging
import sys


def produce_logger(name):
    # logging.basicConfig(
    #     level=logging.INFO,
    #     format='%(levelname)s: [%(asctime)s.%(msecs)03d] %(name)s:  %(message)s',
    #     datefmt='%d-%m-%Y %H:%M:%S',
    #     handlers=[
    #         logging.StreamHandler(sys.stdout)
    #     ]
    # )
    # logger = logging.getLogger(name)
    logger = logging.getLogger('uvicorn.error')

    return logger

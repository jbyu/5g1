import logging


logger = logging.getLogger('591')
#log_formatter = logging.Formatter('%(asctime)s|%(message)s')
log_formatter = logging.Formatter('%(message)s')
#stream_handler = logging.StreamHandler()
stream_handler = logging.FileHandler('591.log', 'w', 'utf-8')
stream_handler.setFormatter(log_formatter)
logger.setLevel(logging.DEBUG)
logger.addHandler(stream_handler)

import logging

# logging.basicConfig(level=log_level)
logger = logging.getLogger()

try:
    logger.warn('2222222')
    logger.error('2222222')
    logger.warn('2222222')
    logger.warn('2222222')
    logger.warn('2222222')
except Exception as e:
    print 111111111,e
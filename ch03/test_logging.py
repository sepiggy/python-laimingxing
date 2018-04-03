import logging
import logging.config

logging.config.fileConfig('logging.config')

logging.debug('debug message')
logging.info('info message')
logging.warn('warn message')
logging.error('error message')
logging.critical('critical message')

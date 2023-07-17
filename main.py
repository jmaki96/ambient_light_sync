import logging
import time

from core.verbose_argument_parser import VerboseArgumentParser

_logger = logging.getLogger()


if __name__ == '__main__':
    start_time = time.time()
    _logger.info('hello, world!')

    end_time = time.time()
    _logger.info('Script finished in {0:.2f}s'.format(end_time-start_time))
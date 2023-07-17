import logging
import os

from core.settings import LOG_DIRECTORY, DATESTAMP

log_format = "%(asctime)s - %(name)s - %(funcName)s - %(levelname)s - %(message)s"
formatter = logging.Formatter(log_format)
_logger = logging.getLogger()
_logger.setLevel(logging.DEBUG)

# console logging
console_logging = True
if console_logging:
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    _logger.addHandler(console_handler)

# file logging
file_logging = True
debug_log_file_path = os.path.join(LOG_DIRECTORY, "debug_{0}.log".format(DATESTAMP))
if file_logging:
    debug_log_handler = logging.FileHandler(debug_log_file_path)
    debug_log_handler.setLevel(logging.DEBUG)
    debug_log_handler.setFormatter(formatter)
    _logger.addHandler(debug_log_handler)

_logger.info(f"Reports from this run under DATESTAMP: {DATESTAMP}")
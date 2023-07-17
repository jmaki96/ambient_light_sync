import argparse
import logging
import sys

_logger = logging.getLogger()


class VerboseArgumentParser(argparse.ArgumentParser):
    """ Simple wrapper for Argument Parser that adds helpful debug prints.
    """

    def parse_args(self, *args, **kwargs):
        _logger.debug(f'Called like: python3 ' + ' '.join(sys.argv))

        _args = super(VerboseArgumentParser, self).parse_args(*args, **kwargs)

        _logger.debug('Args:')
        for arg in vars(_args):
            _logger.debug(f'\t{arg} = {getattr(_args, arg)}')
        
        return _args
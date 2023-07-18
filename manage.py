"""Script which handles testing and calling the core libraries."""

import argparse
from dotenv import load_dotenv
import logging
import time

# Load environment variables before import settings file
load_dotenv()

from core.lighting.hue.client import HueClient
from core.settings import HUE_BRIDGE_ADDRESS
from core.verbose_argument_parser import VerboseArgumentParser

_logger = logging.getLogger()


def test(args: argparse.Namespace):
    """ Tests all clients to ensure that connections are valid."""

    # Test Hue client
    client = HueClient(HUE_BRIDGE_ADDRESS)
    client.test()


if __name__ == '__main__':
    start_time = time.time()
    
    parser = VerboseArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers()

    test_parser = subparsers.add_parser('test')
    test_parser.set_defaults(cmd=test)

    try:
        args = parser.parse_args()
        args.cmd(args)
    except Exception as e:
        _logger.debug('', exc_info=True)
        raise e

    end_time = time.time()
    _logger.info('Script finished in {0:.2f}s'.format(end_time-start_time))

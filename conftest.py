import os
import pytest
import logging
import contextlib
from http.client import HTTPConnection

def pytest_logger_config(logger_config):
    logger_config.add_loggers(['time_log', 'requests_log'], stdout_level='debug')
    logger_config.set_log_option_default('time_log,requests_log')


time_log = logging.getLogger('time_log')
requests_log = logging.getLogger('requests_log')


def debug_requests_on():
    """Switches on logging of the requests module."""
    HTTPConnection.debuglevel = 2

    logging.basicConfig(filename='example1.log', filemode='w', level=logging.INFO, format='%(asctime)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')
    logging.getLogger().setLevel(logging.DEBUG)

    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True


def debug_requests_off():
    '''Switches off logging of the requests module, might be some side-effects'''
    HTTPConnection.debuglevel = 0

    root_logger = logging.getLogger()
    root_logger.setLevel(logging.WARNING)
    root_logger.handlers = []
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.WARNING)
    requests_log.propagate = False


@contextlib.contextmanager
def debug_requests():
    '''Use with 'with'!'''
    debug_requests_on()
    yield
    debug_requests_off()


@pytest.yield_fixture(scope='function', autouse=False)
def session_time_log():
    time_log.info('start logging info')
    debug_requests_on()
    yield
    debug_requests_off()
    time_log.info('stop logging info')


@pytest.yield_fixture(scope='function', autouse=True)
def testcase_thing():
    requests_log.debug('Requests logging start.')
    debug_requests_on()
    yield
    requests_log.debug('Requests logging stop.')
    debug_requests_on()

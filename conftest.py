# -*- coding: utf-8 -*-
import collections
import pytest


MailOpts = collections.namedtuple(
    'MailOpts', ('url', 'username', 'password', 'to', 'body')
)


@pytest.fixture
def selenium(selenium, request):
    selenium.implicitly_wait(request.config.getoption('--wait-timeout'))
    return selenium


def pytest_addoption(parser):
    parser.addoption('--wait-timeout', default=10, help='todo')
    parser.addoption('--mailru-url', default='https://mail.ru')
    parser.addoption('--mail-username')
    parser.addoption('--mail-password')
    parser.addoption('--mail-to')
    parser.addoption('--mail-body', default='Hello from selenium')


@pytest.fixture(scope='session')
def mail_opts(request):
    return MailOpts(
        request.config.getoption('--mailru-url'),
        request.config.getoption('--mail-username'),
        request.config.getoption('--mail-password'),
        request.config.getoption('--mail-to'),
        request.config.getoption('--mail-body')
    )

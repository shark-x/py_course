# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application


fixture = None

@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    base_url = request.config.getoption("--baseURL")
    # user_name = request.config.getoption("--user")
    # password = request.config.getoption("--pass")
    if fixture is None:
        fixture = Application(browser=browser, base_url=base_url)
    else:
        if not fixture.is_valid():
            fixture = Application(browser=browser, base_url=base_url)
    # fixture.session.ensure_login(username=user_name, password=password)
    fixture.session.ensure_login(username="admin", password="secret")
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--baseURL", action="store", default="http://localhost/addressbook/")
    # parser.addoption("--user", action="store", default="admin")
    # parser.addoption("--pass", action="store")

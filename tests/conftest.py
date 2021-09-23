import os
import pytest
from selenium import webdriver
import allure
import requests


@pytest.fixture(scope="function")
def browser():
    os.environ['URL'] = 'https://uchebnik.mos.ru/'
    link = os.getenv('URL', default=None)
    browser = webdriver.Chrome()
    browser.get(link)
    print("\nstart browser..")
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.fixture(scope="function")
def browser1():
    browser = webdriver.Chrome()
    browser.get('https://dnevnik.mos.ru/webteacher/')
    print("\nstart browser..")
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        mode = 'a' if os.path.exists('failures') else 'w'
        try:
            with open('failures', mode) as f:
                if 'browser' in item.fixturenames:
                    web_driver = item.funcargs['browser']
                else:
                    print('Fail to take screen-shot')
                    return
            allure.attach(
                web_driver.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print('Fail to take screen-shot: {}'.format(e))

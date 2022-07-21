import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="--language must be es")
    parser.addoption('--browser_name', action='store', default='Chrome',
                     help='Choose browser: chrome or firefox')


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption('browser_name')
    language = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        print('\nstart chrome browser for test..')
        browser = webdriver.Chrome(options=options)
    elif browser_name == 'firefox':
        fp = webdriver.FirefoxProfile()
        fp.set_preference('intl.accept_languages', language)
        print('\nstart firefox browser for test..')
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        browser = webdriver.Chrome()
    browser.get(f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/")
    yield browser
    print("\nquit browser..")
    browser.quit()

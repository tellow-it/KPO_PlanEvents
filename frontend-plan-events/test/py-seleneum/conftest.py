import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from webdriver_manager.firefox import GeckoDriverManager


# выбор браузера при запуске тестов
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):  # request - получение данных о текущем запущенном тесте
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome("./chromedriver")
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        binary = FirefoxBinary('./geckodriver')
        browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browser_name == "edge":
        print("\nstart edge browser for test..")
        browser = webdriver.Edge()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()

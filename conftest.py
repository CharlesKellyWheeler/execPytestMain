import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


@pytest.fixture()
def driver(request):
    # Firefox driver
    options = Options()
    #options.headless = False
    options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    driver_path = r'C:\geckodriver\geckodriver.exe'
    driver = webdriver.Firefox(executable_path=driver_path, options=options)

    yield driver

    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--test-name", action="store", help="Name of the test method to execute.")
    parser.addoption("--test-data", action="store", help="Additional data to pass.")


def pytest_configure(config):
    test_name = config.getoption("--test-name")
    test_data = config.getoption("--test-data")
    if test_name:
        setattr(config.option, "test_name", test_name)
    if test_data:
        setattr(config.option, "test_data", test_data)

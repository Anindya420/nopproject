from selenium import webdriver
import pytest
@pytest.fixture()
def setup(browser):
    if browser=="chrome":
        driver = webdriver.Chrome()
        print("chrome browser")
    elif browser == "firefox":
        driver = webdriver.Firefox()
        print("firefox")
    else:
        driver = webdriver.Ie()
    return driver
def pytest_addoption(parser):  ## this will get the value from CLI/hooks
    parser.addoption("--browser")
@pytest.fixture()
def browser(request):  ## this will return the browser value to setup method
    return request.config.getoption("--browser")
#### pytest HTML report
def pytest_configure(config):
    config._metadata["Project name"] = "Nop commerce"
    config._metadata["Module NAME"] = "Customer"
    config._metadata["tester"] = "Anindya"
### its a hook for delete/modify enviornment info to HTML report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)

from pytest import fixture

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@fixture(scope= 'session')
def chrome_browser():
    # browser = webdriver.Chrome()
    # browser = webdriver.Chrome(ChromeDriverManager().install())

    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")
    service = Service(ChromeDriverManager().install())
    # options = webdriver.ChromeOptions()
    # options.add_argument("--headless")  # Run in headless mode
    driver = webdriver.Chrome(service=service, options=chrome_options)
    # driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options)
    # return driver
    return driver


def pytest_addoption(parser):
    parser.addoption("--env", 
                     action="store",
                     help="Environment to run tests against"
                     )

@fixture(scope='session')
def env(request):
    return request.config.getoption("--env")

@fixture(scope='session')
def app_config():
    cfg=Config(env)
    return cfg 
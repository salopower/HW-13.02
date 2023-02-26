import pytest
from selenium import webdriver
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="package")
def driver():
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument("--disable-extensions")
    options.add_argument('--start-maximized')
    driver = Chrome(ChromeDriverManager().install(), options=options)
    yield driver
    driver.quit()


@pytest.fixture(scope="package")
def demo_page(request):
    driver = request.getfixturevalue('driver')
    driver.get("https://demoqa.com/links")
    yield driver
    driver.quit()

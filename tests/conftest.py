# conftest.py
import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

if not os.path.exists("results"):
    os.makedirs("results")

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Send 'chrome' or 'firefox' as parameter for execution"
    )

@pytest.fixture()
def driver(request):
    browser = request.config.getoption("--browser")
    driver = ""

    if browser == "chrome":
        options = Options()

        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        }

        options.add_experimental_option("prefs", prefs)

        options.add_argument("--disable-infobars")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-notifications")
        options.add_argument("--no-default-browser-check")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--incognito")  # <- Navegación privada ayuda a evitar sugerencias y prompts
        options.add_argument("--start-maximized")

        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)

        print(f"\nSetting up: {browser} driver")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.execute_cdp_cmd("Page.setDownloadBehavior", {"behavior": "allow", "downloadPath": os.getcwd()})

    elif browser == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    driver.implicitly_wait(10)
    yield driver
    print(f"\nTear down: {browser} driver")
    driver.quit()

from datetime import datetime

import allure
import pytest
from allure_commons.types import AttachmentType
from appium import webdriver
from appium.options.android import UiAutomator2Options


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(
        item, "rep_" + rep.when, rep
    )
    return rep

# Screenshots trigger (on fail)
@pytest.fixture(autouse=True)
def log_on_failure(request):
    yield  # The code pauses here until the test is finished

    # After the test finishes, we check if it failed
    item = request.node
    # Check if the 'call' phase (the test execution) exists and failed
    if hasattr(item, "rep_call") and item.rep_call.failed:
        # Access the driver from the test class
        driver = getattr(request.cls, "driver", None)
        if driver:
            now = datetime.now().strftime("%Y-%m-%d_%H_%M_%S")
            # Attach to Allure Report
            allure.attach(
                driver.get_screenshot_as_png(),
                name=f"Screenshot_at_{now}", # Dynamic name; date + time
                attachment_type=AttachmentType.PNG
            )

@pytest.fixture(scope="class")
def test_setup(request):
    # 1. Setup - This runs BEFORE the class
    desired_caps = dict(
        deviceName='sdk_gphone64_x86_64',
        platformName='Android',
        platformVersion='16',
        automationName='UiAutomator2',
        app=r'C:\Users\ondog\Documents\praca\Automation testing\Python Appium\Udemy\app\Android\Android-NativeDemoApp-0.4.0.apk',
        appActivity='com.wdiodemoapp.MainActivity'
    )

    # desired_caps = dict(
    #     deviceName='Redmi Note 9S',
    #     udid='d3f53483',
    #     platformName='Android',
    #     platformVersion='12',
    #     automationName='UiAutomator2',
    #     app=r'C:\Users\ondog\Documents\praca\Automation testing\Python Appium\Udemy\app\Android\Android-NativeDemoApp-0.4.0.apk',
    #     appActivity='com.wdiodemoapp.MainActivity'
    # )

    capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
    driver = webdriver.Remote('http://127.0.0.1:4723', options=capabilities_options)

    # Assign driver to the class so tests can access it via self.driver
    request.cls.driver = driver

    yield driver #Everything after this runs AFTER tests.

    # 2. Teardown - This runs AFTER the class finishes
    driver.quit()
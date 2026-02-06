import allure
import pytest
from PageObjects.loginPage import LoginPage

# Run the test with html reports: pytest --html=allure-reports/report1.html --self-contained-html
# Run the test with allure reports: pytest -vs --alluredir="./allure-reports"
# To view allure reports: allure serve ./allure-reports

@pytest.mark.usefixtures("test_setup")
class TestLogin:

    def get_data(self):
        return [
            ("signup01@somemail.com", "Password01")
        ]

    @pytest.mark.parametrize("email, password", get_data(None))
    def test_appLaunch(self, email, password):
        lp = LoginPage(self.driver)

        # 1. Navigate to Sign Up
        with allure.step("Switch to Sign Up"):
            lp.navigate_to_signup()

        # 2. Fill and submit sign up
        with allure.step("Fill and submit sign up"):
            lp.fill_signup_form(email, password)
            lp.submit_signup()

        # 3. Verification: check the popup message
        with allure.step("Sign up was successful"):
            success_msg = lp.get_success_message()
            assert success_msg == "Signedd Up!", f"Expected 'Signed Up!' but got '{success_msg}'"

        # 4. Close pop up
        with allure.step("Close pop up"):
            lp.close_success_popup()
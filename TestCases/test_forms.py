import allure
import pytest
from PageObjects.formsPage import FormsPage

# Run the test with html reports: pytest --html=allure-reports/report1.html --self-contained-html
# Run the test with allure reports: pytest -vs --alluredir="./allure-reports"
# To view allure reports: allure serve ./allure-reports

@pytest.mark.usefixtures("test_setup")
class TestForms:

    def get_data(self):
        return [
            ("Testing text")
        ]

    @pytest.mark.parametrize("text", get_data(None))
    def test_appLaunch(self, text):
        fp = FormsPage(self.driver)

        # 1. Open Forms
        with allure.step("Open forms"):
            fp.open_forms_page()

        # 2. Input and verify
        with allure.step("Input text and verify"):
            fp.fill_input_field(text)
            assert fp.get_input_text() == text, "Input text did not match!"

        # 3. Switch button and verify
        with allure.step("Switch button and verify"):
            fp.toggle_switch()
            assert fp.is_switch_on(), "Switch failed to turn ON"

        # 4. Select from dropdown and verify
        with allure.step("Select from dropdown and verify"):
            select_item = "Appium is awesome"
            fp.select_dropdown_option(select_item)
            selected_item = fp.get_selected_dropdown_item()
            assert selected_item == select_item, f"Dropdown error: Expected {select_item} but found {selected_item}"

        # 5. Active button, popup closed
        with allure.step("Active button works, popup closed"):
            fp.click_active_btn()
            fp.close_popup()
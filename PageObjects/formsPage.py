import allure
from appium.webdriver.common.appiumby import AppiumBy
from PageObjects.basePage import BasePage

class FormsPage(BasePage):
    # Locators (Stored as Tuples)
    FORMS_TAB = (AppiumBy.XPATH, '//android.widget.TextView[@text="Forms"]')
    INPUT_FIELD = (AppiumBy.XPATH, '//android.widget.EditText[@content-desc="text-input"]')
    SWITCH = (AppiumBy.XPATH, '//android.widget.Switch[@content-desc="switch"]')
    DROPDOWN_BTN = (AppiumBy.XPATH, '//android.widget.TextView[@text="󰅀"]')
    # This finds the EditText that is a CHILD of the Dropdown group
    DROPDOWN_TEXT_FIELD = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="Dropdown"]//android.widget.EditText')
    ACTIVE_BTN = (AppiumBy.XPATH, '//android.widget.TextView[@text="Active"]')
    POPUP_OK = (AppiumBy.ID, 'android:id/button1')

    def open_forms_page(self):
        self.click(self.FORMS_TAB)

    def fill_input_field(self, text):
        self.type(self.INPUT_FIELD, text)

    def get_input_text(self):
        return self.get_text(self.INPUT_FIELD)

    def toggle_switch(self):
        self.click(self.SWITCH)

    def is_switch_on(self):
        return self.get_attribute(self.SWITCH, "checked") == "true"

    def select_dropdown_option(self, option_text):
        self.click(self.DROPDOWN_BTN)
        # Dynamic XPath to find the option based on the text passed
        option_locator = (AppiumBy.XPATH, f'//android.widget.CheckedTextView[@text="{option_text}"]')
        self.click(option_locator)

    def get_selected_dropdown_item(self):
        # This finds the element by its position/desc, THEN reads whatever text happens to be there
        return self.get_text(self.DROPDOWN_TEXT_FIELD)

    def click_active_btn(self):
        self.click(self.ACTIVE_BTN)

    def close_popup(self):
        self.click(self.POPUP_OK)
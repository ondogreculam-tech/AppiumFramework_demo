from appium.webdriver.common.appiumby import AppiumBy
from PageObjects.basePage import BasePage


class LoginPage(BasePage):
    # Locators (Stored as Tuples)
    LOGIN_TAB = (AppiumBy.XPATH, '//android.widget.TextView[@text="Login"]')
    SIGNUP_TAB = (AppiumBy.XPATH, '//*[@text="Sign up"]')
    EMAIL_FIELD = (AppiumBy.XPATH, '//android.widget.EditText[@content-desc="input-email"]')
    PASSWORD_FIELD = (AppiumBy.XPATH, '//android.widget.EditText[@content-desc="input-password"]')
    REPEAT_PASSWORD_FIELD = (AppiumBy.XPATH, '//android.widget.EditText[@content-desc="input-repeat-password"]')
    SIGNUP_BTN = (AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="button-SIGN UP"]')

    # Popup Locators
    POPUP_TITLE = (AppiumBy.ID, 'android:id/alertTitle')
    POPUP_OK_BTN = (AppiumBy.ID, 'android:id/button1')

    def navigate_to_signup(self):
        self.click(self.LOGIN_TAB)
        self.click(self.SIGNUP_TAB)

    def fill_signup_form(self, email, password):
        self.type(self.EMAIL_FIELD, email)
        self.type(self.PASSWORD_FIELD, password)
        self.type(self.REPEAT_PASSWORD_FIELD, password)

    def submit_signup(self):
        self.click(self.SIGNUP_BTN)

    def get_success_message(self):
        # Returns the text of the popup title (e.g., "Signed Up!")
        return self.get_text(self.POPUP_TITLE)

    def close_success_popup(self):
        self.click(self.POPUP_OK_BTN)
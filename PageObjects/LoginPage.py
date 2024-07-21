from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from TestCases.BaseClass import BaseClass


class Login(BaseClass):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Adjust the timeout as needed
        self.login_button = "//button[normalize-space()='Log in']"
        self.email_xpath = "//input[@placeholder='Enter email address']"
        self.submit_button = ("//button[@class='MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeMedium "
                              "css-1cbp9qz']")
        self.password_text = "//input[@placeholder='Enter password']"
        self.login_btn = ("//button[@class='MuiButton-root MuiButton-contained MuiButton-containedPrimary "
                          "MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButtonBase-root  css-10kazk9']")
        self.homepage_txt = "//div[@class='MuiTypography-root MuiTypography-h5 sc-eqUAAy kQprup css-11kcpxh']"

    def signUp(self):
        signup_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.login_button)))
        signup_button.click()

    def email_value(self, email):
        email_text = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.email_xpath)))
        email_text.send_keys(email)

    def submit(self):
        form_submit = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.submit_button)))
        form_submit.click()

    def password(self, enter_password):
        password_field = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.password_text)))
        password_field.send_keys(enter_password)

    def clickLogin(self):
        login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.login_btn)))
        login_button.click()

    def homepage(self):
        homepage_element = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.homepage_txt)))
        return homepage_element.is_displayed()

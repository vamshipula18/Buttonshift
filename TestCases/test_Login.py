import time

import pytest
from selenium.webdriver.common.by import By

from PageObjects.LoginPage import Login
from TestCases.BaseClass import BaseClass


class Test_Signup(BaseClass):
    def test_Login(self):
        try:
            self.driver.get("https://dev-fe.buttonshift.com/")
            time.sleep(3)
            signup_page = Login(self.driver)
            signup_page.signUp()
            signup_page.email_value("vamshepula@gmail.com")
            signup_page.submit()
            signup_page.password("Himavari@143")
            signup_page.clickLogin()
            signup_page.homepage()
        except:
            path = r"C:\Users\vamsh\PycharmProjects\ButtonShift\Screenshots"
            self.driver.save_screenshot(path+r"\error4.png")

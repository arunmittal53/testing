from selenium import webdriver
import time
import unittest
from POM_test.Pages.Home_page import HomePage
from POM_test.Pages.Login_page import LoginPage
import HtmlTestRunner


class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="/home/mittal/Desktop/testing/chromedriver")
        cls.driver.implicitly_wait(10)

    def test_login_valid(self):

        driver = self.driver

        self.driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()

    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        cls.driver.close()
        cls.driver.quit()
        print("passed")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/home/mittal/Desktop/testing/report"))


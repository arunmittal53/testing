from selenium import webdriver
import unittest
import HtmlTestRunner


class GoogleSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="../chromedriver")
        cls.driver.implicitly_wait(10)

    def test_search_hello(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("hello")
        self.driver.find_element_by_name("btnK").click()

    def test_search_name(self):
        self.driver.get("https://google.com")
        self.driver.find_element_by_name("q").send_keys("your name")
        self.driver.find_element_by_name("btnK").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("test conmpleted")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/mittal/Desktop/testing/report'))






#!/usr/bin/env python3


from selenium import webdriver
from selenium.webdriver.common.keys import Keys


user = ""
pwd = ""
driver = webdriver.Chrome(executable_path="./chromedriver")
driver.get("https://www.facebook.com")

elem = driver.find_element_by_id("email")
elem.send_keys(user)

elem = driver.find_element_by_id("pass")
elem.send_keys(pwd)

elem = driver.find_element_by_id("loginbutton")
elem.click()


#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path="./chromedriver")


# Open up a Firefox browser and navigate to web page.
driver.get("http://econpy.pythonanywhere.com/ex/001.html")

# Extract lists of "buyers" and "prices" based on xpath.
buyers = driver.find_elements_by_xpath('//div[@title="buyer-name"]')
prices = driver.find_elements_by_xpath('//span[@class="item-price"]')

# Print out all of the buyers and prices on page:
num_page_items = len(buyers)
for i in range(num_page_items):
    print(buyers[i].text + " : " + prices[i].text)

# Clean up (close browser once completed task).
driver.close()



#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json


driver = webdriver.Chrome(executable_path="./chromedriver")


# Open up a Chrome browser and navigate to web page.
driver.get("http://quotes.toscrape.com/")

# Extract lists of "quotes" and "authors" based on xpath.
text1 = driver.find_elements_by_xpath('//span[@class="text"]')
author1 = driver.find_elements_by_xpath('//small[@class="author"]')

# Store all of the quotes and authors on page:
lst = []
num_page_items = len(text1)
for i in range(num_page_items):
    d = {}
    d[author1[i].text]=text1[i].text
    lst.append(d)
print(json.dumps(lst))

# Clean up (close browser once completed task).
driver.close()



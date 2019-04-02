from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome(executable_path="./chromedriver")

driver.get("https:/web.whatsapp.com/")

# sleep time to allow user to got to selected
# contact whom want to flood with messages

sleep(5)

a = driver.switch_to.active_element

file1 = open("textfile.txt","r")

data = file1.readlines()
for x in data:
    a.send_keys(x) 

print("operation done")





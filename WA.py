from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from requests import get
from selenium.webdriver.chrome.options import Options
import time, os

from_file = open('from_file.txt', 'r+')
groups = []
group_name = from_file.read().split('\n')

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")
inp_xpath_search = "//*[@class='_2_1wd copyable-text selectable-text']"
input_box_search = WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_xpath(inp_xpath_search))
input_box_search.click()

print("\n \n \n Hello!")
print("YOUR WHATSAPP WEB IS OPEN ... ")
print("Groups from which the contacts are supposed to be extracted:   ")
print(group_name)
print("\n")
for target in group_name:
    input_box_search.send_keys(target)
    selected_target = driver.find_element_by_xpath("//span[@title='"+target+"']")
    print(selected_target)
    selected_target.click()
    inp_xpath = '//span[@class="_7yrSq _3-8er selectable-text copyable-text"]'
    time.sleep(10)
    input_box = WebDriverWait(driver,50).until(lambda driver:driver.find_element_by_xpath(inp_xpath))
print(input_box.text)
 
driver.quit()

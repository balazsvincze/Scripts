import os
from selenium import webdriver

path = os.path.abspath('..') + '\\venv\driver\chromedriver'
driver = webdriver.Chrome(path)
driver.get("http://www.irodaihuszarok.hu/")

links = driver.find_elements_by_partial_link_text('Download')
for link in links:
    link.click()

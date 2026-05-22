from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.google.com")

driver.maximize_window()
time.sleep(2)
driver.refresh()
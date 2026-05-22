from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("http://www.google.com")

driver.maximize_window()

input = driver.find_element_by_name("q")

input.send_keys("selenium")

time.sleep(50)

button = driver.find_element_by_name("FPdoLc T14B5e iThwld")

button.click()


time.sleep(35)

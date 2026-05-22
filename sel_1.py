from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.google.com")

driver.maximize_window()

search = driver.find_element(By.NAME, "q")
search.send_keys("Selenium")

time.sleep(2)

button = driver.find_element(By.NAME, "btnK")
button.click()

time.sleep(5)
driver.back()
time.sleep(2)
driver.forward()
time .sleep(2)
driver.quit()

input("Press Enter to close...")
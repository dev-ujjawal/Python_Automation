from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com")
time.sleep(2)
language_link = driver.find_element(By.LINK_TEXT, "English")
language_link.click()
driver.quit()
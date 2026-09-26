from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://text-compare.com/")
driver.maximize_window()

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

about = driver.find_element(By.LINK_TEXT, "About")
print("About link found:", about.text)

about.click()
print("About link clicked successfully!")

time.sleep(3)

driver.quit()
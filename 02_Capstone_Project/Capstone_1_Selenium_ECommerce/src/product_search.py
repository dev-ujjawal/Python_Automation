from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Start the chrome browser 
driver = webdriver.Chrome()

# Now open the tutorialNinja Homepage
driver.get("https://tutorialsninja.com/demo/")

# Locate the search box using name attribute
search_box = driver.find_element(By.NAME, "search")

# search for a product
search_box.send_keys("iphone")

# click the search button to search
driver.find_element(By.CSS_SELECTOR, "button.btn.btn-default.btn-lg").click()

#Adding a sleeping time to wait for some time to obseve the result
time.sleep(10)

# Display the result in cmd
print("Page title: ", driver.title)
print("Current URL: ", driver.current_url)

driver.quit()

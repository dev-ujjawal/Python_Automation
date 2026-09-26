from selenium import webdriver
from selenium.webdriver.common.by import By

# Start Chrome
driver = webdriver.Chrome()

# Open SauceDemo
driver.get("https://www.saucedemo.com/")

# Maximize browser
driver.maximize_window()

# Username using ID
username = driver.find_element(By.ID, "user-name")
username.send_keys("standard_user")

# Password using NAME
password = driver.find_element(By.NAME, "password")
password.send_keys("secret_sauce")

# Login button using XPATH
login_button = driver.find_element(
    By.XPATH,
    "//input[@type='submit']"
)
login_button.click()

# Verify successful login
assert "/inventory.html" in driver.current_url

print("Login successful!")
print("Current URL:", driver.current_url)

# Keep browser open for 3 seconds so it can be seen
import time
time.sleep(3)

# Close browser
driver.quit()
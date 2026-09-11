from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import time

# I will be using chrome, you can use anyone-chrome,firefox,edge etc
#start chrome browser
driver = webdriver.Chrome()

# we need to open tutorialsNinja login page
driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")

# REad login credentials from json file
with open("../test_data/test_data.json", "r") as file:
    data = json.load(file)

email = data["email"]
password = data["password"]

# Enter email address
driver.find_element(By.ID, "input-email").send_keys(email)

# Enter password
driver.find_element(By.ID, "input-password").send_keys(password)

# Click on Login button
driver.find_element(By.CSS_SELECTOR, "input[type='submit'][value='Login']").click()

# we will wait for some time so that we can observe the result.
time.sleep(5)

# verify successfull login is completed or not
print("Page title: ", driver.title)
print("Current URL: ", driver.current_url)

if "account/account" in driver.current_url:
    print("Login Successful")
else:
    print("Login Failed")

# close the browser
driver.quit()


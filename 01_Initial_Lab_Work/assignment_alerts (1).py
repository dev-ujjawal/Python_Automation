from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/javascript_alerts")

driver.maximize_window()

driver.find_element(
    By.XPATH,
    "//button[text()='Click for JS Alert']"
).click()

alert = driver.switch_to.alert

print("Alert text:", alert.text)

alert.accept()

print("Alert accepted")


driver.find_element(
    By.XPATH,
    "//button[text()='Click for JS Confirm']"
).click()

confirm = driver.switch_to.alert

print("Confirm text:", confirm.text)

confirm.dismiss()

print("Confirm dismissed")


driver.find_element(
    By.XPATH,
    "//button[text()='Click for JS Prompt']"
).click()

prompt = driver.switch_to.alert

print("Prompt text:", prompt.text)

prompt.send_keys("Selenium Test")

prompt.accept()

print("Prompt submitted")

print("Assignment 4 completed successfully!")

driver.quit()
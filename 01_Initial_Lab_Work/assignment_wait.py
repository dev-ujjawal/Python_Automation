from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Start Chrome
driver = webdriver.Chrome()

# Open the dynamic loading page
driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

# Maximize browser
driver.maximize_window()

# Find and click the Start button
start_button = driver.find_element(
    By.XPATH,
    "//button[text()='Start']"
)

start_button.click()

print("Start button clicked")
print("Waiting for the text to become visible...")

# Create an explicit wait
wait = WebDriverWait(driver, 10)

# Wait until the Hello World element is visible
message = wait.until(
    EC.visibility_of_element_located(
        (By.ID, "finish")
    )
)

# Extract the text
print("Text displayed:", message.text)

# Verify the text
assert message.text == "Hello World!"

print("Test passed successfully!")

# Close the browser
driver.quit()
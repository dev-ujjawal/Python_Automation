from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.maximize_window()

checkbox = driver.find_element(
    By.ID,
    "checkBoxOption1"
)

checkbox.click()

print("Checkbox selected:", checkbox.is_selected())

assert checkbox.is_selected()

autocomplete = driver.find_element(
    By.ID,
    "autocomplete"
)

autocomplete.send_keys("Ind")

print("Typed 'Ind' in autocomplete field")

wait = WebDriverWait(driver, 10)

suggestions = wait.until(
    EC.visibility_of_all_elements_located(
        (By.CSS_SELECTOR, ".ui-menu-item")
    )
)

for suggestion in suggestions:

    print("Suggestion:", suggestion.text)

    if suggestion.text == "India":
        suggestion.click()
        print("India selected")
        break

print(
    "Selected country:",
    autocomplete.get_attribute("value")
)

print("Assignment 3 completed successfully!")

driver.quit()
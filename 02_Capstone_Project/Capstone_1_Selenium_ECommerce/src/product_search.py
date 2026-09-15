from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

# Start the chrome browser 
driver = webdriver.Chrome()

# Now open the automation exercise Homepage
driver.get("https://automationexercise.com/")

# reading product name from json test_data
with open ("../test_data/test_data.json","r") as file:
    data = json.load(file)

product = data["product"]

# click on products
driver.find_element(By.CSS_SELECTOR, "a[href='/products']").click()

# wait untill all product page is laoded
all_products = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(
        (By.XPATH, "//h2[normalize-space()='All Products']")
    )
)

print("All product page displayed")

# Enter product name in search box
search_box = driver.find_element(By.ID, "search_product")

search_box.send_keys(product)

# click on search button
driver.find_element(By.ID, "submit_search").click()

# Wait until Searched Products heading appears
searched_products = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(
        (By.XPATH, "//h2[normalize-space()='Searched Products']")
    )
)

print("Searched product heading displayed")

# verify searched product is visible or not
product_element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "a[href='/product_details/2']")
    )
)

print("Product found: ", product)
print("Product search successful.")

driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

# start the chrome browser
driver = webdriver.Chrome()

# open the automation exercise homepage
driver.get("https://automationexercise.com/")

# read product and quantity from JSON test data
with open("../test_data/test_data.json", "r") as file:
    data = json.load(file)

product = data["product"]
quantity = str(data["quantity"])

# click product
driver.find_element(
    By.CSS_SELECTOR,
    "a[href='/products']"
).click()

# wait for the product page to load
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(
        (By.XPATH, "//h2[normalize-space()='All Products']")
    )
)

# Search for the product
search_box = driver.find_element(By.ID, "search_product")

search_box.send_keys(product)

driver.find_element(
    By.ID,
    "submit_search"    
).click()

# Wait for the search result
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(
        (By.XPATH, "//h2[normalize-space()='Searched Products']")
    )
)

print("Searched Products heading displayed.")

# Get Men Tshirt product link from search results
product_link = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR, "a[href='/product_details/2']")
    )
)

product_url = product_link.get_attribute("href")

print("Product URL:", product_url)

# Navigate to the product details page
driver.get(product_url)

# Wait for quantity field
quantity_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.ID, "quantity")
    )
)

print("Product details page loaded.")

# verify correct product
product_id = driver.find_element(
    By.ID,
    "product_id"
).get_attribute("value")


if product_id == "2":
    print("Men Tshirt product opened successfully.")
else:
    print("Incorrect product opened.")

# Change quantity to 4
quantity_input.clear()
quantity_input.send_keys(quantity)

print("Quantity set to:", quantity)

# Click Add to Cart
driver.find_element(
    By.CSS_SELECTOR,
    "button.cart"
).click()

# Handle Add to Cart popup
continue_shopping = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "button.close-modal")
    )
)

print("Add to Cart popup displayed.")

continue_shopping.click()

# Open Cart
driver.find_element(
    By.CSS_SELECTOR,
    "a[href='/view_cart']"
).click()

# Wait for cart page
WebDriverWait(driver, 10).until(
    EC.url_contains("/view_cart")
)

print("Cart opened successfully.")

driver.quit()
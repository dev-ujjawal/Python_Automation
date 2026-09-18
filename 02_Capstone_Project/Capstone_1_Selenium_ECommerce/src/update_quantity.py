from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import os

def take_screenshot(driver, filename):
    screenshot_path = os.path.join(
        "../screenshots",
        filename
    )

    driver.save_screenshot(screenshot_path)

    print("Screenshot saved:", screenshot_path)

# Start the Chrome browser
driver = webdriver.Chrome()

# Open AutomationExercise
driver.get("https://automationexercise.com/")

# Read test data from JSON
with open("../test_data/test_data.json", "r") as file:
    data = json.load(file)

product = data["product"]
new_quantity = str(data["quantity"])

# Click Products
driver.find_element(
    By.CSS_SELECTOR,
    "a[href='/products']"
).click()

# Wait for Products page
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(
        (By.XPATH, "//h2[normalize-space()='All Products']")
    )
)

print("Products page loaded.")

# Search for the product
search_box = driver.find_element(
    By.ID,
    "search_product"
)

search_box.send_keys(product)

driver.find_element(
    By.ID,
    "submit_search"
).click()

# Wait for search results
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(
        (By.XPATH, "//h2[normalize-space()='Searched Products']")
    )
)

print("Searched Products heading displayed.")

# Get product link
product_link = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR, "a[href='/product_details/2']")
    )
)

product_url = product_link.get_attribute("href")

print("Product URL:", product_url)

# Navigate to product details
driver.get(product_url)

# Wait for quantity field
quantity_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.ID, "quantity")
    )
)

print("Product details page loaded.")

# Verify correct product
product_id = driver.find_element(
    By.ID,
    "product_id"
).get_attribute("value")

if product_id == "2":
    print("Men Tshirt product opened successfully.")
else:
    print("Incorrect product opened.")

# Read current quantity
current_quantity = quantity_input.get_attribute("value")

print("Current quantity:", current_quantity)

# Update quantity
quantity_input.clear()
quantity_input.send_keys(new_quantity)

print("Updated quantity to:", new_quantity)

take_screenshot(driver, "04_quantity_updated.png")

# Add product to cart
driver.find_element(
    By.CSS_SELECTOR,
    "button.cart"
).click()

# Wait for Add to Cart popup
continue_shopping = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "button.close-modal")
    )
)

print("Add to Cart popup displayed.")

# Close popup
continue_shopping.click()

# Open Cart
driver.find_element(
    By.CSS_SELECTOR,
    "a[href='/view_cart']"
).click()

# Wait for Cart page
WebDriverWait(driver, 10).until(
    EC.url_contains("/view_cart")
)

print("Cart opened successfully.")

# Locate product row
product_row = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.ID, "product-2")
    )
)

# Read quantity from cart
cart_quantity = product_row.find_element(
    By.CSS_SELECTOR,
    "td.cart_quantity button"
).text

print("Cart quantity:", cart_quantity)

take_screenshot(driver, "04_quantity_updated-cart.png")

# Verify updated quantity
if cart_quantity == new_quantity:
    print("Quantity updated successfully.")
else:
    print("Quantity update failed.")

driver.quit()
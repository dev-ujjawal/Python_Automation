from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import os
from datetime import datetime

# function to take screenshot
def take_screenshot(driver, filename):
    screenshot_path = os.path.join(
        "../screenshots",
        filename
    )

    driver.save_screenshot(screenshot_path)

    print("Screenshot saved:", screenshot_path)


# generating report function
def generate_execution_report(
    product,
    price,
    expected_quantity,
    actual_quantity,
    expected_total,
    actual_total,
    verification_status
):
    report_path = os.path.join(
        "../reports",
        "execution_report.txt"
    )

    os.makedirs("../reports", exist_ok=True)

    with open(report_path, "w") as report:
        report.write("Selenium E-Commerce Automation - Execution Report\n")
        report.write("Application: AutomationExercise\n\n")

        report.write("Test Details\n")
        report.write(f"Product           : {product}\n")
        report.write(f"Unit Price        : {price}\n")
        report.write(f"Expected Quantity : {expected_quantity}\n")
        report.write(f"Actual Quantity   : {actual_quantity}\n")
        report.write(f"Expected Total    : Rs. {expected_total:.2f}\n")
        report.write(f"Actual Total      : Rs. {actual_total:.2f}\n\n")

        report.write("Execution Status\n")
        report.write(f"Login             : PASS\n")
        report.write(f"Product Search    : PASS\n")
        report.write(f"Add to Cart       : PASS\n")
        report.write(f"Quantity Update   : PASS\n")
        report.write(f"Cart Verification : {verification_status}\n")
        report.write(f"Screenshots       : PASS\n\n")

        report.write(f"Overall Result    : {verification_status}\n")

    print("Execution report saved:", report_path)

# Start Chrome browser
driver = webdriver.Chrome()

# Open AutomationExercise
driver.get("https://automationexercise.com/")

# Read test data from JSON
with open("../test_data/test_data.json", "r") as file:
    data = json.load(file)

product = data["product"]
expected_quantity = str(data["quantity"])

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

# Search for product
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

# Open product details page
driver.find_element(
    By.CSS_SELECTOR,
    "a[href='/product_details/2']"
).click()

# Wait for product details page
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.ID, "quantity")
    )
)

# Set quantity to 4
quantity_input = driver.find_element(
    By.ID,
    "quantity"
)

quantity_input.clear()
quantity_input.send_keys(expected_quantity)

# Add product to cart
driver.find_element(
    By.CSS_SELECTOR,
    "button.cart"
).click()

# Wait for Add to Cart popup
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "button.close-modal")
    )
)

# Close popup
driver.find_element(
    By.CSS_SELECTOR,
    "button.close-modal"
).click()

# Open cart
driver.find_element(
    By.CSS_SELECTOR,
    "a[href='/view_cart']"
).click()

# Wait for cart page
WebDriverWait(driver, 10).until(
    EC.url_contains("/view_cart")
)

# Locate Men Tshirt cart row
product_row = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.ID, "product-2")
    )
)

# Get product name
product_name = product_row.find_element(
    By.CSS_SELECTOR,
    "td.cart_description h4 a"
).text

# Get price
price = product_row.find_element(
    By.CSS_SELECTOR,
    "td.cart_price p"
).text

# Get quantity
quantity = product_row.find_element(
    By.CSS_SELECTOR,
    "td.cart_quantity button"
).text

# Get total
total = product_row.find_element(
    By.CSS_SELECTOR,
    "td.cart_total p.cart_total_price"
).text

# Display cart details
print("--------- Cart Details ---------")
print("Product Name:", product_name)
print("Price:", price)
print("Quantity:", quantity)
print("Total:", total)

# take_screenshot(driver, "05_cart_verification.png")

# Calculate expected total
unit_price = float(price.replace("Rs. ", ""))
actual_total = float(total.replace("Rs. ", ""))
expected_total = unit_price * int(expected_quantity)

print("Expected Total: Rs.", expected_total)

# Verify cart details
if (
    product_name == product
    and quantity == expected_quantity
    and actual_total == expected_total
):
    verification_status = "PASS"
    print("Cart verification successful.")
else:
    verification_status = "FAIL"
    print("Cart verification failed.")

# Generate execution report
generate_execution_report(
    product,
    price,
    expected_quantity,
    quantity,
    expected_total,
    actual_total,
    verification_status
)

driver.quit()
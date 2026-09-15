from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Start the chrome browser
driver = webdriver.Chrome()

# Open tutorialNinja homepage
driver.get("https://tutorialsninja.com/demo/")

# search for iphone
search_box = driver.find_element(By.NAME, "search")
search_box.send_keys("iphone")

# Click search
driver.find_element(
    By.CSS_SELECTOR,
    "button.btn.btn-default.btn-lg"
).click()

time.sleep(4)

# Add iphone to cart
driver.find_element(
    By.CSS_SELECTOR,
    "button[onclick^=\"cart.add('40'\"]"
).click()

time.sleep(4)

# Open shopping Cart
driver.find_element(
    By.CSS_SELECTOR,
    "a[title='Shopping Cart']"
).click()

time.sleep(4)

# Locate the product row
product_row = driver.find_element(
    By.CSS_SELECTOR,
    "table.table-bordered tbody tr"
)

# changing quantity to 2
quantity = driver.find_element(
    By.CSS_SELECTOR,
    "input[name^='quantity[']"
)

quantity.clear()
quantity.send_keys("2")

# Click on update to update the quantity
driver.find_element(
    By.CSS_SELECTOR,
    "button[data-original-title='Update']"
).click()

time.sleep(4)

# The cart page reloads after clicking Update,
# so the product row must be located again.
# locate the product row again after the page update

# product_row = driver.find_element(
#     By.XPATH,
#     "//a[normalize-space()='iPhone']/ancestor::tr"
# )

# Display all rows in the cart table
rows = driver.find_elements(
    By.CSS_SELECTOR,
    "table.table-bordered tbody tr"
)

print("Number of rows:", len(rows))

for row_index, row in enumerate(rows, start=1):
    print(f"\n--- Row {row_index} ---")

    cells = row.find_elements(By.TAG_NAME, "td")

    print("Number of cells:", len(cells))

    for cell_index, cell in enumerate(cells, start=1):
        print(f"Cell {cell_index}: {cell.text}")

product_name = product_row.find_element(
    By.CSS_SELECTOR,
    "td:nth-child(2) a"
).text

model = product_row.find_element(
    By.CSS_SELECTOR,
    "td:nth-child(3)"
).text

quantity_input = driver.find_element(
    By.CSS_SELECTOR,
    "input.form-control"
)

updated_quantity = quantity_input.get_attribute("value")

unit_price = product_row.find_element(
    By.CSS_SELECTOR,
    "td:nth-child(5)"
).text

# total = product_row.find_element(
#     By.CSS_SELECTOR,
#     "td:nth-child(6)"
# ).text

# Display all cells in the product row
cells = product_row.find_elements(By.TAG_NAME, "td")

print("Number of cells:", len(cells))

for i, cell in enumerate(cells, start=1):
    print(f"Cell {i}:", cell.text)

# Display cart details
print("---------Cart Details---------")
print("Product Name:", product_name)
print("Model:", model)
print("Quantity:", updated_quantity)
print("Unit Price:", unit_price)
# print("Total:", total)

# Verify Cart 
if product_name == "iphone" and updated_quantity == "2":
    print("Cart verification successful.")
else:
    print("Cart verification failed.")

driver.quit()

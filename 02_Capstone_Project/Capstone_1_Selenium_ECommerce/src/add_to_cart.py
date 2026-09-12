from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Start the browser
driver = webdriver.Chrome()

# Open tutorialNinja Homepage
driver.get("https://tutorialsninja.com/demo/")

# Locate the search box
search_box = driver.find_element(By.NAME, "search")

#search for any product
search_box.send_keys("iphone")

# Now click the search Button
driver.find_element(By.CSS_SELECTOR, "button.btn.btn-default.btn-lg").click()

# Wait for search results
time.sleep(2)

# Locate the iPhone Add to Cart button
add_to_cart = driver.find_element(
    By.CSS_SELECTOR,
    "button[onclick^=\"cart.add('40'\"]"
)

# Click Add to Cart
add_to_cart.click()

# Wait so the cart update can be observed
time.sleep(3)

print("Product added to cart.")

driver.quit()
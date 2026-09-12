from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Start the browser first
driver = webdriver.Chrome()

# Now we will open the tutorialNinja homapage
driver.get("https://tutorialsninja.com/demo/")

# Search for Iphone
search_box = driver.find_element(By.NAME, "search")
search_box.send_keys("iphone")

# click on search button
driver.find_element(By.CSS_SELECTOR, "button.btn.btn-default.btn-lg").click()

# wait for the result to show
time.sleep(3)

# add iphone to cart
driver.find_element(By.CSS_SELECTOR, "button[onclick^=\"cart.add('40'\"]").click()

time.sleep(3)

# Now to open shopping cart
driver.find_element(By.CSS_SELECTOR, "a[title='Shopping Cart']").click()

time.sleep(3)

# Now just locate the quantity field
quantity = driver.find_element(By.CSS_SELECTOR, "input[name^='quantity[']")

# change quantity from 1 to 2
quantity.clear()
quantity.send_keys("2")

# click on update to update the quantity
driver.find_element(By.CSS_SELECTOR, "button[data-original-title='Update']").click()

time.sleep(4)

# read the updated quantity
updated_quantity = driver.find_element(By.CSS_SELECTOR, "input[name^='quantity[']").get_attribute("value")

# print the updated quantity in terminal
print("Updated quantity: ",updated_quantity)

# verify update quantity
if (updated_quantity == "2"):
    print("Quantity updated successfully.")
else:
    print("Quantity Update failed")


# close the browser 
driver.quit()
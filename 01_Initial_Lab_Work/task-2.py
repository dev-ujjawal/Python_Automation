from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://tutorialsninja.com/demo")
first_tab = driver.current_window_handle

driver.switch_to.new_window("tab")
#2nd url
driver.get("https://testautomationpractice.blogspot.com/")

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("apple")

driver.quit()


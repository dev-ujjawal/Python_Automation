from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")

time.sleep(3)

source = driver.find_element(By.ID, "draggable")
target = driver.find_element(By.ID, "droppable")

act = ActionChains(driver)
act.drag_and_drop(source, target)
act.perform()

print("Dragged and Dropped Successfully")

time.sleep(3)

driver.quit()
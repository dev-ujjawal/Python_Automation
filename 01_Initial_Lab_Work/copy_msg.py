from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://text-compare.com/")
driver.maximize_window()

left_text = driver.find_element(By.XPATH, "(//textarea)[1]")
left_text.send_keys("Selenium Keyboard Actions")

time.sleep(2)  # pause so you can see the text typed into the left box

act = ActionChains(driver)

act.click(left_text)
act.key_down(Keys.CONTROL)
act.send_keys("a")
act.key_up(Keys.CONTROL)

act.key_down(Keys.CONTROL)
act.send_keys("c")
act.key_up(Keys.CONTROL)

right_text = driver.find_element(By.XPATH, "(//textarea)[2]")
act.click(right_text)

act.key_down(Keys.CONTROL)
act.send_keys("v")
act.key_up(Keys.CONTROL)

act.perform()

time.sleep(2)  
right_text_value = right_text.get_attribute("value")
print("Right textbox now contains:", right_text_value)

time.sleep(3)  

driver.quit()
# 1. send_keys()
# 2. key_down()
# 3. key_up()
# 4. perform()
# 5. release()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://text-compare.com/")
driver.maximize_window()

# 1. Give the page a moment to fully load (ads/scripts can delay layout)
time.sleep(2)

# 2. Some sites show a cookie-consent banner that silently eats the first
#    interaction. Try to dismiss anything obvious before proceeding.
try:
    consent_btn = WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(translate(text(),'ACEPT','acept'),'accept') or contains(text(),'Accept') or contains(text(),'Agree')]"))
    )
    consent_btn.click()
    print("Dismissed a consent banner.")
except:
    print("No consent banner found (or it wasn't blocking) — continuing.")

# 3. Wait explicitly until the textarea is actually visible and interactable
left_textbox = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//textarea[@id='inputText1']"))
)

# 4. Clear first in case there's placeholder/leftover content, then type
left_textbox.clear()
left_textbox.send_keys("Welcome to Selennium")

# 5. Verify it actually landed — this is the important debugging step
actual_value = left_textbox.get_attribute("value")
print("Textbox now contains:", repr(actual_value))

time.sleep(3)
driver.quit()
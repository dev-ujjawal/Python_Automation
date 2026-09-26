# //input[@value="radio2"]

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time

browser_name =  "chrome"

if browser_name.lower()=="chrome":
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
elif browser_name.lower()=="firefox":
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
else:
    raise Exception("Invalid browser name. Please choose either 'chrome' or 'firefox'.")

driver.get("https://testautomationpractice.blogspot.com/")

driver.maximize_window()
time.sleep(3)  # Wait for page to load

# Create WebDriverWait instance with 10 second timeout
wait = WebDriverWait(driver, 10)

# Fill form fields with explicit waits
wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='name']"))).send_keys("Yashraj Sharma")
wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='email']"))).send_keys("yashrajs118@gmail.com")
wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='phone']"))).send_keys("8100129357")

# Address field - try different possible IDs with longer wait
address_filled = False
try:
    address_elem = wait.until(EC.presence_of_element_located((By.XPATH, "//textarea[@id='textarea']")))
    address_elem.send_keys("Dum Dum")
except:
    print("textarea[@id='textarea'] not found")
    try:
        address_elem = driver.find_element(By.CSS_SELECTOR, "textarea")
        address_elem.send_keys("Dum Dum")
        address_filled = True
        print("Address filled using CSS selector")
    except:
        print("Textarea not found via CSS selector either")

wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='male']"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='sunday']"))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='monday']"))).click()

# Select country from dropdown using Select class
country_dropdown = wait.until(EC.presence_of_element_located((By.XPATH, "//select[@id='country']")))
select = Select(country_dropdown)
select.select_by_value("india")

# Select date using date picker
wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='datepicker']"))).send_keys("12/15/2026")

time.sleep(2)
driver.quit()


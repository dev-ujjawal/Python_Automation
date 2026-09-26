from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import time

browser_name =  "chrome"

if browser_name.lower()=="chrome":
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
elif browser_name.lower()=="firefox":
    driver = webdriver.Firefox(service=FirefoxService(executable_path=GeckoDriverManager().install()))
else:
    raise Exception("Invalid browser name. Please choose either 'chrome' or 'firefox'.")

driver.get("https://testautomationpractice.blogspot.com")

driver.maximize_window()
driver.find_element(By.XPATH, "//input[@id='email']").send_keys("test@example.com")
driver.find_element(By.XPATH, "//input[@id='phone']").send_keys("8100129357")
driver.find_element(By.XPATH, "//input[@id='name']").send_keys("Yashraj Sharma")

time.sleep(2)


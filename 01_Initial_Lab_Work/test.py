from selenium import webdriver

driver = webdriver.Chrome()

try:
    driver.get("https://www.google.com")
    print("Page title:", driver.title)
finally:
    driver.quit()
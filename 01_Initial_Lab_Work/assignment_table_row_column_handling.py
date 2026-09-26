from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.maximize_window()

rows = driver.find_elements(
    By.XPATH,
    "//table[@id='product']/tbody/tr"
)

print("Number of rows:", len(rows))

search_name = "Alex"

found = False

for row in rows:

    columns = row.find_elements(
        By.TAG_NAME,
        "td"
    )

    if len(columns) > 0:

        name = columns[0].text

        if name == search_name:

            print("Name found:", name)

            for i, column in enumerate(columns):

                print(
                    "Column",
                    i + 1,
                    ":",
                    column.text
                )

            found = True
            break

if found:
    print("Target row found successfully!")
else:
    print("Target name not found.")

driver.quit()
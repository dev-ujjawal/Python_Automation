from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


URL1 = "https://rahulshettyacademy.com/AutomationPractice/"
URL2 = "https://testautomationpractice.blogspot.com/"


def part_a_direct_child_checkbox():

    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get(URL1)

    wait = WebDriverWait(driver, 10)

    # Find labels that are direct children of fieldset
    labels = wait.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "fieldset > label")
        )
    )

    print("Found", len(labels), "labels via 'fieldset > label'")

    # Find checkboxes that are inside label elements
    checkboxes = driver.find_elements(
        By.CSS_SELECTOR,
        "fieldset > label > input[type='checkbox']"
    )

    print(
        "Found",
        len(checkboxes),
        "checkboxes via 'fieldset > label > input'"
    )

    for cb in checkboxes:

        cb.click()

        print(
            "Clicked",
            cb.get_attribute("id"),
            "-> checked =",
            cb.is_selected()
        )

    driver.quit()


def part_b_table_child_selector():

    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get(URL2)

    wait = WebDriverWait(driver, 10)

    # Find table rows that are direct children of tbody
    rows = wait.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "table#productTable > tbody > tr")
        )
    )

    print(
        "Found",
        len(rows),
        "rows via 'table#productTable > tbody > tr'"
    )

    # Find first row, first column
    first_id_cell = driver.find_element(
        By.CSS_SELECTOR,
        "table#productTable > tbody > tr:nth-child(1) > td:nth-child(1)"
    )

    print(
        "First row, first column text:",
        first_id_cell.text
    )

    # Find all product names
    product_names = driver.find_elements(
        By.CSS_SELECTOR,
        "table#productTable > tbody > tr > td:nth-child(2)"
    )

    print(
        "Product names:",
        [p.text for p in product_names]
    )

    driver.quit()


if __name__ == "__main__":

    part_a_direct_child_checkbox()

    part_b_table_child_selector()
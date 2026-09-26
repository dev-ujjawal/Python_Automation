import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


# Read test data from CSV file
with open("login_test_data.csv", mode="r", newline="") as file:

    reader = csv.DictReader(file)

    # Execute every test case from CSV
    for row in reader:

        test_case = row["test_case"]
        username = row["username"]
        password = row["password"]
        expected_result = row["expected_result"]

        print("\n----------------------------------------")
        print("Executing:", test_case)
        print("Username:", username)
        print("Password:", password)
        print("Expected Result:", expected_result)

        # Open Chrome
        driver = webdriver.Chrome()

        # Open login page
        driver.get("https://the-internet.herokuapp.com/login")
        driver.maximize_window()

        time.sleep(2)

        # Enter username
        username_field = driver.find_element(By.ID, "username")
        username_field.send_keys(username)

        # Enter password
        password_field = driver.find_element(By.ID, "password")
        password_field.send_keys(password)

        # Click Login
        login_button = driver.find_element(
            By.CSS_SELECTOR,
            "button[type='submit']"
        )
        login_button.click()

        time.sleep(2)

        # Get validation message
        message = driver.find_element(By.ID, "flash").text

        print("Actual Message:", message)

        # Verify expected result
        if expected_result == "success":

            if "You logged into a secure area!" in message:
                print("RESULT: PASS")
            else:
                print("RESULT: FAIL")

        else:

            if "Your username is invalid!" in message or \
               "Your password is invalid!" in message:
                print("RESULT: PASS")
            else:
                print("RESULT: FAIL")

        # Close browser
        driver.quit()

        time.sleep(1)


print("\n---------------------------------------")
print("All test cases executed successfully.")
print("---------------------------------------")
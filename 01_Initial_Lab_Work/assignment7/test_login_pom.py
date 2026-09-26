from selenium import webdriver
from pages.login_page import LoginPage


def test_valid_login():

    # Setup
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Open application
    driver.get("https://the-internet.herokuapp.com/login")

    # Create Page Object
    login_page = LoginPage(driver)

    # Perform login
    login_page.login(
        "tomsmith",
        "SuperSecretPassword!"
    )

    # Get message
    message = login_page.get_flash_message()

    # Test assertion
    assert "You logged into a secure area!" in message

    # Teardown
    driver.quit()


def test_invalid_login():

    # Setup
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Open application
    driver.get("https://the-internet.herokuapp.com/login")

    # Create Page Object
    login_page = LoginPage(driver)

    # Perform login with incorrect password
    login_page.login(
        "tomsmith",
        "wrongpassword"
    )

    # Get message
    message = login_page.get_flash_message()

    # Test assertion
    assert "Your password is invalid!" in message

    # Teardown
    driver.quit()


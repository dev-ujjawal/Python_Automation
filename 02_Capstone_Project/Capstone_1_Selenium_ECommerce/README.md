# Capstone 1 - Selenium E-Commerce Automation

## Project Overview

This project automates a basic e-commerce shopping flow using Selenium WebDriver with Python.

The automation is performed on [AutomationExercise](https://automationexercise.com/), a public practice e-commerce website.

The test scenario covers logging in, searching for a product, adding the product to the cart, updating its quantity, and verifying the final cart details.

## Objective

The objective of this project is to automate an e-commerce purchase workflow using Selenium WebDriver and Python while demonstrating:

- Launch Browser
- User login
- Product search
- Product selection
- Add to cart functionality
- Quantity update
- Cart verification
- Test data handling using JSON
- Popup handling
- Screenshot capture
- Execution report generation

## Application Under Test

**Website:** AutomationExercise

**URL:** https://automationexercise.com/

**Product Used:** Men Tshirt

**Unit Price:** Rs. 400

**Test Quantity:** 4

**Expected Cart Total:** Rs. 1600

## Technology Used

- Python
- Selenium WebDriver
- Google Chrome
- ChromeDriver
- JSON
- VS Code
- Git and GitHub

## Project Structure

```text
Capstone_1_Selenium_ECommerce/
│
├── src/
│   ├── login_test.py
│   ├── product_search.py
│   ├── add_to_cart.py
│   ├── update_quantity.py
│   └── verify_cart.py
│
├── test_data/
│   └── test_data.json
│
├── screenshots/
│   ├── 01_login_success.png
│   ├── 02_product_search.png
│   ├── 03_product_added.png
│   ├── 04_quantity_updated.png
│   ├── 04_quantity_updated-cart.png
│   └── 05_cart_verification.png
│
├── reports/
│   └── execution_report.txt
│
├── outputs/
│
├── README.md
├── requirements.txt
└── .gitignore
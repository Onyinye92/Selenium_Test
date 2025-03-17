import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com")
driver.maximize_window()

driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
driver.find_element(By.ID,"login-button").click()
time.sleep(5)

# Add 6 items to the cart
items = driver.find_elements(By.CLASS_NAME, "inventory_item")
for item in items[:6]:  # Select first 6 items
    item.find_element(By.CLASS_NAME, "btn_inventory").click()
    time.sleep(1)  # Small delay to simulate human interaction

# Go to Cart
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
time.sleep(2)

# Proceed to Checkout
driver.find_element(By.ID, "checkout").click()
time.sleep(2)

# Fill in Checkout Information
driver.find_element(By.ID, "first-name").send_keys("onyinye")
driver.find_element(By.ID, "last-name").send_keys("azunna")
driver.find_element(By.ID, "postal-code").send_keys("105102")
driver.find_element(By.ID, "continue").click()
time.sleep(3)

# Finish the Purchase
driver.find_element(By.ID, "finish").click()
time.sleep(2)

# Log out
driver.find_element(By.ID, "react-burger-menu-btn").click()
time.sleep(2)
driver.find_element(By.ID, "logout_sidebar_link").click()

# Close the browser
time.sleep(2)
driver.quit()
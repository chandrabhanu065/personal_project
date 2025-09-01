import time

from selenium import webdriver
from login_page import LoginPage

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/locatorspractice/")
login_page = LoginPage(driver)

login_page.enter_username("demo_user")
time.sleep(5)
login_page.enter_password("password123")
time.sleep(5)
login_page.click_login()
time.sleep(5)
# Assert logic can be added here
driver.quit()

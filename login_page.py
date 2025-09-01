from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_locator = (By.XPATH, ".//input[@id='inputUsername']")
        self.password_locator = (By.XPATH, ".//input[@name='inputPassword']")
        self.login_button_locator = (By.XPATH, ".//button[@type='submit']")

    def enter_username(self, username):
        self.driver.find_element(*self.username_locator).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_locator).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button_locator).click()

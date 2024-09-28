import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base



class Login_page(Base):

    url = 'https://www.777555.by/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    menu_enter = "//i[@class='icon icon-person--bold']"
    user_name = "//input[@name = 'login']"
    password = "//input[@name = 'pwd']"
    login_button = "//div[@class = 'field-btn centered']"
    link_enter = "//div[@class='tooltip']/span[1]"
    main_word = "//main[@class = 'content flx-main flx-m-12']/h1[1]"

    # Getters

    def get_menu_enter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.menu_enter)))

    def get_link_enter(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.link_enter)))

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))


    # Actions

    def click_menu_enter(self):
        self.get_menu_enter().click()
        print("Click menu enter")

    def click_link_enter(self):
        self.get_link_enter().click()
        print("Click link enter")

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("Input user name")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_login_button(self):
        self.get_login_button().click()
        print("Click login button")



    # Methods
    def authorisation(self):

        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_menu_enter()
        self.click_link_enter()
        self.input_user_name("Alex338")
        self.input_password("Alex338yxgap")
        self.click_login_button()
        self.assert_word(self.get_main_word(), 'Личный кабинет')

        time.sleep(5)
import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class Cart_delivery_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    select_pay = "//form[@method = 'post']/div[1]/label[3]/div"
    select_delivery = "//form[@method = 'post']/div[2]/label[1]/div"

    # Getters

    def get_select_pay(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_pay)))

    def get_select_delivery(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_delivery)))

    # Actions

    def click_select_pay(self):
        self.get_select_pay().click()
        print("Click select pay")

    def click_select_delivery(self):
        self.get_select_delivery().click()
        print("Click select delivery")

    # Methods
    def pay_product(self):
        self.click_select_pay()
        self.click_select_delivery()

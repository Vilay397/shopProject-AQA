import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class Client_information_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    name = "//div[@class='cart-block cart-steps form_modal']/div[3]/div[1]/input"
    telephone = "//div[@class='cart-block cart-steps form_modal']/div[3]/div[2]/input"
    e_mail = "//div[@class='cart-block cart-steps form_modal']/div[3]/div[3]/input"
    city = "//div[@class='cart-block cart-steps form_modal']/div[3]/div[4]/input"
    address = "//div[@class='cart-block cart-steps form_modal']/div[3]/div[5]/input"
    total_sum = "//div[@class='cart-total']/div[4]/span"

    # Getters

    def get_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name)))

    def get_telephone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.telephone)))

    def get_e_mail(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.e_mail)))

    def get_city(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.city)))

    def get_address(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.address)))

    def get_total_sum(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.total_sum)))


    # Actions

    def input_name(self, name):
        self.get_name().clear()
        self.get_name().send_keys(name)
        print("Input name")

    def input_telephone(self, telephone):
        self.get_telephone().clear()
        self.get_telephone().send_keys(telephone)
        print("Input telephone")

    def input_e_mail(self, e_mail):
        self.get_e_mail().clear()
        self.get_e_mail().send_keys(e_mail)
        print("Input e_mail")

    def input_city(self, city):
        self.get_city().clear()
        self.get_city().send_keys(city)
        print("Input city")

    def input_address(self, address):
        self.get_address().clear()
        self.get_address().send_keys(address)
        print("Input address")

    # Methods
    def input_information(self):
        self.get_current_url()
        self.input_name("Александра")
        self.input_telephone("291234567")
        self.input_e_mail("www.ghty@mail.com")
        self.input_city("Минск")
        self.input_address("пр-т Победителей")
        self.assert_total_summ(self.get_total_sum(), '2 055 руб. 80 коп.')

        time.sleep(5)

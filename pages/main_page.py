import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base



class Main_page(Base):

    url = 'https://www.777555.by/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators

    main_menu = "//button[@class = 'catalog-btn']"
    select_electronics = "//li[@data-name = 'Электроника']"
    select_smartfons = "//a[@href = 'https://www.777555.by/elektronika/telefoniya_i_svyaz/smartfony/']"
    filter_price_ot = "//div[@class = 'filters-group not-collapsible']/div[2]/div[1]/input"
    filter_price_do = "//div[@class = 'filters-group not-collapsible']/div[2]/div[2]/input"
    filter_model_smartfon = "//div[@class = 'filter_chek filter_chek_show']/ul/li[2]/div"
    add_product_to_cart = "//div[@class = 'catalog-item-store']/a"
    count_cart = "//div[@class='panel']/a[2]/i/span"
    click_cart = "//div[@class='panel']/a[2]/i"

    # Getters

    def get_main_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_menu)))

    def get_select_electronics(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_electronics)))

    def get_select_smartfons(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_smartfons)))

    def get_filter_price_ot(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_price_ot)))

    def get_filter_price_do(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_price_do)))

    def get_filter_model_smartfon(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_model_smartfon)))

    def get_add_product_to_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_product_to_cart)))

    def get_count_in_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.count_cart)))

    def get_click_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.click_cart)))


    # Actions


    def click_main_menu(self):
        self.get_main_menu().click()
        print("Click main menu")

    def click_select_electronics(self):
        self.get_select_electronics().click()
        print("Click select electronics")

    def click_select_smartfons(self):
        self.get_select_smartfons().click()
        print("Click select smartfons")

    def input_filter_price_ot(self,filter_price_ot):
        self.get_filter_price_ot().clear()
        self.get_filter_price_ot().send_keys(filter_price_ot)
        print("Input filter price ot")

    def input_filter_price_do(self,filter_price_do):
        self.get_filter_price_do().clear()
        self.get_filter_price_do().send_keys(filter_price_do)
        print("Input filter price do")

    def click_filter_model_smartfon(self):
        self.get_filter_model_smartfon().click()
        print("Click filter model smartfon")

    def click_add_product_to_cart(self):
        self.get_add_product_to_cart().click()
        print("Click button add product to cart")

    def click_button_cart(self):
        self.get_click_cart().click()
        print("Click button cart")


    # Methods
    def select_product(self):

        self.get_current_url()
        self.click_main_menu()
        self.click_select_electronics()
        self.click_select_smartfons()
        self.input_filter_price_ot("2000")
        self.input_filter_price_do("3500")
        self.click_filter_model_smartfon()
        time.sleep(5)
        self.click_add_product_to_cart()
        time.sleep(5)
        self.assert_count_product_in_cart(self.get_count_in_cart(), '1')
        self.click_button_cart()
        time.sleep(5)
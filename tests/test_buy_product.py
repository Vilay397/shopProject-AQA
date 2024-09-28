import time
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.cart_delivery_page import Cart_delivery_page
from pages.client_information_page import Client_information_page
from pages.login_page import Login_page
from pages.main_page import Main_page


def test_buy_product():
    driver = webdriver.Chrome()
    print("Start test")

    login = Login_page(driver)
    login.authorisation()

    mp = Main_page(driver)
    mp.select_product()

    cp = Cart_delivery_page(driver)
    cp.pay_product()

    cip = Client_information_page(driver)
    cip.input_information()

    time.sleep(10)

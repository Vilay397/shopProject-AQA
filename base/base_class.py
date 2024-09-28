
class Base():

    def __init__(self, driver):
        self.driver = driver

    """Method get current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url " + get_url)


    """Method get assert word"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good value word")

    def assert_count_product_in_cart(self, count, result):
        value_count = count.text
        assert value_count == result
        print("Good count in cart")

    def assert_total_summ(self,sum, result):
        total_summ = sum.text
        assert total_summ == result
        print("Good total summ")

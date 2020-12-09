from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Testwait:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://home.testing-studio.com/")
        self.driver.implicitly_wait(3)

    # def teardown(self):
    #     self.driver.quit()

    def test_wait(self):
        self.driver.find_element_by_xpath('//li[@title="所有分类"]').click()

        print("hello sleep")

        # def wait(x):
        #     return len(self.driver.find_elements_by_xpath('//*[@class="table-heading"]')) >= 1
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(By.XPATH,'//*[@class="table-heading"]')
        self.driver.find_element_by_xpath('//li[@title="在最近的一年，一月，一周或一天最活跃的主题"]').click()

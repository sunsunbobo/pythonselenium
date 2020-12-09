from time import sleep

from selenium import webdriver
from selenium.webdriver import TouchActions


class TestTouchAction:
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(5)

    def teardown(self):
        pass

    def test_touchaction(self):
        self.driver.get("https://www.baidu.com")
        input1 = self.driver.find_element_by_xpath('//input[@id="kw"]')
        button1 = self.driver.find_element_by_xpath('//input[@id="su"]')
        input1.send_keys("selenium测试")
        button1.click()
        action = TouchActions(self.driver)
        # action.tap(button)
        # action.perform()
        action.scroll_from_element(input1, 0, 10000).perform()
        sleep(5)

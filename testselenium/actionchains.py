from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class TestActionChains:
    def setup(self):
        self.driver = webdriver.Chrome()
        # self.driver.get("http://sahitest.com/demo/clicks.htm")
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")

    def teardown(self):
        pass

    # def test_case_click(self):
    #     element_click = self.driver.find_element_by_xpath('//input[@value="click me"]')
    #     element_dbl_click = self.driver.find_element_by_xpath('//input[@value="dbl click me"]')
    #     element_right_click = self.driver.find_element_by_xpath('//input[@value="right click me"]')
    #     action = ActionChains(self.driver)
    #     action.click(element_click)
    #     action.context_click(element_right_click)
    #     action.double_click(element_dbl_click)
    #     action.perform()

    def test_dragdrop(self):
        action = ActionChains(self.driver)
        source1 = self.driver.find_element_by_xpath('//div[@id="dragger"]')
        target1 = self.driver.find_element_by_xpath('//div[text()="Item 1"]')
        action.drag_and_drop(source1, target1)
        action.perform()
        action.click_and_hold(source1).release(target1).perform()

    def test_keys(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        input1 = self.driver.find_element_by_xpath('//input[@type="textbox"]')
        input1.click()
        actions = ActionChains(self.driver)
        actions.send_keys("username")
        actions.send_keys(Keys.SPACE)
        actions.send_keys("Tom")
        actions.send_keys(Keys.BACK_SPACE)
        actions.perform()

from selenium import webdriver

from testselenium.base import Base


class TestHandle(Base):
    def test_handle(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element_by_xpath('(//a[@name="tj_login"])[2]').click()
        print(self.driver.current_window_handle)
        self.driver.find_element_by_xpath('//a[text()="立即注册"]').click()
        print(self.driver.current_window_handle)
        window = self.driver.window_handles
        self.driver.switch_to_window(window[-1])
        self.driver.find_element_by_xpath('//input[@id="TANGRAM__PSP_4__userName"]').send_keys("username")

        self.driver.switch_to_window(window[0])
        self.driver.find_element_by_xpath('//input[@id="TANGRAM__PSP_4__userName"]').send_keys("username")

from selenium import webdriver


class TestForm:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)

    def teardown(self):
        pass

    def test_form(self):
        self.driver.get("https://testerhome.com/account/sign_in")
        self.driver.find_element_by_xpath('//*[@id="user_login"]').send_keys("123")
        self.driver.find_element_by_xpath('//*[@id="user_password"]').send_keys("password")
        self.driver.find_element_by_xpath('//*[@id="user_remember_me"]').click()
        self.driver.find_element_by_xpath('//input[@type="submit"]').click()
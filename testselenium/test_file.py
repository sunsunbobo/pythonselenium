from testselenium.base import Base


class test_file(Base):
    def test_file(self):
        self.driver.get("https://image.baidu.com")
        self.driver.find_element_by_xpath('//*[@id="sttb"]/img[2]').click()
        self.driver.find_element_by_xpath('//*[@id="stfile"]').send_keys("图片路径")

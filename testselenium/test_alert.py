from time import sleep

from selenium.webdriver import ActionChains

from testselenium.base import Base


class TestAlert(Base):
    def test_alert(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult")
        action = ActionChains(self.driver)
        source1 = self.driver.find_element_by_xpath('//*[@id="draggable"]')
        target1 = self.driver.find_element_by_xpath('//*[@id="droppable"]')
        action.drag_and_drop(source1,target1).perform()
        sleep(5)
        self.driver.switch_to.alert.accept()
        self.driver.switch_to.default_content()
        self.driver.find_element_by_xpath('//*[@id="submitBTN"]').click()


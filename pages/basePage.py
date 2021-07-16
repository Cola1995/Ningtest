from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):
    """
    pom模式基础类
    """

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *loc):
        """
        定位元素方法
        :param loc:
        :return:
        """
        WebDriverWait(self.driver, 5).until(EC.presence_of_all_elements_located(*loc))  # 等待元素可见
        return self.driver.find_element(*loc)

    def type_text(self, text, *loc):
        """
        元素send值
        :param text:
        :param loc:
        :return:
        """
        return self.driver.find_element(*loc).send_keys(text)

    def click(self, *loc):
        """
        元素点击
        :param loc:
        :return:
        """
        return self.driver.find_element(*loc).click()

    def clear(self, *loc):
        """
        元素清除数据方法
        :param loc:
        :return:
        """
        return self.driver.find_element(*loc).clear()

    def get_text(self, *loc):
        return self.driver.find_element(*loc).text

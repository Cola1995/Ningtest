import os, sys

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# sys.path.append("C:/Users/waction/PycharmProjects/Ningtest/pages")
# sys.path.extend(['C:\\Users\\waction\\PycharmProjects\\Ningtest\\pages'])
# sys.path.extend(['C:\\Users\\waction\\PycharmProjects\\Ningtest'])
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 当前程序上上一级目录，这里为pages
BASE_DIR1 = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # 项目目录
sys.path.append(BASE_DIR)  # 添加环境变量
sys.path.append(BASE_DIR1)  # 添加环境变量
import pytest
# print(sys.path)
from selenium import webdriver
import allure
from pages.numAttPage import NumAttPage
from time import sleep
from util.util import get_logger
import threading


@allure.suite("这是title")
class TestMunAtt(object):
    # def setup_class(self):
    #     # self.driver = webdriver.Chrome()     # 启动本地浏览器
    #     # 启动selenium grid
    #
    #     # self.driver.get("http://www.baidu.com")

    def setup(self):
        chrome_capabilities = {
            "browserName": "chrome",  # 浏览器名称
            "version": "",  # 操作系统版本
            "platform": "ANY",  # 平台，这里可以是windows、linux、andriod等等
            "javascriptEnabled": True,  # 是否启用js
        }
        self.driver = webdriver.Remote("http://192.168.1.43:17822/wd/hub", desired_capabilities=chrome_capabilities)
        # self.driver2 = webdriver.Remote("http://192.168.1.31:46043/wd/hub", desired_capabilities=chrome_capabilities)
        # self.loggin = get_logger()

        self.numattpage = NumAttPage(self.driver)
        # self.numattpage2 = NumAttPage(self.driver2)

    @allure.title("关闭浏览器")
    def teardown(self):
        self.numattpage.loggin.info("浏览器退出。。。")
        self.driver.close()
        self.driver.quit()

    # @allure.story("数字属性")
    # def test_num_limit(self):
    #     self.numattpage.input_user("admin")
    #     self.loggin.info("填写用户名：admin")
    #     self.numattpage.input_password("Wa12345678.")
    #     self.numattpage.login_btn_click()
    #     sleep(3)
    #     self.numattpage.go_to_create_num_att_page()
    #     self.numattpage.create_add_num_att("测试列表")
    #     self.numattpage.add_data_and_assert("数字输入框必须填写")

    def test_num_att(self):
        c1 = threading.Thread(target=self.numattpage.all, args=("admin", "Wa12345678.", "测试列表", "数字输入框必须填写"))
        # c1 = threading.Thread(target=self.numattpage.aaa)
        # sleep(3)
        # c2 = threading.Thread(target=self.numattpage2.all, args=("admin", "Wa12345678.", "测试列表", "数字输入框必须填写"))
        c_list = []
        c_list.append(c1)
        # c_list.append(c2)
        for c in c_list:
            c.start()
            c.join()




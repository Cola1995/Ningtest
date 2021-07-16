import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import allure
@allure.feature("列表数字输入框属性")
class TestNumAtt(object):
    @allure.step(title="1.登陆系统，选择自动化列表测试分组")
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://192.168.1.14:1997/#/login")
        self.driver.maximize_window()
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//input[(@placeholder="请输入账号")]')))
        self.driver.find_element_by_xpath('//input[(@placeholder="请输入账号")]').send_keys('admin')
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//input[(@placeholder="请输入密码")]')))
        self.driver.find_element_by_xpath('//input[(@placeholder="请输入密码")]').send_keys("Wa12345678.")
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//div[(@class="el-form-item__content")]/button')))
        self.driver.find_element_by_xpath('//div[(@class="el-form-item__content")]/button').click()
        sleep(3)
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, '//span[(.="自动化一级分组")]')))
        self.driver.find_element_by_xpath('//span[(.="自动化一级分组")]').click()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, '//span[(.="自动化二级分组")]')))
        self.driver.find_element_by_xpath('//span[(.="自动化二级分组")]').click()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, '//input[(@placeholder="请选择")]')))
        self.driver.find_element_by_xpath('//input[(@placeholder="请选择")]').click()
        sleep(2)
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//span[(.="自动化列表")]')))
        self.driver.find_element_by_xpath('// span[(.="自动化列表")]').click()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, '//span[(.="进入应用管理")]')))
        self.driver.find_element_by_xpath('//span[(.="进入应用管理")]').click()
        # 删除容器
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, '//div[(@class="drag_y dragHandle yqf_move")]')))
            self.driver.find_element_by_xpath('//div[(@class="drag_y dragHandle yqf_move")]').click()
            WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//i[(@class ="el-icon-delete")]')))
            self.driver.find_element_by_xpath('//i[(@class ="el-icon-delete")]').click()

            WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//div[(@class ="el-message-box__btns")]/button[2]')))
            self.driver.find_element_by_xpath('//div[(@class ="el-message-box__btns")]/button[2]').click()
        except Exception as e:
            print(e)

    def teardown(self):
        self.driver.close()
        self.driver.quit()

    @allure.step(title="2.创建表单，添加输入输入框，勾选必填提示，验证")
    def test_num_limit(self):

        WebDriverWait(self.driver,5).until(EC.presence_of_element_located((By.XPATH, '//span[(.="创建容器")]')))
        self.driver.find_element_by_xpath('//span[(.="创建容器")]').click()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, '//div[(@class ="drag_y dragHandle yqf_move")]')))
        self.driver.find_element_by_xpath('//div[(@class ="drag_y dragHandle yqf_move")]').click()

        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, '//i[(@class ="el-icon-edit")]')))
        self.driver.find_element_by_xpath('//i[(@class ="el-icon-edit")]').click()
        sleep(3)
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, '//li[(@name="addsubmenu1")]')))
        self.driver.find_element_by_xpath('//li[(@name="addsubmenu1")]').click()

        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, '//div[(@id="tab-first")]')))  # 基础设置
        self.driver.find_element_by_xpath('//div[(@id="tab-first")]').click()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, '//div/input[(@id="titleName")]')))   # 表单名称
        self.driver.find_element_by_xpath('//div/input[(@ id="titleName")]').send_keys("测试列表")
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//div[.= "表单设计"]')))
        self.driver.find_element_by_xpath('//div[.= "表单设计"]').click()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, '//div[(@class ="components-list")]/ul/li/a/span[(.="数字输入框")]')))
        self.driver.find_element_by_xpath('//div[(@class ="components-list")]/ul/li/a/span[(.="数字输入框")]').click()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, '(// main[@class ="el-main config-content"]//span[@ class ="el-checkbox__inner"])[9]'))) # 必填属性按钮
        self.driver.find_element_by_xpath('(// main[@class ="el-main config-content"]//span[@ class ="el-checkbox__inner"])[9]').click()
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//div[(.="保存")]')))
        self.driver.find_element_by_xpath('//div[(.="保存")]').click()
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//span[(.="进入应用访问")]')))
        self.driver.find_element_by_xpath('//span[(.="进入应用访问")]').click()
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '(//span[(.="添加")])[1]')))
        self.driver.find_element_by_xpath('(//span[(.="添加")])[1]').click()
        # WebDriverWait(self.driver, 5).until(
        #     EC.presence_of_element_located((By.XPATH, '(//form[@class="el-form el-form--label-left"]//input[@class ="el-input__inner"])[1]')))
        # self.driver.find_element_by_xpath('(//form[@class="el-form el-form--label-left"]//input[@class ="el-input__inner"])[1]').send_keys('')
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '(//span[(.="提 交")])[last()]')))
        self.driver.find_element_by_xpath('(//span[(.="提 交")])[last()]').click()
        WebDriverWait(self.driver, 5).until(
        EC.presence_of_element_located((By.XPATH, '//div[@class ="el-form-item__error"]')))
        print(WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class ="el-form-item__error"]'))))
        msg = self.driver.find_element_by_xpath('//div[@class ="el-form-item__error"]').text
        assert msg == "数字输入框必须填写"
        # self.driver.find_element(By.XPATH,'//div[@class ="el-form-item__error"]')

# if __name__ == '__main__':
#     pytest.main(['test_num.py'])





from selenium.webdriver.common.by import By
from pages.basePage import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import allure
from util.util import get_logger


@allure.feature("列表数字输入框属性")
class NumAttPage(BasePage):
    user_input = (By.XPATH, '//input[(@placeholder="请输入账号")]')
    password_input = (By.XPATH, '//input[(@placeholder="请输入密码")]')
    login_btn = (By.XPATH, '//div[(@class="el-form-item__content")]/button')
    first_group_ele = (By.XPATH, '//span[(.="自动化一级分组")]')
    two_group_ele = (By.XPATH, '//span[(.="自动化二级分组")]')
    three_group_choic_ele = (By.XPATH, '//input[(@placeholder="请选择")]')
    three_group_ele = (By.XPATH, '//span[(.="自动化列表")]')
    yinyong_ele = (By.XPATH, '//span[(.="进入应用管理")]')
    pane_ele = (By.XPATH, '//div[(@class="drag_y dragHandle yqf_move")]')
    dele_ronqi_ele = (By.XPATH, '//i[(@class ="el-icon-delete")]')
    confire_dele_rongqi_ele = (By.XPATH, '//div[(@class ="el-message-box__btns")]/button[2]')
    add_rinqi_ele = (By.XPATH, '//span[(.="创建容器")]')
    qianbi_ele = (By.XPATH, '//i[(@class ="el-icon-edit")]')  # 小铅笔元素
    create_menu = (By.XPATH, '//li[(@name="addsubmenu1")]')  # 创建表单元素
    tab_base_ele = (By.XPATH, '//div[(@id="tab-first")]')  # 基础设计元素
    tab_name_ele = (By.XPATH, '//div/input[(@id="titleName")]')
    tab_desin_ele = (By.XPATH, '//div[.= "表单设计"]')
    num_components_ele = (By.XPATH, '//div[(@class ="components-list")]/ul/li/a/span[(.="数字输入框")]')
    # 必填提示信息选项
    num_att_bt_radio = (By.XPATH, '(// main[@class ="el-main config-content"]//span[@ class ="el-checkbox__inner"])[9]')
    num_att_save_ele = (By.XPATH, '//div[(.="保存")]')
    yingyongfangwen_ele = (By.XPATH, '//span[(.="进入应用访问")]')
    add_data_ele = (By.XPATH, '(//span[(.="添加")])[1]')
    submit_data_ele = (By.XPATH, '(//span[(.="提 交")])[last()]')
    error_msg_ele = (By.XPATH, '//div[@class ="el-form-item__error"]')

    def __init__(self, driver):
        self.loggin = get_logger()  # 初始化loggin 方法
        BasePage.__init__(self, driver)

    @allure.step("1.跳转登录页面。")
    @allure.title("aaaaaa")
    def go_to_login_page(self):
        self.driver.get("http://192.168.1.14:1997/#/login")
        self.driver.maximize_window()

    @allure.step("2.填写用户名。")
    def input_user(self, user):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((self.user_input)))
        self.clear(*self.user_input)
        self.type_text(user, *self.user_input)

    @allure.step("3.填写密码。")
    def input_password(self, pwd):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((self.password_input)))
        self.clear(*self.password_input)
        self.type_text(pwd, *self.password_input)

    @allure.step("4.点击登陆按钮")
    def login_btn_click(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.login_btn))
        self.click(*self.login_btn)

    @allure.step("5.跳转创建添加属性页面")
    def go_to_create_num_att_page(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.first_group_ele))
        self.click(*self.first_group_ele)
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.two_group_ele))
        self.click(*self.two_group_ele)
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.three_group_choic_ele))
        self.click(*self.three_group_choic_ele)
        sleep(2)
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.three_group_ele))
        self.click(*self.three_group_ele)
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.yinyong_ele))
        self.click(*self.yinyong_ele)
        try:
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.pane_ele))
            self.click(*self.pane_ele)
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.dele_ronqi_ele))
            self.click(*self.dele_ronqi_ele)
            WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.confire_dele_rongqi_ele))
            self.click(*self.confire_dele_rongqi_ele)
        except Exception as e:
            self.loggin.info(e)

    @allure.step("6.添加必填属性")
    def create_add_num_att(self, tabname):
        WebDriverWait(self.driver, 5).until(EC.presence_of_all_elements_located(self.add_rinqi_ele))
        self.click(*self.add_rinqi_ele)
        WebDriverWait(self.driver, 5).until(EC.presence_of_all_elements_located(self.pane_ele))
        self.click(*self.pane_ele)
        WebDriverWait(self.driver, 5).until(EC.presence_of_all_elements_located(self.qianbi_ele))
        self.click(*self.qianbi_ele)
        sleep(2)
        WebDriverWait(self.driver, 5).until(EC.presence_of_all_elements_located(self.create_menu))
        self.click(*self.create_menu)
        WebDriverWait(self.driver, 5).until(EC.presence_of_all_elements_located(self.tab_base_ele))
        self.click(*self.tab_base_ele)
        WebDriverWait(self.driver, 5).until(EC.presence_of_all_elements_located(self.tab_base_ele))
        self.type_text(tabname, *self.tab_name_ele)
        WebDriverWait(self.driver, 5).until(EC.presence_of_all_elements_located(self.tab_desin_ele))
        self.click(*self.tab_desin_ele)
        WebDriverWait(self.driver, 5).until(EC.presence_of_all_elements_located(self.num_components_ele))
        self.click(*self.num_components_ele)
        WebDriverWait(self.driver, 5).until(EC.presence_of_all_elements_located(self.num_att_bt_radio))
        self.click(*self.num_att_bt_radio)
        WebDriverWait(self.driver, 5).until(EC.presence_of_all_elements_located(self.num_att_save_ele))
        self.click(*self.num_att_save_ele)

    @allure.step("7.添加数据并验证必填提示。")
    def add_data_and_assert(self, msg):

        WebDriverWait(self.driver, 5).until(EC.presence_of_all_elements_located(self.yingyongfangwen_ele))
        self.click(*self.yingyongfangwen_ele)
        WebDriverWait(self.driver, 5).until(EC.presence_of_all_elements_located(self.add_data_ele))
        self.click(*self.add_data_ele)
        WebDriverWait(self.driver, 5).until(EC.presence_of_all_elements_located(self.submit_data_ele))
        self.click(*self.submit_data_ele)
        WebDriverWait(self.driver, 5).until(EC.presence_of_all_elements_located(self.error_msg_ele))
        err_msg = self.get_text(*self.error_msg_ele)
        assert err_msg == msg

    def all(self, user, pwd, tablename, msg):

        self.go_to_login_page()
        self.loggin.info("去登陆页面")
        self.input_user(user)
        self.loggin.info("填写用户名")
        self.input_password(pwd)
        self.loggin.info("填写密码")
        self.login_btn_click()
        self.loggin.info("点击登陆按钮")
        self.go_to_create_num_att_page()
        self.loggin.info("添加属性页面")
        self.create_add_num_att(tablename)
        self.loggin.info("添加表单名称")
        self.add_data_and_assert(msg)
        self.loggin.info("添加并验证属性")

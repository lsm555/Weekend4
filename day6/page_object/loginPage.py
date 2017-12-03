from selenium.webdriver.common.by import By


class LoginPage:
    #构造方法的作用
    #实例化LoginPage对象的时候，必须要调用构造方法，
    #python 构造方法是固定写法，__init__表示 构造方法
    # 需要把driver作为参数传进来
    #便于别的属性和方法使用driver
    def __init__(self,driver):
        self.driver = driver

    title = "用户登录 - 道e坊商城 - Powered by Haidao"
    url = "http://localhost/index.php?m=user&c=public&a=login"

    #小括号表示元祖，元祖中有两个元素，第一个元素是控件的定位方式
    #第二个元素，控件定位方式的具体值
    username_input_loc = (By.ID,"username")
    passwrod_input_loc = (By.ID,"password")
    login_button_loc = (By.CLASS_NAME,"login_btn")

    def click_login_button(self):
        self.driver.find_element(*self.login_button_loc).click()

    def open(self):
        self.driver.get(self.url)

    def input_username(self,username):
        #self.driver.find_element_by_id("username").send_keys(username)
        self.driver.find_element(*self.username_input_loc).send_keys(username)
    def input_password(self,password):
        self.driver.find_element(*self.passwrod_input_loc).send_keys(password)
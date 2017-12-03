import time

from day6.myTestCase import MyTestCase
from day6.page_object.loginPage import LoginPage
from day6.page_object.personalCenterPage import PersonalCenterPage


class LoginTest(MyTestCase):
    def test_login(self):
        #现在这种测试用例可读性和维护比较困难，
        # 1、打开网页
        # self.driver.get("http://localhost/index.php?m=user&c=public&a=login")
        lp = LoginPage(self.driver)#实例化一个登录页面
        lp.open()
        # 2、输入用户名
        # self.driver.find_element(By.ID,"username").send_keys("milkway")
        lp.input_username("changcheng")
        #3、输入密码
        # self.driver.find_element(By.ID,"password").send_keys("123456")
        lp.input_password("123456")
        #4、点击登陆按钮
        # self.driver.find_element(By.CLASS_NAME,"login_btn").submit()
        lp.click_login_button()
        #5、验证跳转页面
        # expected = "我的会员中心 - 道e坊商城 - Powered by Haidao"
        # time.sleep(5)
        # self.assertIn("我的会员中心",self.driver.title)
        pcp = PersonalCenterPage(self.driver)
        time.sleep(5)
        self.assertEqual(pcp.title ,self.driver.title)






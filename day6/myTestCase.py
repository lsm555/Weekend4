import  unittest
from  selenium import  webdriver
import  time


class  MyTestCase(unittest.TestCase):
    def setUp(self):
        #打开浏览器
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # 浏览器版本与driver版本必须匹配，才可以用窗口最大化
        #self.driver.maximize_window()
    def tearDown(self):
        self.driver.quit()
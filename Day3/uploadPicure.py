import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()
driver.get("http://localhost/index.php?&m=admin&c=public&a=login")
driver.find_element_by_name("username").send_keys("admin")
driver.find_element_by_name("userpass").send_keys("password")
driver.find_element_by_name("userverify").send_keys("1234")
driver.find_element_by_class_name("Btn").click()

driver.find_element_by_link_text("商品管理").click()
driver.find_element_by_link_text("添加商品").click()
#driver.find_elements_by_name("name").send_keys("iphone X")
#有一种特殊的网页，比如左边或者上边有一个导航条，这是就要注意了
#开发很喜欢在一个页面中嵌套多个页面
#driver.find_elements_by_css_selector("body > div.content > div.install.tabs.mt10 > dl > form > dd:nth-child(1) > ul > li:nth-child(1) > input").send_keys("iphone X")
driver.switch_to.frame("mainFrame")
driver.find_element_by_name("name").send_keys("iphone X3")
driver.find_element_by_id("1").click()
driver.find_element_by_css_selector("[id='2']").click()
driver.find_element_by_id("6").click()
#driver.find_element_by_id("7").click()
#双击是特殊的元素操作，被封装到ActionChains这个类中
#java被封装到Actions这个类中
ActionChains(driver).double_click(driver.find_element_by_id("7")).perform()
#driver.find_element_by_id("jiafen").click()
brand = driver.find_element_by_name("brand_id")
Select(brand).select_by_value("1")
#driver.find_element_by_class_name("button_search").click()

#点击商品图册
driver.find_element_by_link_text("商品图册").click()
#动态的，不能用：driver.find_element_by_css_selector("#rt_rt_1bvor4q0uou8iivr1s13g1g8 > label").click()
#driver.find_element_by_css_selector("#filePicker label").click()
#label是一个纯文本的标签
#因为真正负责上传文件的页面元素是<input  type="file"
#所以我们可以直接操作这个空间，这个控件可以直接输入图片的路径
time.sleep(3)
driver.find_element_by_name("file").send_keys("D:/2017-11-25_140253.png")
#点击开始上传，同时用三个class定位
ac = ActionChains(driver)
for i in range(5):
   ac.send_keys(Keys.ARROW_RIGHT)
ac.perform()
driver.find_element_by_css_selector(".uploadBtn.state-finish.state-ready").click()
#alert这个控件不是直接弹出来的，需要时间等待
time.sleep(3)
driver.switch_to.alert.accept()
#页面太长，点击不了下面的按钮，怎么操作滚动条
ac = ActionChains(driver)
for i in range(10):
   ac.send_keys(Keys.ARROW_DOWN)
ac.perform()
brand.submit()
#driver.execute_script("window.scrollTo(200,100)")


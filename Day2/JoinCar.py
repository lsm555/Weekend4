import time
from selenium import webdriver
#firefox浏览器的45版本以下的是不需要驱动文件
#46开始的firefox浏览器，也需要把driver.exe文件放到环境变量下面
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

#隐式等待，一经设置，对后面的所有语句都有效果，所以在创建浏览器时设置一次就可以了
#implicitly 含蓄的，委婉的意思
driver.implicitly_wait(30)
#窗口最大化
driver.maximize_window()

driver.get("http://localhost/")
login_link = driver.find_element_by_link_text("登录")
driver.execute_script("arguments[0].removeAttribute('target')",login_link)
login_link.click()
driver.find_element_by_id("username").send_keys("新用户")
driver.find_element_by_id("password").send_keys("111aaa")
driver.find_element_by_id("username").submit()
#submit()用于提交form表单，form是html中的一个元素
#form表单的任何子孙节点都可以调用submit()方法
time.sleep(5)
#time.sleep到底设成几秒好，几秒都不好
#应该使用隐式等待，会自动判断网页是否加载完毕，当加载完毕立刻开始执行后续的操作
#我们需要设一个最大时间，不能让程序无限等待，一般这个时间为30s
driver.find_element_by_link_text("进入商城购物").click()
driver.find_element_by_name("keyword").send_keys("iphone")
driver.find_element_by_name("keyword").submit()
#iphone_img = "body > div.shopCon.w1100 > div.ShopboxR.fl > div.protect_con > div > " \
            # "div.shop_01-imgbox > a > img"
iphone_link = "div.shop_01-imgbox > a"
#img是标签名，表示前面得是父节点，后面的是子节点
#如果想在css中写class属性，那么前面需要加上小数点
#：nth_child(2)表示当前节点在家中排行老二，是他父亲的第二个儿子
iphone = driver.find_element_by_css_selector(iphone_link)
driver.execute_script("arguments[0].removeAttribute('target')",iphone)
iphone.click()
driver.find_element_by_id("joinCarButton").click()
driver.find_element_by_class_name("shopCar_T_span3").click()
driver.find_element_by_link_text("结算").click()
driver.find_element_by_class_name("add-address").click()
driver.find_element_by_name("address[address_name]").send_keys("新用户")
driver.find_element_by_name("address[mobile]").send_keys("18000010001")
#选择下拉框
#driver.find_elememt_by_id("add-new-area-select").find_element_by_css_selector(["value='230000'"]).click()
#因为230000是唯一的，所以可把前面的父节点去掉
# driver.find_element_by_css_selector("[value='230000']").click()

#driver.find_element_by_css_selector("#add-new-area-select")
#driver.find_element_by_xpath("//*[@id='add-new-area-select']")
# driver.find_element_by_css_selector("[value='230500']").click()
# driver.find_element_by_css_selector("[value='230506']").click()


#下拉框是一种比较特殊的网页元素，selenium专门为下拉框提供了一种定位方式
#需要把这个元素从webelement类型转换成select类型
sheng = driver.find_element_by_id("add-new-area-select")
#print(type(sheng))
#select是selenium专门为我们创建的一个类，用于操作下拉框的
#select这个类中封装了很多操作下拉框的方法
Select(sheng).select_by_value('230000')
#定位第二个下拉框
shi = driver.find_elements_by_tag_name("select")[1]
Select(shi).select_by_index(2)
qu = driver.find_elements_by_tag_name("select")[2]
Select(qu).select_by_visible_text("龙沙区")




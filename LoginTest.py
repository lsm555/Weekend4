#1.打开浏览器
from selenium import webdriver
#从  selenium   导入    网络驱动，用代码来操作浏览器
#python语言不需要加分号
#括号表示动作，才能打开
#file-settings-Editor-color and font-font 可修改字体大小
driver = webdriver.Chrome()
#2.打开登录页面
#网址必须包含协议
driver.get("http://localhost/index.php?m=user&c=public&a=login")
#3.输入用户名,首先寻找用户名的输入框
#网页上所有可见的都属于element，比如，link，按钮，下拉框
driver.find_element_by_id("username").send_keys("新用户")
#4.输入密码
driver.find_element_by_id("password").send_keys("111aaa")
#5.点击登录页面
#如果我使用一个方法，这个方法没有提示信息，那么这个方法肯定是不存在的
driver.find_element_by_class_name("login_btn").click()

#第四种元素定位方法：链接的文本信息
driver.find_elements_by_link_text("注册").click()
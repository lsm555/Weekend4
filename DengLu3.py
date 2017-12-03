#javascript是一门独立的语言，
#要想学好selenium，最重要的三件事：
#1.元素的定位：id--->name--->class
#link_text必须是链接,必须是a标签，必须得是文本
#2.元素的操作：左键单击click，发送 send_keys
#3.学好javascript
#用javascript实现窗口切换
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://localhost/")
#pycharm是用来写python语言的
#怎么在python执行javascript语言
js ='document.getElementsByClassName("site-nav-right fr")[0].' \
    'childNodes[1].removeAttribute("target")'
driver.execute_script(js)
driver.find_element_by_link_text("登录").click()
driver.find_element_by_id("username").send_keys("新用户")
driver.find_element_by_id("password").send_keys("111aaa")
driver.find_element_by_class_name("login_btn").click()
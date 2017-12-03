import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()
driver.get("http://localhost/index.php?m=user&c=public&a=login")
driver.find_element_by_id("username").send_keys("新用户")
#driver.find_element_by_id("username").send_keys(Keys.TAB)
#tab键输入密码，可避免定位密码
#ActionChains针对的是整个浏览器
#数组有固定的长度，Chains链表必须有明确的结束标志
ActionChains(driver).send_keys(Keys.TAB).send_keys("111aaa").send_keys(Keys.ENTER).perform()
driver.find_element_by_link_text("账号设置").click()
#因为之前有个图标，所以用部分链接文本定位
driver.find_element_by_partial_link_text("个人资料").click()
#clear是清空的意思，用来清除元素中原本的内容
#更好的编程习惯：在每次执行sendkeys之前，都进行一边clear操作。
#4a.真实姓名
driver.find_element_by_id("true_name").clear()
driver.find_element_by_id("true_name").send_keys("新用户啊")
#4b.性别
#css可以用多个属性组合定位一个元素
#一个元素的多个属性之前不能有空格
driver.find_element_by_css_selector('#xb[value="2"]').click()
#javascript是一个单独语言，和python的语法不一样，不能直接写在pycharm中执行
#js = 'document.getElementById("date").removeAttribute("readonly")'
#driver.execute_script(js)
#driver.find_element_by_id("date").clear()
#driver.find_element_by_id("date").send_keys("2001-11-21")
#用aarguments改写上面输入：用selenium的定位方式，定位元素之后，对元素执行javascript脚本，删除readonly属性
date = driver.find_element_by_id("date")
driver.execute_script('arguments[0].removeAttribute("readonly")',date)
date.clear()
date.send_keys("1980-11-21")
#用selenium调用javascript一共有两个关键字：1、arguments[0]：表示用一部分python语言代替一部分javascript，好处是有时selenium定位比较容易

#2、return把javascript执行的结果返回给python语言，好处：有时selenium定位不到的元素可以用javascript定位
#date = driver.execute_script("return document.getElementById('date')")
#这句话==date = driver.find_element_by_id("date")
#date.click()
#类名需要大写，或者两个单词之间没有空格，下划线，单词的首字母大写，或者首字母缩写词可以大写
#解开注释，ctrl+斜杠
driver.find_element_by_id("qq").clear()
driver.find_element_by_id("qq").send_keys("12345678")
driver.find_element_by_class_name("btn4").click()
#右键检查不了html代码的弹出框，叫做alert，有单独的方法来处理
time.sleep(3)
#alert控件不是html代码生成的，所以implivitly_wait飞这个空间不管用
#所以就算上面写了implicitly_wait，这个time_sleep（）方法不能省
#切换到alert的方法，和切换窗口的方法类似
#alert 弹出框，accept接受 ，同意，确定 dismiss拒绝 取消
driver.switch_to.alert.accept()
#driver.switch_to.alert.dismiss()

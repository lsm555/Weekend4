from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://localhost/")
driver.find_element_by_link_text("注册").click()


#窗口切换：把selenium切换到新的窗口工作
cwh = driver.current_window_handle #浏览器当前窗口的句柄，没有括号说明不是方法，是一个属性
print(cwh)
#selenium只提供了selenium工作的窗口的名字，并没有提供第二个窗口的名中，得自己求
whs = driver.window_handles #浏览器中所有的窗口句柄
#for关键字（类型名 变量名 ：数组）{}  ---java
#for关键字 _ 集合中的某个元素 in关键字 数组/集合
#item表示whs中的一个元素，每次循环取一个值，循环结束，
#whs中的每个元素被遍历一次
#python语法：遇到冒号，下一行，肯定要空4个空格
for item in whs:
    if item == cwh:
        #pass
        driver.close()  #关闭当前标签
    else:
        driver.switch_to.window(item)
driver.find_element_by_name("username").send_keys("新用户2")
driver.find_element_by_name("password").send_keys("111aaa")
driver.find_element_by_name("userpassword2").send_keys("111aaa")
driver.find_element_by_name("mobile_phone").send_keys("18000010003")
driver.find_element_by_name("email").send_keys("12345@163.com")
driver.find_element_by_class_name("reg_btn").click()





from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://localhost/index.php?m=user&c=public&a=reg")
driver.find_element_by_name("username").send_keys("新用户1")
driver.find_element_by_name("password").send_keys("111aaa")
driver.find_element_by_name("userpassword2").send_keys("111aaa")
driver.find_element_by_name("mobile_phone").send_keys("18000010002")
driver.find_element_by_name("email").send_keys("1234@163.com")
driver.find_element_by_class_name("reg_btn").click()

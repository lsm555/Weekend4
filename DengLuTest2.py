from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://localhost/")
driver.find_element_by_link_text("登录").click()
#从浏览器中的所有窗口中，排除第一个窗口
#把selenium切换到第二个窗口
cwh = driver.current_window_handle
whs = driver.window_handles
for item in  driver.window_handles: #item表示集合中的一个元素
    if item == cwh:
        driver.close()
    else:
        driver.switch_to.window(item)

driver.find_element_by_id("username").send_keys("新用户2")


from selenium import webdriver

# 创建浏览器对象
driver = webdriver.PhantomJS()
driver.get('http://www.qiushibaike.com/text/')
# 查找单个节点
serOne = driver.find_element_by_class_name('content')
print(serOne)

# 查找多个节点
serMany = driver.find_elements_by_class_name('content')
print(serMany)
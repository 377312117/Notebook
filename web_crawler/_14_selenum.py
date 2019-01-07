
# 导入selenium的webdraver
from selenium import webdriver


# 创建phantomjs对象
# webdriver.PhantomJS(executable_path='/usr/local/bin/phantomjs')
# driver = webdriver.Chrome()
# python需要对应版本
driver = webdriver.PhantomJS()
# 发请求
driver.get('http://www.baidu.com/')
# 获取网页源码
print(driver.page_source)
# 获取网页截屏
driver.save_screenshot('baidu.png')
# 关闭浏览器
driver.quit()

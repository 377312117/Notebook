# 导入selenium的webdraver
from selenium import webdriver
import time

# driver = webdriver.PhantomJS()
driver = webdriver.PhantomJS(service_args=['--ignore-ssl-errors=true', '--ssl-protocol=TLSv1'])
# 打开百度
driver.get('http://www.baidu.com/')

# 找到搜索框
driver.find_element_by_id('kw').send_keys('美女')

# 找到百度一下,点击一下
driver.find_element_by_id('su').click()


# 截图
time.sleep(5)
driver.save_screenshot('meinv.png')

# 关闭浏览器
driver.quit()
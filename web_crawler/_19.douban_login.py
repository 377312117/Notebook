from selenium import webdriver
import time

# 创建浏览器对象
driver = webdriver.PhantomJS()

# driver = webdriver.ChromeOptions()
# driver.set_headless()
driver.get('http://www.douban.com/')

# 查找输入框并输入
uname = driver.find_element_by_name('form_email')
uname.send_keys('15307553614')
pwd = driver.find_element_by_name('form_password')
pwd.send_keys('zzx15216241612')
driver.save_screenshot('yzm.png')
yzm=input('请输入验证码:')
if yzm:
    driver.find_element_by_name('captcha_image').send_keys(yzm)
# 模拟点击登录
driver.find_element_by_class_name('bn_submit').click()
# 屏幕截图
time.sleep(5)
driver.save_screenshot('chenggong.png')
# 发请求,获响应



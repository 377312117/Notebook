from selenium import webdriver
import time

# 创建浏览器对象
driver = webdriver.PhantomJS()
# 访问京东首页
driver.get('http://www.jd.com/')
# 找到搜索框按钮,接收终端输入,发送到搜索框
text = driver.find_element_by_id('key')
key = input('请输入要搜索的内容:')
text.send_keys(key)
# 点击搜索按钮
button = driver.find_element_by_class_name('button')
button.click()

time.sleep(5)
# 提取数据,分析数据
rList = driver.find_elements_by_xpath('//div[@id="J_goodsList"]//li')
# print(rList)
for r in rList:
    # print(r.text)
    contentList = r.text.split('\n')
    price = contentList[0]
    name = contentList[1]
    status = contentList[2]
    price = contentList[3]
    market = contentList[4]
    print(price)
    print(name)
    print(status)
    print(price)
    print(market)
    print('*'*30)

while True:
    # 执行脚本,进度条
    pass   


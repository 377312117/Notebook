import requests

from bs4 import BeautifulSoup

import pymongo

import time


class LianjiaSpider:
    def __init__(self):
        self.baseurl = 'https://bj.lianjia.com/ershoufang/pg'
        self.headers = {'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
        self.conn = pymongo.MongoClient('localhost',27017)
        # 库对象
        self.db = self.conn['Lianjia']
        # 集合对象
        self.myset = self.db['houseInfo']


    def getPage(self,url):
        res = requests.get(url,headers=self.headers)
        res.encoding = 'utf-8'
        html = res.text 
        print(html)
        self.parsePage(html)

    # 解析并保存页面
    def parsePage(self,html):
        # 创建解析对象
        soup = BeautifulSoup(html,'lxml')
        # 解析对象的find_all()方法获取每个房源信息
        rList = soup.find_all('li',attrs={"class":'clear LOGCLICKDATA'})
        for r in rList:
            # #########################
            # houseInfo节点
            Info = r.find('div',attrs={'class':"houseInfo"}).get_text().split('/')
            positionInfo = r.find('div',attrs={'class':"positionInfo"}).get_text().split('/')
            # 小区名称
            name=Info[0]
            # 户型
            huxing = Info[1]
            # 面积
            area = Info[2]
            # louceng
            louceng=positionInfo[0]
            # 年份
            year = positionInfo[1]
            # 地址
            address = positionInfo[2]
            # 总价
            totalPrice=r.find('div',attrs={
                'class':'totalPrice'
            }).get_text()
            # 单价
            unitPrice=r.find('div',attrs={
                'class':'unitPrice'
            }).get_text()
            d = {
                '名称':name,
                '户型':huxing,
                '面积':area,
                '楼层':louceng,
                '年份':year,
                '地址':address,
                '总价':totalPrice,
                '单价':unitPrice,
            }
            self.myset.insert_one(d)

    def workOn(self):
        n = int(input('请输入页数:'))
        for pg in range(1,n+1):
            # 拼接url
            url= self.baseurl+str(pg)+'/'
            self.getPage(url)
            time.sleep(0.5)
            print(f'第{pg}页爬取成功')

if __name__ == "__main__":
    spider = LianjiaSpider()
    spider.workOn()
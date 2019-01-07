import requests

from multiprocessing import Queue

from threading import Thread

from lxml import etree

import time 

class XiaomiSpider:
    def __init__(self, *args, **kwargs):
        self.baseurl = 'http://app.mi.com/category/12#page='
        self.mainurl = 'http://app.mi.com'
        self.headers = {'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
        # Url队列
        self.urlQueue=Queue()
        # 解析队列
        self.parseQueue=Queue()
    
    # URL入队列
    def getUrl(self):
        for page in range(20):
            url = self.baseurl+str(page)
            self.urlQueue.put(url)

    
    # 采集线程函数,get出URL发请求,把html给解析队列
    def getHtml(self):
        while True:
            # 先判断队列是否为空
            if self.urlQueue.empty():
                # 5秒没get数据,抛出超时异常
                url = self.urlQueue.get(block=True,timeout=0.5)
                # 三步走
                res = requests.get(url,headers=self.headers)
                res.encoding='utf-8'
                html=res.text 
                # 把html放到解析队列里去
                self.parseQueue.put(html)
            else:
                break

    
    # 解析线程函数,get出html源码,提取并处理数据
    def getData(self):
        while True:
            if not self.parseQueue.empty():
                html = self.parseQueue.get()
                # 创建解析对象,调用xpath
                parseHtml = etree.HTML(html)
                baseList=parseHtml.xpath('//ul[@id="all-applist"]//li')
                for base in baseList:
                    # 应用名称
                    name = base.xpath('./h5/a/text()')[0]
                    # 应用链接
                    link = self.mainurl + base.xpath('./h5/a/@href')[0]
                    # 
                    d = {
                        '分类':'学习教育',
                        '名称':name,
                        '链接':link,
                    }
                    with open('xiaomi.json','a',encoding='utf-8') as f:
                        f.write(str(d)+'\n')
            else:
                break

    # 主函数
    def workOn(self):
        # url先入队列
        self.getUrl()

        tList=[]

        # 采集线程
        for i in  range(10):
            t = Thread(target=self.getHtml())
            t2 = Thread(target=self.getData())
            tList.append(t)
            tList.append(t2)
            t.start()
            t2.start()
        # 统一回收采集线程
        for i  in tList:
            i.join()



if __name__ == "__main__":
    start = time.time()
    spider = XiaomiSpider()
    spider.workOn()
    end = time.time()
    print(f'执行时间:{end-start}')


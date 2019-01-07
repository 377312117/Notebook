import urllib.request
import urllib.parse
import ssl
import re 
import csv 
from pymongo import *
from pymysql import *

# 处理警告模块
import warnings


class MaoyanSpyder:
    def __init__(self,baseurl,headers):
        self.baseurl = baseurl
        self.headers = headers
        self.offset = 0

    # 获取页面
    def getPage(self,url):
        req = urllib.request.Request(url,headers=self.headers)
        res = urllib.request.urlopen(req)
        html = res.read().decode('utf-8')
        self.parsePage(html)


    # 解析页面
    def parsePage(self,html):
        p = re.compile('<div class="movie-item-info">.*?title="(.*?)".*?class="star">(.*?)</p>.*?releasetime">(.*?)</p>',re.S)
        rlist = p.findall(html)
        # 获取一个元组组成的列表集合
        self.writeMysql(rlist)
        
    # 保存数据到csv文件
    def writePage(self,rlist):
        for r in rlist:
            chlst = [r[0].strip(),r[1].strip(),r[2].strip()[5:].strip()]
            with open('maoyan.csv','a',newline='',encoding='utf-8') as f:
                # 创建写入对象
                writer = csv.writer(f)
                # 利用写入对象的writerow()写入csv文件
                writer.writerow(chlst)
                print('写入成功')
    
    # 保存进芒果数据库
    def writeMongoDB(self,rlist):
        # 创建数据库连接对象
        conn = MongoClient('localhost',27017)
        # 创建库对象
        db = conn['spiderdb']
        # 创建集合对象
        myset = db['maoyanspider']
        # 插入文档
        for r in rlist:
            myset.insert_one({'name':r[0].strip(),'actor':r[1].strip()[3:].strip(),'release_times':r[2].strip()[5:].strip()})
            print('write succses')

    # 保存进mysql数据库
    def writeMysql(self,rlist):
        # 过滤警告
        warnings.filterwarnings('ignore')
        # 创建数据库连接对象
        db = connect('localhost','root','123456',charset='utf8')
        # 创建游标对象
        cursor = db.cursor()
        # 利用游标对象的execute()方法执行命令
        cdb = 'create database if not exists spiderdb charset utf8'
        cursor.execute(cdb)
        udb = 'use spiderdb'
        cursor.execute(udb)
        ctab = 'create table if not exists maoyanspider(id int primary key auto_increment,name varchar(50),actor varchar(120),release_times varchar(50))'
        cursor.execute(ctab)
        # 在t1集合中插入1条文档
        for r in rlist:
            cursor.execute(f'insert into maoyanspider(name,actor,release_times) values("{r[0].strip()}","{r[1].strip()[3:].strip()}","{r[2].strip()[5:].strip()}")')
            print('write succses')
        # 提交
        db.commit()
        # 关闭游标和游标对象
        cursor.close()
        db.close()
        

        

    
    # 主函数
    def workOn(self):
        while True:
            c = input('爬取是否继续(y/n):')
            if c.strip().lower() == 'y':
                url = self.baseurl +str(self.offset)
                print(url)
                self.getPage(url)
                self.offset +=10
            else:
                print('爬取结束')
                break
                



if __name__ == '__main__':
    ssl._create_default_https_context = ssl._create_unverified_context
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    baseurl = 'https://maoyan.com/board/4?offset='
    spider = MaoyanSpyder(baseurl,headers)
    spider.workOn()


# 正则表达式
# <div class="movie-item-info">.*?title=".*?".*?class="star">(.*?)</p>.*?releasetime">(.*?)</p>
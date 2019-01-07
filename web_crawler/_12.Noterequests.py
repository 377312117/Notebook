import ssl
import re 
from pymysql import *
import requests
import warnings


class NoteSpyder:
    def __init__(self,baseurl,headers):
        self.baseurl = baseurl
        self.headers = headers
        # 创建数据库连接对象y
        
        self.db = connect('localhost','root','123456',charset='utf8')
        # 创建游标对象
        self.cursor = self.db.cursor()
        # web验证对象
        self.auth = ('tarenacode','code_2013')

    # 获取页面
    def getPage(self):
        res = requests.get(self.baseurl,auth=self.auth,headers=self.headers)
        res.encoding = 'utf-8'
        html = res.text
        self.parsePage(html)


    # 解析页面
    def parsePage(self,html):
        p = re.compile('<a href="(.*?)/.*?</a>',re.S)
        rlist = p.findall(html)
        # 获取一个元组组成的列表集合
        self.writeMysql(rlist)
        

    # 保存进mysql数据库
    def writeMysql(self,rlist):
        # 过滤警告
        warnings.filterwarnings('ignore')
        # 利用游标对象的execute()方法执行命令
        cdb = 'create database if not exists spiderdb charset utf8'
        self.cursor.execute(cdb)
        udb = 'use spiderdb'
        self.cursor.execute(udb)
        ctab = 'create table if not exists notespider(id int primary key auto_increment,name varchar(50))'
        self.cursor.execute(ctab)
        # 在t1集合中插入1条文档
        for r in rlist[1:]:
            cursor.execute(f'insert into notespider(name) values("{r[0].strip()}"')
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
                self.getPage()
            else:
                print('爬取结束')
                break
                



if __name__ == '__main__':
    ssl._create_default_https_context = ssl._create_unverified_context
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    baseurl = 'https://code.tarena.com.cn/'
    spider = NoteSpyder(baseurl,headers)
    spider.workOn()


# 正则表达式
# <div class="movie-item-info">.*?title=".*?".*?class="star">(.*?)</p>.*?releasetime">(.*?)</p>
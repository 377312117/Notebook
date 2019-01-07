import urllib.request
import urllib.parse
import ssl
import re 


class NeihanSpider:
    def __init__(self,baseurl,headers):
        self.baseurl = baseurl
        self.headers = headers
        self.page = 2

    # 获取页面
    def getPage(self,url):
        req = urllib.request.Request(url,headers=self.headers)
        res = urllib.request.urlopen(req)
        html = res.read().decode('utf-8')
        self.parsePage(html)


    # 解析页面
    def parsePage(self,html):
        p = re.compile('<div class="text-.*?title="(.*?)">.*?class="desc">(.*?)</div>',re.S)
        rlist = p.findall(html)
        # print(rList)
        # [("动物贴墙","海豹"),(),(),()]
        self.writePage(rlist)
        
    # 保存数据
    def writePage(self,rlist):
        for rTuple in rlist:
            with open('neihan.txt','a',encoding='utf-8') as f:
                f.write(rTuple[0].strip()+'\n')
                f.write(rTuple[1].strip()+'\n\n')

    
    # 主函数
    def workOn(self):
        self.getPage(self.baseurl)
        while True:
            c = input('成功,是否继续(y/n):')
            if c.strip().lower() == 'y':
                url = self.baseurl + 'index_' + str(self.page) + '.html'
                self.getPage(url)
                self.page +=1
            else:
                print('爬取结束')
                break
                



if __name__ == '__main__':
    ssl._create_default_https_context = ssl._create_unverified_context
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    baseurl = 'http://neihan8,com/njj'
    spider = NeihanSpider(baseurl,headers)
    spider.workOn()
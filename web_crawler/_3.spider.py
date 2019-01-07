import urllib.request
import urllib.parse
import ssl


class BaiduSpider:
    def __init__(self,baseurl,headers):
        self.baseurl = baseurl
        self.headers = headers

    # 解析页面
    def getPage(self,url):
        req = urllib.request.Request(url,headers=self.headers)
        res = urllib.request.urlopen(req)
        html = res.read().decode('utf-8')
        return html

    # 保存数据
    def parsePage(self,filename,html):
        with open(filename,'w',encoding='utf-8') as f:
            f.write(html)

    
    # 主函数
    def workOn(self):
        name = input('请输入贴吧名称:')
        begin = int(input('请输入起始页:'))
        end = int(input('请输入终止页:'))
        kw = urllib.parse.urlencode({'kw':name}) 
        for page in range(begin,end+1):
            pn = (page-1)*50
            url = self.baseurl+kw + '&pn='+ str(pn)
            print(f'url为{url}')
            filename = name+str(page)+'.html'
            html = self.getPage(url)
            self.parsePage(filename,html)
            print(f'第{page}页爬取成功')



if __name__ == '__main__':
    ssl._create_default_https_context = ssl._create_unverified_context
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    baseurl = 'http://tieba.baidu.com/f?'
    spider = BaiduSpider(baseurl,headers)
    spider.workOn()
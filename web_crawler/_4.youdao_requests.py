'''
此类用于有道的翻译的爬取
'''

import requests
import ssl
import json

class YoudaoSpider:
    def __init__(self,baseurl,headers):
        self.baseurl = baseurl
        self.headers = headers

    # 解析页面
    def getPage(self,data):
        res = requests.post(self.baseurl,data=data,headers=self.headers)
        res.encoding='utf-8'
        html = res.text
        return html

    
    # 主函数
    def workOn(self):
         # 接收用户输入
        key = input('请输入查询词:')
        # 将formdata定义成一个大字典
        data ={
            'i': key,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'salt': '15458147402493',
            'sign': 'b4909747823a2af802693e5f21b1a01b',
            'ts': '1545814740249',
            'bv': '7f2901ed530536104d65f4d3f630826a',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTIME',
            'typoResult': 'false'
        }
        # # 将data转为bytes数据类型
        # 发请求,获取响应,获取内容
        html = self.getPage(data)
        dic = json.loads(html)        
        print(f'翻译内容为:{dic["translateResult"][0][0]["tgt"]}')



if __name__ == '__main__':
    ssl._create_default_https_context = ssl._create_unverified_context
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    baseurl = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    spider = YoudaoSpider(baseurl,headers)
    spider.workOn()







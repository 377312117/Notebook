
import urllib.request
import urllib.parse

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
baseurl = 'http://tieba.baidu.com/f?'
name = input('请输入贴吧名称:')
begin = int(input('请输入起始页:'))
end = int(input('请输入终止页:'))

kw = urllib.parse.urlencode({'kw':name})
for page in range(begin,end+1):
    pn = (page-1)*50
    url = baseurl+kw + '&pn='+ str(pn)
    # 创建请求对象
    req = urllib.request.Request(url,headers=headers)
    # 获取响应对象
    res = urllib.request.urlopen(req)
    # 获取内容
    html = res.read().decode('utf-8')
    with open(f'tieba{page}.html','w',encoding='utf-8') as f:
        f.write(html)
        print(f'{page}页爬取成功')






import urllib.request
import urllib.parse


baseurl = 'http://www.baidu.com/s?wd='
# first_request = urllib.request.urlopen(url)
# print(f'第一个请求:{first_request.read().decode("utf-8")}')

'''
headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
request = urllib.request.Request(url,headers={})
res = urllib.request.urlopen(request)
html = res.read().decode('utf-8')
print(html)
relurl = res.geturl()
relcode = res.getcode()
print(f'code:{relcode}')
print(f'url:{relurl}')
'''

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
# 接收用户从终端输入
key = input('请输入要搜索的内容')
# 进行urlencode编码
# key = urllib.parse.urlencode({'wd':key})
key = urllib.parse.quote(key)
# 拼接url
url = baseurl+key
print(f'url:{url}')

# 创建请求对象
req = urllib.request.Request(url,headers=headers)
# 获取响应对象
res = urllib.request.urlopen(req)
# 获取内容
html = res.read().decode('utf-8')
print(html)
with open('meinv.html','w',encoding='utf-8') as f:
    f.write(html)
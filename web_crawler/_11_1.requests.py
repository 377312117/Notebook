import requests

url = 'http://www.baidu.com/'
headers = {'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
# 发请求获取响应对象
res = requests.get(url,headers=headers)
res.encoding = 'utf-8'
html = res.content

with open('yinbao.jpg','wb')as f:
    f.write(html)

print('保存到本地')


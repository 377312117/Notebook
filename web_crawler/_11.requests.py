import requests

url = 'http://www.baidu.com/'
headers = {'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
# 发请求获取响应对象
res = requests.get(url,headers=headers)
res.encoding = 'utf-8'
print(res.encoding)
# 获取res内容(字符串)
print(res.text)
# 获取res内容(bytes)
print(res.content)
print(type(res.content))


# 获取响应码
print(res.status_code)


# 获取返回实际数据的URL地址
print(res.url)


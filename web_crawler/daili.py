import requests

url= 'http://httpbin.org/get'


headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

proxies = {'http':'http://37.192.32.213:36344'}

try:
    res=requests.get(url,proxies=proxies,headers=headers,timeout=5)
    res.encoding='utf-8'
    html = res.text 
    print(html)
except Exception as e:
    print(e)


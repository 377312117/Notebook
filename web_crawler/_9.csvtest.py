import urllib.request
import urllib.parse
import ssl
import re 

import csv



with open('test.csv','w',newline='',encoding='utf-8') as f:
    # 创建写入对象
    writer = csv.writer(f)
    # 利用写入对象的writerow()写入csv文件
    writer.writerow(['旭哥',38])
    writer.writerow(['超哥哥',29])
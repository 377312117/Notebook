'''存储小文件'''
from pymongo import MongoClient
import bson.binary

conn = MongoClient("localhost",27017)
db = conn.image
myset = db.flower

# 文件提取
img = myset.find_one({'filename':'flower.jpg'})

# 将数据写入到本地
with open("mm.jpg",'wb') as f:
    f.write(img['data'])


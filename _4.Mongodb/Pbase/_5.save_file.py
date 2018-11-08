'''存储小文件'''
from pymongo import MongoClient
import bson.binary

conn = MongoClient("localhost",27017)
db = conn.image
myset = db.flower

# 存储图片
f = open('img_5.jpg','rb')
data = f.read()

# 将数据转换为mongodb格式
content  = bson.binary.Binary(data)

# 插入集合
myset.insert({'filename':'flower.jpg','data':content})

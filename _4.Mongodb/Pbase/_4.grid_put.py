from pymongo import MongoClient
import gridfs

# 获取数据库对象
conn = MongoClient("localhost",27017)
db = conn.grid

# 获取文件集合对象
fs = gridfs.GridFS(db)

with open('img_5.jpg',"rb") as f:
    # 从数据库存取
    fs.put(f.read(),filename="mm.jpg")
conn.close()

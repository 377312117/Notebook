from pymongo import MongoClient

# 创建数据库连接
conn = MongoClient('localhost',27017)

# 创建数据库连接对象
db = conn.stu

# 创建集合对象
myset = db.class4

# 查看模块中所有的集合操作符
print(dir(myset))

# 插入文档
# myset.insert_many([{"name":"张铁林","King":"乾隆"},{"name":"张国立","King":"康熙"}])
# myset.insert_one({"name":"任贤齐","King":"杨过"})
# myset.insert_many([{"name":"古天乐","King":"丁鹏"},{"name":"李若彤","king":"小龙女"}])

# 查找操作
cursor = myset.find({}, {"_id":0})
for i in cursor:
    print(i)
# 关闭数据库连接
conn.close()

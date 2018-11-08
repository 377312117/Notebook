# 在t1中增加一条记录
# 在t1表中把李白的成绩改为100分
# 删除一条记录
import pymysql
db = pymysql.connect(host = "localhost",user = "root",password = "123456",database = "studb2",charset = "utf8")
cursor = db.cursor()

# 修改表                                  a
# try:
#     cursor.execute("insert into t1 values(5,'贺知章',96);")
#     print("插入成功")
#     cursor.execute("update t1 set score = 100 where name = '李白';")
#     print("修改成功")
#     cursor.execute("delete from t1 where name = '杜甫';")
#     print("删除成功")

# except Exception as e:
#     db.rollback()
#     print("Failed",e)

# 查看表
cursor.execute("select * from t1;")
print(cursor.fetchall())

# 结束事务
db.commit()
print("ok")

# 关闭..
cursor.close()
db.close()
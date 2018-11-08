from pymysql import *

#创建数据库连接对象
db = connect(host = "localhost",user = "root",
password = "123456",database = "studb2",charset = "utf8")

#创建游标对象(利用数据库的对象)
cursor = db.cursor()

#执行sql语句
cursor.execute("")

# 提交到数据库执行
db.commit()

#关闭游标对象
cursor.close()

#关闭数据库连接对象
db.close()




# 创建数据库连接对象
db = pymysql.connect(host = "localhost",user = "root",password = "123456",database = "studb2",charset = "utf8")

# 创建游标对象(利用数据库的对象)
cursor = db.cursor()

# 执行sql命令(利用游标对象)
cursor.execute('insert into t1 values(4,"王维",80);')

# 提交到数据库执行
db.commit()

# 关闭游标对象
cursor.close()

# 关闭数据库连接对象
db.close()
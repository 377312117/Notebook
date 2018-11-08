import pymysql

db = pymysql.connect("localhost","root","123456")
cursor = db.cursor()
# cursor.execute("create database indexdb;")
cursor.execute("use indexdb;")
cursor.execute("create table t3(id int,name char(20));")
n = 1
name="lucy"
while n <= 2000000:
    cursor.execute("insert into t3 values('%s','%s')" % (n,name+str(n)))
    print("正在插入第%d" % n)
    # n = int(n)
    n += 1

db.commit()
cursor.close()
db.close()
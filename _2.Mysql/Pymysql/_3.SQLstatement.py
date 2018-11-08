import pymysql
db = pymysql.connect(host = 'localhost',user = "root",password = "123456",database = 'studb2',charset = "utf8")
cursor = db.cursor()
while True:
    name =  input("请输入姓名:")
    if name == "q":
        break
    score = input("请输入成绩:")
    try:

        ins = 'insert into t1(name,score) values(%s,%s)'
        # 如果用%占位给值,需要将%s用引号引起来,不推荐
        # ins = 'insert into t1(name,score) values("%s","%s")' % (name,socre)
        cursor.execute(ins,[name,score])
        db.commit()
        print("ok")
    except Exception as e:
        db.rollback()
        print("failed",e)

cursor.close()
db.close()
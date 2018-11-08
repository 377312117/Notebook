from pymysql import *

# 创建如何连接mysql的类,具有查找和修改功能
def PythonMysql():
    def __init__(self,database,host = "localhost",user = "root",\
    password = "123456",charset = "utf-8",port = 3306):
        '''对PythonMysql 进行初始赋值'''
        self.database = database 
        self.host = host
        self.user = user 
        self.password = password
        self.charset = charset
        self.port = port

    def open(self):
        '''创建数据库对象和游标对象'''
        self.db = connect(host = self.host,user = self.user,password\
        = self.password,port = self.port, database = self.database,\
        charset = self.charset)
        self.cur = self.db.cursor()
    def close(self):
        '''关闭游标对象和数据库对象'''
        self.cur.close()
        self.db.close()

    def to_execute(self,sql,L = None):
        '''执行sql命令'''
        self.open()
        self.cur.execute(sql,L)
        self.db.commit()
        print("ok")
        self.close()
    
    def select():
        '''查询数据库'''
        self.open()
        self.cur.execute(sql,L)
        result = self.cur,fetchall()
        return result

if __name__ == "__main__":
    sqlh = PythonMysql("studb2")
    upd = input("请输入增删改查sql语句")
    sqlh.to_execute(upd)

from pymysql import * 
class Mysqlpython:
    def __init__(self,database,host = "localhost",user = "root",password = "123456",
    charset = "utf8",port = 3306):
       '''对mysqlpython 进行初始赋值'''
       self.database = database
       self.host = host
       self.user = user
       self.port = port
       self.password = password
       self.charset = charset
       self.port = port

    def open(self):
        '''创建数据库连接对象和游标对象'''
        self.db = connect(host = self.host,user = self.user,password = self.password,
        port = self.port,database = self.database,charset = self.charset)
        self.cur =self.db.cursor()

    def close(self):
        '''关闭游标对象和数据库连接对象'''
        self.cur.close()
        self.db.close()
    
    def zhixing(self,sql,L = None):
        '''执行sql命令'''
        self.open()
        self.cur.execute(sql,L)
        self.db.commit()
        print("ok")
        self.close()
    
    def select(self,sql,L = None):
        '''查询数据库'''
        self.open()
        self.cur.execute(sql,L)
        result = self.cur.fetchall()
        return  result

# 作为测试使用,如果本模块作为主程序,则创建实例
# 若作为主程序的导入模块,则下列实例不会被创建
if __name__ == "__main__":
    sqlh = Mysqlpython("studb2")
    upd = input('请输入增删改sql语句:')
    sqlh.zhixing(upd)
    # r = sqlh.all("select * from t1")
    # print(r)
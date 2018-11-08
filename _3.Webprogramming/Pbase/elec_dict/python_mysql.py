from pymysql import * 
class Mysqlpython:
    '''包含了简单的数据库的增删改查功能'''
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
        '''执行sql命令进行增删改等操作'''
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
        # fetchone返回单元组,无则返回None,fetchall返回包含元组的元组
        return  result

# 作为测试使用,如果本模块作为主程序,则创建实例
# 若作为主程序的导入模块,则下列实例不会被创建
import time
if __name__ == "__main__":
    sqlh = Mysqlpython("elec_dict")
    result = sqlh.select('select * from word_phrase where word=%s;',["a"])
    # 返回一个元组,每个查询结果以元组为元素存入其中,如果无查询结果,则是一个空元组
    if not result:
        print('无查询结果')  
    else:
        senddata = ["OK",result[0][1],result[0][2]]
        print(senddata)
    # try:
    #     myFiles=open("dict.txt",'r')
    #     while True:
    #         line =myFiles.readline()
    #         #一旦读取到空,则结束读取
    #         if line == "":
    #             break
    #         #删除右边的换行符
    #         line =line.rstrip()
    #         #形成单独的个人信息列表
    #         word = line[0:17].rstrip()
    #         phrase = line[17:].strip()
    #         upd = """insert into word_phrase(word,phrase) values("%s","%s");""" % (word,phrase)
    #         # print(upd)
    #         sqlh.zhixing(upd)
    #         # 把个人信息放入字典中
    #     myFiles.close()
    #     print('导入完成')
    # except OSError:
    #     print("读取失败")
    
# 如果使用正则表达式
# import re 
# for line in f:
#     obj = re.match('([-a-zA-Z]+)\s+(.+)',line)
#     word = obj.group(1)
#     inerpret = obj.group(2)

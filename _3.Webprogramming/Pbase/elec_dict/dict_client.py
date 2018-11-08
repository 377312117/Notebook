'''
客户端包括了两级界面,客户端负责请求和展示数据
客户端启动即进入一级界面(print打印)
    一级界面功能包括登录注册,退出
用户登录后即进入二级界面
    注册后是否处于登录状态自定,
    二级功能:查看单词    
        要求:可以循环输入单词,获取单词解释
            提示
            每个单词占一行
            单词按照顺序排列
            单词和解释之间一定有空格
            可以选择直接操作文本
            或者将单词本导入数据库然后从数据库查找
        查看历史记录
            格式:name   word   time
            可以显示登录人员查的所有单词或者最近十条
        注销
            返回一级界面
'''

from socket import *
import time
import sys
from getpass import getpass


# 全局变量
client_ip = '127.0.0.1'
client_port = 9090
ADDR =(client_ip,client_port)


class DictClient(object):
    '''分别封装了以下功能:
        连接服务器
        一级用户界面
        二级用户界面
        注册,登录,查询,查看查询记录等功能
        '''
    def __init__(self,address):
        self.address = ADDR
        self.client_socket(address)

    def client_socket(self,address):
        '''连接客户端'''
        self.sockfd = socket()
        try:
            self.sockfd.connect(self.address)
        except Exception as e:
            print('Error',e)
            return

    def first_interface(self):
        '''负责展示一级界面'''
        while True:
            print('+++++++++++++++++++Main Choice+++++++++++++++++++')
            print('+++++++1.Already a member?Please Login in++++++++')
            print('+++++++2.Not a member?Please register++++++++++++')
            print('+++++++q.Want to quit?Good bye+++++++++++++++++++')
            try:
                cmd = input('please input your command:')
            except Exception as e:
                print('命令错误')
                continue
            if cmd == 'q':
                print('Thank you for  using it')
                self.quit_pro()
            elif cmd == '1':
                print('请输入您的登录信息')
                self.verify_login()
            elif cmd == '2':
                print('请输入您的注册信息')
                self.register_user()
            else:
                print("输入命令有误,请重新输入")
                          
    def verify_login(self):
        '''
        主要功能
            负责验证用户的用户名,密码
        整体逻辑
            1.发送用户名到服务器判断是否存在
            2.存在则返回账户密码进行判断.判断完成后进入二级查询界面
        '''
        while True:
            user_name = input('请输入您的用户名:')
            if not user_name:
                print('退出登录')
                break
            senddata ='L ' + user_name
            self.sockfd.send(senddata.encode())
            data = self.sockfd.recv(2048).decode().split(' ')
            if data[0] == 'OK':
                # 如果确认数据库中存在该用户名进行下一步验证
                while True:
                    user_password = getpass('请输入您的密码:')
                    if user_password == data[2]:
                        print('登录成功!')
                        self.sec_interface(user_name)
                        break
                    elif user_password == '':
                        print('退出登录界面')
                        break
                    else:
                        print('输入错误,请重新输入')
            elif data[0] == 'notexist':
                print("用户名不存在请重新输入")
        
    def register_user(self):
        '''
        主要功能
            负责用户的注册
        整体逻辑:
            1.先发送输入用户名给服务器判断用户名是否存在,若不存在进行密码设置
            2.设置完以后返回账户密码给服务器并存入数据库,
            3.注册完成进入到二级查询界面
        '''
        while True:
            user_name = input('请输入您的注册用户名:')
            if not user_name:
                print('退出登录')
                break
            if " " in user_name:
                print('用户名包含空格,请重新输入!')
                continue
            senddata ='R ' + user_name
            self.sockfd.send(senddata.encode())
            data = self.sockfd.recv(128).decode()
            if data == 'OK':
                while True:
                # 如果确认数据库中不存在该用户名进行下一步验证
                    user_password = getpass('请输入密码(不少于六位且无空格):')
                    reuser_password = getpass('请再次输入密码:')
                    if len(user_password) < 6 or (' ' in user_password):
                        print('密码不符合规范,请重新输入')
                        continue
                    elif user_password != reuser_password:
                        print("两次密码不相同,请重新输入!")
                    else:
                        senddata = user_name+' '+user_password
                        self.sockfd.send(senddata.encode())
                        print('注册成功')
                        self.sec_interface(user_name)
                        break
                break
            elif data == 'already exist':
                print('用户名已经存在,请重新输入')
    
    def quit_pro(self):
        '''退出客户端'''
        self.sockfd.send(b'Q')
        self.sockfd.close()
        sys.exit('谢谢使用')             
    
    def sec_interface(self,user_name):
        '''负责展示用户的二级界面'''
        while True:
            print('+++++++++++++++++function Chioce+++++++++++++++++')
            print('+++++++++1.View word interpretation++++++++++++++')
            print('+++++++++2.View query records++++++++++++++++++++')
            print('+++++++++q.Log out+++++++++++++++++++++++++++++++')
            cmd1 = input('please input function chioce:')
            if cmd1 == 'q':
                print('Exit the interface')
                self.first_interface()
                break
            elif cmd1 == '1':
                print('使用查询功能:')
                self.query_word(user_name)
            elif cmd1 == '2':
                print('查询最近十条查询记录')
                self.query_log(user_name)
            else:
                print('无该命令选项')

    
    def query_word(self,user_name):
        '''封装了具体的查询功能'''
        while True:
            word = input("请输入您要查询的单词,按enter退出查询:")
            if not word:
                print('退出查询界面')
                break    
            senddata = "C "+ word + " " + user_name
            self.sockfd.send(senddata.encode())
            recvdata = self.sockfd.recv(1024).decode()
            if recvdata == 'OK':
                time.sleep(0.1)
                recvdata = self.sockfd.recv(2048).decode()
                print('%s的含义为:%s'% (word,recvdata))
            elif recvdata == 'not exist':
                print('单词不存在,请重新查询')
            else:
                print('未能识别,请重新查询')
        

    def query_log(self,user_name):
        '''封装了具体的查看查询记录的功能.可放在客户端进行'''
        data ='S '+user_name
        self.sockfd.send(data.encode())
        recvdata = self.sockfd.recv(1024).decode()
        if recvdata == 'OK':
            print('查询成功,历史记录如下:')
            while True:
                if recvdata == "##":
                    print('查询结束!')
                    break
                recvdata =self.sockfd.recv(1024).decode()
                print(recvdata)
        elif recvdata == 'notexist':
            print('为查询到历史记录,返回到上级界面')            


                

def main():
    elecdict = DictClient(ADDR)
    elecdict.first_interface()



if __name__ == '__main__':
    main()
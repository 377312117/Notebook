# 面向对象综合练习
    # 两个人:
    #       1.姓名:张三,年龄:35
    #        2.姓名:李四,年龄:8
    
    # 行为:
    #       教别人学东西 teach
    #       赚钱   work
    #       借钱   borrow
    #       显示自己信息 show_info
    #       张三 教李四 学 python 
    #       李四 教张三 学 王者荣耀
    #       张三 上班赚了 1000元钱
    #       李四  向张三 借了 200元
    #       35 岁的 张三 有钱 800 元,他学会的技能是: 王者荣耀
    #       8  岁的 李四 有钱 200 元,他学会的技能是: python

# 程序如下:
# 初始化函数
class Human:
    def __init__(self,n,a):
        self.name = n      # 姓名
        self.age = a       # 年龄 
        self.money = 0     # 资产
        self.skill = []    # 技能
# 教学函数
    def teach(self,other,skill):
        print(self.name,"教",other.name,skill)
        other.skill.append(skill)
# 工作赚钱函数
    def work(self,money):
        print(self.name,"上班赚了",money,"元钱")
        self.money += money
# 借钱函数
    def borrow(self,other,money):
        print(other.name,"借钱给",self.name,money,"元钱")
        self.money += money
        other.money -= money
# 显示信息函数
    def show_info(self):
        print(self.age,"岁的",self.name,"有钱",self.money,"元,他学会的技能是",self.skill[0])
#调用函数做事
# 为对象初始化属性
zhang3 = Human("张三",35)
li4 = Human("李四",8)
# 教学
zhang3.teach(li4,"python")
li4.teach(zhang3,"王者荣耀")
# 赚钱过程
zhang3.work(1000)
li4.borrow(zhang3,200)
# 显示两人信息
zhang3.show_info()
li4.show_info()
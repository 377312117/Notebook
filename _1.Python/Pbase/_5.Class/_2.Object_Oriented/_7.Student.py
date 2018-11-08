# 写一个学生的Student类,此类用于描述学生的信息
# 学生信息有:
#     姓名,年龄,成绩,默认为90
# 1.为该类添加初始化方法,实现在创建对象时自动设置姓名,年龄,成绩属性
# 2.添加set_score方法,能为对象修改成绩信息
# 3.添加show_info方法打印学生信息
# 如:
class Student:
    def __init__(self,n,a,s=90):
        self.name = n
        self.age = a
        self.score = s
    def set_score(self,score):
        self.score = score
    def show_info(self):
        print(self.name,"年龄:",self.age,",分数为:",self.score)
L = []
L.append(Student("小张",20,100))
L.append(Student("小李",18))
L.append(Student("小张",19,85))
L[1].set_score(70)
for s in L:
    s.show_info()


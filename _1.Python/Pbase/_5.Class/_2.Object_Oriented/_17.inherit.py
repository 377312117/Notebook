# 此示例示意单继承的用法
class Human:
    """此类用于描述人类的共性"""
    def say(self,what):
        print("说",what)
    def walk(self,distance):
        print("走了",distance,"公里")

class student(Human):
    def study(self,subject):
        print("正在学习:",subject)

class teacher(student):
    def teach(self,subject):
        print("正在学习:",subject)

h1 = Human()
h1.say("天真蓝")
h1.walk(5)

s1=student()
s1.say("学习有点累")
s1.walk(1)
s1.study("python")

t1 = teacher()
t1.say("终于国庆放假了")
t1.walk(8)
t1.study("继承/派生")
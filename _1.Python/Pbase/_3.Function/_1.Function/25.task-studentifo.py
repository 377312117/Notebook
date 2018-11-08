#改写之前的学生管理信息
# 改用两个函数
# 1)当函数input_student()来获取学生信息,当
#   输入空时结束,形成字典组成的列表并返回
# 2)当函数print_student(L)将上述函数得到的打印成表格显示
# 如:
#     def input_student():
#         ...
#     def print_student():
#         ...
# L=input_student():   #获取表格
# print(L)
# print_student(L)
L1=["name","age","score"]
def input_student():
    l=[]
    while True:
        dic={}
        s1=input("please input name:")
        if s1 == "":
            break
        s2=input("please input age:")
        s3=input("please input score:")
        L2=[s1,s2,s3]
        for x in range(0,3):
            dic[L1[x]]=L2[x]
        l.append(dic)
    return l
L=input_student()
print("学生信息为:",L)
def print_student(L):
    c1="+--------+--------+--------+"
    c2="|  name  |   age  |  score |"
    print(c1)
    print(c2)
    print(c1)
    for x in L:
        c3=x["name"].center(8)
        c4=x["age"].center(8)
        c5=x["score"].center(8)
        print("|"+c3+"|"+c4+"|"+c5+"|")
    print(c1)
print_student(L)
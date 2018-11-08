#实现带界面的学生信息管理系统的项目
#+--------------------------+
#|1)添加学生信息              |
#|2)显示学生信息              |
#|3)删除学生信息              |
#|4)退出                     |
#+--------------------------+
# 用函数来实现,每个功能写一个函数与之相对应
# 用于制作添加元素的函数
l=[]
def input_studentinfo():
    L1=["name","age","score"]
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
# 用于查看列表的函数
def print_studentinfo():
    c1="+---------------+--------+--------+"
    c2="|     name      |   age  |  score |"
    print(c1)
    print(c2)
    print(c1)
    for x in l:
        c3=x["name"].center(15)
        c4=x["age"].center(8)
        c5=x["score"].center(8)
        print("|"+c3+"|"+c4+"|"+c5+"|")
    print(c1)
# 用于删除列表中的元素的函数
def delete_studentinfo():
    t=input("请输入您要删除学员信息的名字:")
    for y in range(0,len(l)):
        if l[y]["name"] == t:
            del l[y]
            print("您已删除学生%s的信息!" % t)
            break
# 用于修改列表中元素的函数
def alter_studentscore():
    t1=input("请输入需要修改成绩的学员姓名:")
    t2=input("请输入成绩:")
    global l
    for z in range(0,len(l)):
        if l[z]["name"] == t1:
            l[z]["score"] = t2
            print("您已修改学生%s的成绩为%s!" % (t1,t2))
            break
s1="+--------------------------------------------------+"
s2="|1)insert into student infomation                  |"
s3="|1)select student infomation                       |"
s4="|3)delete student infomation                       |"
s5="|4)exit  system                                    |"
print(s1,s2,s3,s4,s5,s1,sep="\n")
while True:
    s=int(input("请输入选项:"))
    if s == 1:
        L=input_studentinfo()
    elif s == 2:
        print_studentinfo()
    elif s == 3:
        delete_studentinfo()
    elif s == 4:
        alter_studentscore()
    elif s == 5:
        print("已退出系统!")
        break

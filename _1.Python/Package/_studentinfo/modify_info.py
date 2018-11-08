# 用于修改列表中元素的函数
def alter_studentscore(l):
    t1=input("请输入需要修改成绩的学员姓名:")
    t2=int(input("请输入成绩:"))
    for z in range(0,len(l)):
        if l[z]["name"] == t1:
            l[z]["score"] = t2
            print("您已修改学生%s的成绩为%s!" % (t1,t2))
            break

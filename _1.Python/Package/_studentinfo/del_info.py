# 用于删除列表中的元素的函数
def delete_studentinfo(l):
    t=input("请输入您要删除学员信息的名字:")
    for y in range(0,len(l)):
        if l[y]["name"] == t:
            del l[y]
            print("您已删除学生%s的信息!" % t)
            break
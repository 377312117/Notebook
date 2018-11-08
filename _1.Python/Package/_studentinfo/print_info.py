# 用于查看列表的函数
def print_studentinfo(l):
    c1="+---------------+--------+--------+"
    c2="|     name      |   age  |  score |"
    print(c1)
    print(c2)
    print(c1)
    for x in l:
        c3=x["name"].center(15)
        c4=str(x["age"]).center(8)
        c5=str(x["score"]).center(8)
        print("|"+c3+"|"+c4+"|"+c5+"|")
    print(c1)
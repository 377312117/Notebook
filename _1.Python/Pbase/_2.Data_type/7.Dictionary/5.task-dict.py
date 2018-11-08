#任意输入多个学生姓名,年龄,成绩,每个学生的信息存于字典中,再放入列表中
#如:请输入姓名:tarena 
#     请输入姓名:tarena
#     请输入年龄:15 
#     请输入成绩:99
#     请输入姓名:zhangsan
#     请输入年龄:22
#     请输入成绩:100
#     请输入姓名:<直接回车结束输入>
# 在程序中生成如下列表:
# L=[{"name":tarena,"age":15,"score":99},{"name":"name2","age":22,
# "score":100}]
# 1.打印此列表
# 2.以下列表格的形式打印出上述信息
# +--------+--------+--------+
# |  name  |   age  |  score |
# +--------+--------+--------+
# | tarena |   15   |   99   |
# |zhangsan|   22   |   100  |
# +--------+--------+--------+
L1=["name","age","score"]
L=[]
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
    L.append(dic)
print(L)
print("+--------+--------+--------+")
print("|  name  |   age  |  score |")
print("+--------+--------+--------+")
for x in L:
    print("|"+x[L1[0]].center(8)+"|"+x[L1[1]].center(8)+"|"+x[L1[2]].center(8)+"|")
print("+--------+--------+--------+")
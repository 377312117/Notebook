# 练习: 写一个程序,输入很多人的姓名,年龄,家庭住址,保存在infos.txt中.格式自定义,建议用空格或者逗号隔开
# 如: 小李 20 北京市朝阳区
    # 小张 18 上海市浦东区
# myFiles=open("infos.txt","a")
# while True:
#     s1 = input("请输入学生姓名:")
#     if s1 == "":
#         break
#     s2 = int(input("请输入学生成绩:"))
#     s3 = int(input("请输入学生年龄:"))
#     s4 = input("请输入学生地址:")
#     myFiles.write([s1+" ")
#     myFiles.write([s2+" ")
#     myFiles.write([s3+" ")
#     myFiles.write([s4+" ")
#     myFiles.write("\n")
# myFiles.close()

# 解析: 分两步来做   
# 1.读取数据作为字典
# 2.将数据保存到infos.txt

def get_info():
    L=[]
    while True:
        n = input("请输入姓名:")
        if n == "":
            break
        a = int(input("请输入年龄:"))
        b = input("请输入家庭住址")
        d = dict(name=n,age=a,address = b)
        L.append(d)
    return L
def save_to_file(L):
    try:
        myFiles=open("infos.txt","w")
        for d in L:
            myFiles.write(d["name"])
            myFiles.write(" ")
            myFiles.write(str(d["age"]))
            myFiles.write(" ")
            myFiles.write(str(d["address"]))
            myFiles.write("\n")
        myFiles.close()
    except OSError:
        print("写入错误")
L=get_info()
print(L)
save_to_file(L)
# 将如下数字用编辑器写入文件data.txt中,数据如下
    # 小李   13888888888
    # 小赵   13999999999
    # 张三丰 010-88888888

# 写程序读取文件中的数据,打印出姓名和电话号码,
# 格式如下:
#     姓名: 小李 电话:13888888888
#     姓名: 小赵 电话:13999999999
#     姓名: 张三丰  电话:010-88888888

# 方法1:
# try:
#     f = open("data.txt") 
#     print("成功打开文件")
#     s1 = f.read(3)
#     s2 = f.read(12)
#     s3 = f.read(3)
#     s4 = f.read(12)
#     s5 = f.read(4)
#     s6 = f.read(12)        
#     print("name:",s1,end=" ")
#     print("电话:",s2)
#     print("name:",s3,end=" ")
#     print("电话:",s4)
#     print("name:",s5,end=" ")
#     print("电话:",s6)
# # 关闭文件
#     f.close()
#     print("成功关闭文件")
# except OSError:
#     print("打开文件失败")

# 方法2
# f = open("data.txt") 
# while True:
#     line =f.readline()
#     if line == "":
#         break
#     line = line.strip()
#     L = line.split()
#     print("姓名:",L[0],"电话:",L[1])
# f.close()

# 方法3
# f = open("data.txt") 
# lines =f.readlines()
# for line in lines:
#     line = line.strip()   #去掉末尾/n
#     L = line.split()    # 将其拆分成字符串列表
#     print("姓名:",L[0],"电话:",L[1])
# f.close() 

# 方法4
f = open("data.txt") 
s = f.read()
lines = s.split("\n")    #拆分为几个列表组成的
for line in lines:
    line = line.strip()  
    L = line.split()    
    print("姓名:",L[0],"电话:",L[1])
f.close() 
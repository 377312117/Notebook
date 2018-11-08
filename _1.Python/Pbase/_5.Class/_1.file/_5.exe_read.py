# 读入infos.txt中的内容
# 以如下格式打印
# 以如下格式打印:
# 姓名 : 小张.年龄:20  住址:北京市朝阳区
# ...
# 1.从文件中读取数据,形成字典组成的列表
# 2.打印表中的数据
# 

def read_from_file():
    """返回字典组成的列表"""
    L = []
    try:
        myFiles=open("infos.txt")
        while True:
            line =myFiles.readline()
            #一旦读取到空,则结束读取
            if line == "":
                break
            #删除右边的换行符
            line =line.rstrip()
            #形成单独的个人信息列表
            items = line.split()
            # 把个人信息放入字典中
            d = dict(name=items[0],age=int(items[1]),address = items[2])
            L.append(d)
        myFiles.close()
    except OSError:
        print("读取失败")
    return L
# 从文件中读取数据形成字典组成的列表
def print_infos(L):
    print(L)
L = read_from_file()
# 打印列表中的数据
print_infos(L)


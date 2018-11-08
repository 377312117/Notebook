# 此示例示意文件的打开.读写操作
# 打开操作
try:
    f = open("mynote.txt")   # 打开文件,用f绑定文件流对象
    print("成功打开文件")

# 读写文件
    s = f.readline()    # 在文件中读取一行文字
    s = f.readlines()   # 读取多行,组成列表
    s = f.read(3)       # 读取3个字符,每次读取都会依次向后,如果括号里为0.则全部读取
    print("您读到的是:",s)
    print("您读到的字符个数是:",len(s))
    # 读到的实际上是,末尾带有换行符的字符串,每次readline读取下一行
# 关闭文件
# f.colse()
# print("成功关闭文件")
except OSError:
    print("打开文件失败")

# 此示例示意seek用来改动文件的读写位置
f = open("data.txt","rb")
b = f.read(3)
print("您读取的是",b)
print("当前的读写位置是",f.tell())

# 以下读写第5至第10个字节的b"abcde"
f.seek(2,1)   #从当前位置往后移两个位置
f.seek(5,0)   #从头开始移动5个位置
f.seek(-15,2) #从文件尾向前移动15个位置
print("当前位置是",f.tell())
b = f.read(5)
print("读取内容是:",b)
f.close()
# 此示例示意用二进制模式读取文件中的数据
f = open("mynote.txt","rb")
b = f.read()
print("读取的内容长度是:",len(b))
print("内容是:",b)
s = b.decode()   # 将二进制转化为字符串
print("转化为字符串s为:",s)
f.close()
# 此示例示意 tell的用法
f = open("data.txt","rb")

f.read(3)
print("当前读写位置是",f.tell())

f.read(7)
print("当前读写位置是",f.tell())

f.read(7)
print("当前读写位置是",f.tell())

f.close()
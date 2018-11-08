# 此示例示意二进制文件的写入
try:
    f = open("0_255.bin","wb")
    b = bytes(range(256))
    f.write(b)
    f.close()
    print("写入成功")
except OSError:
    print("写入失败")
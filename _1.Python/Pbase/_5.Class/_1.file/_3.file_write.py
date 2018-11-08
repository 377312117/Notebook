# 如果是命令符为w,若文件不存在,则创建一个以该名字命名的文件
f = open("myfile.txt","w")  
print("打开文件成功")
f.write("这是第一行文字\n")
f.write("ABCDEFG")
f.writelines(["aaaaaaaaaaa",
"bbbbbbbbbbbbbbb",
"ccccccccccccccccc"])    # 不会自动添加换行
print("写入成功")
f.close()
print("关闭成功")
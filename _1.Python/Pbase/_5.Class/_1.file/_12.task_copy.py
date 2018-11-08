# 1.用程序实现赋值文件功能
# 要求:
    # 1.源文件路径和目标文件路径需手动输入
    # 2.要考虑关闭文件问题
    # 3.要考虑复制超大文件问题
    # 4.要能复制二进制文件
def copy_from_file(x,y):
    """x为源文件路径,y为目标文件路径,此函数的目的为复制文件"""
    try:
        try:
            myFiles=open(x,"rb")   #读文件
            myFiles1=open(y,"wb")  #复制目标文件
            while True:
                data =myFiles.read(4096)
                #一旦读取到空,则结束读取
                if data == "":
                    break
                # 把个人信息放入目标文件中
                myFiles1.write(data)
                myFiles1.flush()
            myFiles.close()    #关闭读文件
            myFiles1.close()   #关闭写文件
            print("复制成功")
        except OSError:
            print("打开写文件失败")
            return False
    finally:
        fr.close()
    return True

s1=input("请输入源文件路径(包含文件名):")
s2=input("请输入目标文件路径(包含文件名):")
if copy_from_file(s1,s2):
    print("复制文件成功")
else:
    print("复制文件失败")
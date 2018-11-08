#写程序，输入一个整数代表三角形宽度和高度
# *
# **
# ***
# ****
width=int(input("请输入一个宽度和高度："))
for x in range(1,width+1):
    y=" "*x
    print(y+"*"*(width-x+1))
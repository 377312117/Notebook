# 打印 9*9乘法表
# 1*1=1
# 1*2=2  2*2 =4
# ......
#思路:第一步,建立列循环,1~9
for x in range(1,10):
    for y in range(1,x+1):
        z = x * y
        print("%dX%d=%d" %(y,x,z),end=" ")
    print()
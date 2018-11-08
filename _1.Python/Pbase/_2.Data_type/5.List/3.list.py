#写一个程序，让用户输入很多歌正整数，当输入负数时结束输入
#1)将用户输入的数存于列表中，打印这个列表
L=[]
while True:
    x=int(input("请输入整数:"))
    if x<0:
        break
    L+=[x]
print(L)


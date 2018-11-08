#打印一行整数，每行打印５个打印n行
n=int(input("请输入整数："))
i=1
while i<=n:
    print(i,end=" ")
    if i%5==0:
        print()
    i+=1
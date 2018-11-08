#写程序，输入一个整数带便正方形的边长，打印制定图形
width=int(input("请输入一个宽度和高度："))
i=1
while i<=width:
    j=i
    while j<=width+i-1:
        print(j,end=" ")
        j+=1
    i+=1
    print()

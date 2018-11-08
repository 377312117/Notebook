width=int(input("请输入一个宽度和高度："))
i=1
for x in range(1,width+1):
    for y in range(i,width+i):
        print(y,end=" ")
    i+=1
    print()
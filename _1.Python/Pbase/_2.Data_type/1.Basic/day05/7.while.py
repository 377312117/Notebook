#打印为宽度高度为n的正方形图形
n=int(input("请输入宽度和高度："))
i=2
m=n
if n>=2:
    print("#"*n)
    while i<n:
        print("#"+" "*(n-2)+"#")
        i+=1
    print("#"*n)
elif n==1:
    print("#"*n)
else:
    print("您输入有误！")
L=[]
i=0
while True:
    s=int(input("请输入整数："))
    if s==-1:
        break
    else:
        L.append(s)
        i+=1
print("你输入有效数个数为:",i)
print("列表为：",L)
print("此列表最大值为：",max(L))
print("此列表平均值为",sum(L)/i)
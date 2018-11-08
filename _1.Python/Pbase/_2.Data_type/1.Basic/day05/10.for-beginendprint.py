begin=int(input("请输入循环开始的数字："))
end=int(input("请输入循环结束的数字："))
i=1
for x in range(begin,end+1):
    print(x,end=" ")
    if i%5==0:       
        print()
    i+=1
print()
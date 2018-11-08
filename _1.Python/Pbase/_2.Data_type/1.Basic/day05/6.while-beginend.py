begin=int(input("请输入循环开始的数字："))
end=int(input("请输入循环结束的数字："))
i=begin
while i<=end:
    print(i,end=" ")
    if (i-begin+1)%5==0:
        print()
    i+=1
print()
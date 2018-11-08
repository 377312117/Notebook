#输入一个整数用begin绑定
#输入一个整数用end绑定
#打印之间的全部奇数不包括end
begin=int(input("请输入循环开始的数字："))
end=int(input("请输入循环结束的数字："))
for x in range(begin,end):
    if x%2==0:
        continue
    print(x,end=" ")
print()
# 两个输入数用begin,end绑定，
# 将beginend之间的所有偶数存于列表中并打印
begin=int(input("请输入开始的数："))
end=int(input("请输入结束s的数："))
L=[x for x in range(begin,end) if x%2==0]
print(L)
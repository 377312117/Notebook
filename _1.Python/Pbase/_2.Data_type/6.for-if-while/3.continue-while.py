#输入一个开始的数begin
#输入一个结束的数end
#打印之间所有的奇数
#使用while循环
begin=int(input("请输入开始的数："))
end=int(input("请输入结束的数："))
i=begin
while i<end:
    if i%2==1:
        print(i)
    i=i+1


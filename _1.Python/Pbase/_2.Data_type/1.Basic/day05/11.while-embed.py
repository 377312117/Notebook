#打印制定高度，宽度长度的序列矩形
begin=int(input("请输入开始数："))
end=int(input("请输入结束数："))
n=int(input("请输入打印的行数："))
i=1
while i<=n:
    s=begin
    while s<=end:
        print(s,end=" ")
        s+=1
    print()
    i+=1
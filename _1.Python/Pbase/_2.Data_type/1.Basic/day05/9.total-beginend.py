begin=int(input("请输入循环开始的数字："))
end=int(input("请输入循环结束的数字："))
total=0
while begin<=end:
    total+=begin
    begin+=1
print(total)
#求１～１００之间所有不能被２，３，５，７整除的数，
# 打印这些数并且打印这些数的和
begin=int(input("请输入循环开始的数字："))
end=int(input("请输入循环结束的数字："))
total=0
for x in range(begin,end):
    if x%2==0 or x%3==0 or x%5==0 or x%7==0:
        continue
    print(x,end=" ")
    total+=x
print(total)
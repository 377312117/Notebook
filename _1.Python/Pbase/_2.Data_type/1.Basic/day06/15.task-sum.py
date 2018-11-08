#编写一个程序，求下列多项的和
# total=1/1-1/3+1/5-1/7......1000000个这样的分数
# 相加的值是多少，４倍又是多少
total=0
x=1
while x<=20000:
    y=1/x-1/(x+2)
    total+=y
    x+=4
print(total)
print(total*4)
#打印0-100不能被５,7,11整除的数之和
i=0
for x in range(1,101):
    if x%5==0 and x%7==0 and x%11==0:
        continue
    i+=x
else:
    print(i)

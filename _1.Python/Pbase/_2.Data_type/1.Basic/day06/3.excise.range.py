#求１００以内有哪些数和自身＋１的成绩再对１１求余结果等于８
count=0
for x in range(1,101):
    y=x*(x+1)%11
    if y==8:
        count+=1
        print(x,end=" ")
print("这样的数一共有：%d个"%count)

#写程序求：1/1+1/3+1/5...1/99之和
i=1
total=0
while i<=99:
    total+=1/i
    i+=2
print("该序列之和为：%f"%total)
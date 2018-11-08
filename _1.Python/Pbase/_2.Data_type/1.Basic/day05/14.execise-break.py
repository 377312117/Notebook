#输入一些整数，当输入小于０的整数时结束输入，
# 打印您输入的这些正整数的和
total=0
while True:
    n=int(input("请输入整数："))
    if n<=0:
        break
    total+=n
print("您输入的正整数总和为：%d"%total)

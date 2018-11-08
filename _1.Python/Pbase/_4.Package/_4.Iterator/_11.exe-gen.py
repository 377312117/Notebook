def prime(begin,end):
    for x in range(begin,end):
        for y in range(2,x):
            if x % y ==0:
                break
        else:
            yield x
# 第二步:将n对素数相除
L = list(prime(10,20))
print(L)  # [10,12,14,16,18]
# for x in myeven(5,10):
#     print(x)   # 6,8
# L = [x for x in myeven(0,10)]
# print(L)   #[0,2,4,6,8]
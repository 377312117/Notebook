#写一个函数primes()返回指定范围内n以内的素数(不包含n),并打印这些素数
#  L=primes(10)
#  print(L)   #[2,3,5,7]
#  1)打印100以内的素数
#  2)打印200以内的素数
def primes(n):
    L=[]
    for x in range(2,n):
        for y in range(2,x):
            if x % y ==0:
                break
        else:
            L.append(x)
    return L
# print(primes(100))
# print(primes(200))
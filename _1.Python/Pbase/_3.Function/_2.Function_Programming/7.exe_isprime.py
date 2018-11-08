#把1~100之间的全部素数放在列表prime中
def isprime(x):
    if x<2:
        return False
    for i in (2,x):
        if x % i ==0:
            return False
        return True
primes=[x for x in filter(isprime,range(100))]
print(primes)
#用递归的方式求1+2+3......n的和
def mysum(n):
    if n == 1:
        return 1
    return n + mysum(n-1)
print(mysum(100))  #5050
#崩溃 crash
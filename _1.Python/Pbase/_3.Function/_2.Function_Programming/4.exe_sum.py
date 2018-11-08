#求1**3+2**3.....+9**3的和
def pow2(x):
    return x**3
s=0
for x in map(pow2,range(1,10)):
    s += x
print(s)
#方法2:
    print(sum(map(lambda x:x**3,range(1,10))))
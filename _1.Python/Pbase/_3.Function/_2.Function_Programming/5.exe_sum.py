# 求1**9+2**8....9**1的和
# s=0
# for x in map(pow,range(1,10),range(9,0,-1)):
#     s += x
# print(s)
#方法2
print(sum(map(pow,range(1,10),range(9,0,-1))))
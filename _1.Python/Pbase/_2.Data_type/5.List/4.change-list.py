# L=[3,5]
# 用索引切片等操作改变为
# L=[1,2,3,4,5,6]
#　将列表翻转，删除最后一个元素后打印此列表
L=[3,5]
L[0:0]=1,2
print(L)
print(id(L))
L[3:3]=[4]
print(L)
print(id(L))
L[len(L):len(L)]=[6]
print(L)
print(id(L))
L=L[::-1]
print(L)
print(id(L))
del L[-1]
print(L)
print(id(L))

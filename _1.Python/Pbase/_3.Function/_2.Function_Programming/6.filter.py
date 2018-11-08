#判断x是否是奇数,如果是奇数返回True,否则返回False
def isodd(x):
    return x % 2 == 1
#生成1~100的奇数
for x in filter(isodd,range(100)):
    print(x,end=" ")
print()
#生成1~100以内的偶数放在列表even中
# even=[x for x in filter(lambda x:x%2 ==0,range(1,100))]
# print(even)
#生成一个可迭代对象,此可迭代对象可以生成
#1**4,2**3,3**2,4**1
#pow(x,y,z=None)
# 示例1:
for x in map(pow,range(1,5),range(4,0,-1)):
    print(x)

# 示例2:
for x in map(pow,[1,2,3,4],[4,3,2,1],range(5,100)):
    print(x)
#返回1,2,2,4,即返回:1**4%5,2**3%6,3**2%7,4**1%8

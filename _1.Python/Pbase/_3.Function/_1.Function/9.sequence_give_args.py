#此示例示意序列传参
def myfun1(a,b,c):
    print(a)
    print(b)
    print(c)
s1=[11,22,33]
#s1是个列表,用*可自动拆解,
# 只可以运用在有序的数据类型中,比如字符串,字典,列表
myfun1(*s1)
s2=(44,55,66)
s3="ABC"
myfun1(*s2)
myfun1(*s3)
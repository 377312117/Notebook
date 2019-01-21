import numpy as np

ary = np.array([1,2,3,4,5])
print(f'ary:{ary},ary*10:{ary*10},ary.shape:{ary.shape},ary.size:{ary.size}')

a = np.arange(1,28)
a.shape = (3,3,3)
print(a,a.shape)
print(a[0])
print(a[0][0])
print(a[0][0][0])
print(a[0,0,0])



b  = np.arange(1,10,1)
print(b)

c = np.zeros(10)
print(c,c.dtype)

d = np.ones(10,dtype='int64')
print(d,d.dtype)

# 测试基本属性


data = [
    ('zs',[10,15,2],3),
    ('zs',[10,15,2],3),
    ('zs',[10,15,2],3),
]
e = np.array(data,dtype='U2,3int32,int32')
print(e)

b = np.array(data,dtype=[
    ('name','str_',2),
    ('scores','int32',3),
    ('age','int32',1),
])

print(b,';zs.name',b[0]['name'])


c = np.array(data,dtype={
    'names':['name','scores','age'],
    'formats':['U2','3int32','int32']
})
print(c,'ls.name:',c[1]['name'])


# 例如scores字段在存储时，将会从第16个字节
# 开始输出分数列表数据，3int32将会占用12
# 字节，那么age字段将会从第28个字节开始
# 向后输出
# U2占用了8字节，与scores字段中间将会
# 空出8个字节，虽然浪费了空间，但是这种数据
# 存储对齐的做法在数据访问时将提高效率
d = np.array(data,dtype={
    'name':('U2',0),
    'scores':('3int32',16),
    'age':('int32',28)
})
print(d,'ls.name:',c[1]['name'])


# 第五种设置dtype的方式
# e = np.array(
#     [0x1234,0x5678],
#     dtype=(
#         'U2',
#         {
#             'lowc':('u1',0),
#             'highc':('u1',1)
#         }
#     )
# )



f = np.array(
    [
        '2018',
        '2019-01-01',
        '2019-02-01',
        '2019-01-02',
        '2019-01-02 01:01:01',   
    ]
)
# 把f数组的元素类型改为日期类型
g = f.astype('M8[D]')
print(g)

h = g.astype('int32')
print(h)


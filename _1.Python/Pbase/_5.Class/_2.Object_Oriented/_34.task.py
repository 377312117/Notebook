# 修改学生管理系统,保护学生信息安全
# 将score, name, age  变为除该类方法外的其它函数和方法无法访问
# (变为私有属性)

# 2. 子集写一个mylist类,实现重写len,和str,让Mylist类型变为可迭代对象

# 3. 写一个类,fibonacci实现迭代器协议,此类的对象可以作为可迭代对象生成相应的斐波那契数列
# 1,1,2,3,5,8,13.....
# 如:
#     class Fibonacci:
#         def __init__(self,n):
#             ...
# 实现如下操作:
#     for  x in Fibonacci(5)
#     print(x)   # 1 1 2 3 5
#     L = [x for x in Fibonacci(50)]
#     print(L)
#     print(sum(Fibonacci(100)))

# 3
class Fibonacci:
    def __init__():
        self.count = n # 记录要生成的数据的个数
    def __iter__(self):
        return fiboIterator(self.count)   # 迭代器
class FiboIterator:
    def __init__(self,cnt):
        self.count = cnt
        self.a = 0          
        self.b = 1          # 绑定当前Fibonacci数
        self.cur_count = 0  #记录已经生成了多少个
    def __next__(self):
        """由迭代器来生成Fibonacci数"""
        if self.cur_count >self.count:
            raise StopIteration   #生成完毕
        v = self.b
        # 算出下一个数,放在self.b中
        self.a,self.b = self.b,self.a +self.b
        # 将已经生成的数加1
        count.cur_count +=1
        ruturn v

#既是可迭代对象又是生成器
class Fibonacci:
    def __init__():
        self.count = n # 记录要生成的数据的个数
        self.a = 0          
        self.b = 1          # 绑定当前Fibonacci数
        self.cur_count = 0  #记录已经生成了多少个
    def __iter__(self):
        return self   # 迭代器
    def __next__(self):
        """由迭代器来生成Fibonacci数"""
        if self.cur_count >self.count:
            raise StopIteration   #生成完毕
        v = self.b
        # 算出下一个数,放在self.b中
        self.a,self.b = self.b,self.a +self.b
        # 将已经生成的数加1
        count.cur_count +=1
        ruturn v




for  x in Fibonacci(5):
    print(x)   # 1 1 2 3 5
L = [x for x in Fibonacci(50)]
print(L)
print(sum(Fibonacci(100)))        
# # 实现两个自定义列表的反向列表相加操作
class Mylist:
    def __init__(self,iterable=()):
        self.data = list(iterable)
    def __repr__(self):
        return "Mylist(%s)" % self.data
    def __add__(self,other):
        return Mylist(self.data + other.data)
    def __mul__(self,rhs):
        return Mylist(self.data * rhs)
    def __rmul__(self,lhs):
        return Mylist(self.data * lhs)
    
    # 复合加等重载
    def __iadd__(self,rhs):
        print("iadd被调用")
        self.data.extend(rhs.data)  

    #一元运算符-号重载
    def __neg__(self):
        L = map(lambda x : -x,self.data)  
        return Mylist(L)

    #一元运算符 +号重载
    def __pos__(self):
        L = [abs(x) for x in self.data]
        return Mylist(L)

    # in 重载
    def __contains__(self,e):
        """重载in 运算符,只需要判断e是否在self里"""
        return e in self.data
    # 赋值重载
    def __getitem__(self,i):
        print("getitem被调用,i=",i)
        if type(i) is int:
            print("您正在执行索引操作")
        elif type(i) is list:
            print("您正在执行切片操作")
            print("起始值:",i.start)
            print("终止值:",i.end)
            print("步长",i.step)
        return self.data[i]
    # del 重载
    def __delitem__(self,i):
        print("delitem被调用,i=",i)
        del self.data[i]
        return self.data
L1 =Mylist(range(1,4))
# print(id(L1))
# L2 =Mylist(range(4,7))
# L5 = L1 *3
# print(L5)    
# L6 =3 * L1
# print(L6) 
# L1 += L2 
L2 = - L1
print(L2)
print(4 in L1)
x = L1[2]
print(x)
del L1[0]
print(L1)
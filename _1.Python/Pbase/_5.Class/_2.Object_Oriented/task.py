# 实现有序集合类Orderset 能实现两个集合的交集&,并集| ,补集 - 
# 对称补集 ^ == != 等操作.功能与集合相同
# 要求,集合内部用list存储
# 如
#     s1 = OrderSet([1,2,3,4])
#     s2 = OrderSet([3,4,5])
#     print(s1 & s2)
#     print(s1 | s2)
#     print(s1 ^ s2)
#     if OrderSet([1,2,3])     # OrderSet([3,4])
#         print("不相等")
#     if 2 in s1:
#         print("2 在 s1内")
#     else:
#         print("2不在s1内")


class OrderSet:
    def __init__(self,iterable=[]):
        self.data = list(iterable)
    # 字符串化表示
    def __repr__(self):
        return "OrderSet(%s)" % self.data
    # 与
    def __and__(self,rhs):
        return OrderSet(set(self.data) & set(rhs.data))
    # 或
    def __or__(self,rhs):
        return OrderSet(set(self.data) | set(rhs.data))
    # 异或
    def __xor__(self,rhs):
        return OrderSet(set(self.data) ^ set(rhs.data))
    # != 
    def __ne__(self,rhs):
        if self.data  != rhs.data:
            return True
        else:
            return False
    # in
    def __contains__(self,e):
        """重载in 运算符,只需要判断e是否在self里"""
        return e in self.data
        
s1 = OrderSet([1,2,3,4])
s2 = OrderSet([3,4,5])
print(s1 & s2)
print(s1 | s2)
print(s1 ^ s2)
if OrderSet([1,2,3]) != s1:    # OrderSet([3,4])
    print("不相等")
if 2 in s1:
    print("2 在 s1内")
else:
    print("2不在s1内")
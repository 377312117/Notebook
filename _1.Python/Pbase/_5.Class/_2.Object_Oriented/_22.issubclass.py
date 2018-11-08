# 此示例示意issubclass的用法
class A:
    pass
class B(A):
    pass
class C(B):
    pass
issubclass(C,A)
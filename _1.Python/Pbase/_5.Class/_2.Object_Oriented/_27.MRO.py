# 此示例示意__mro__的属性和用法
# 小李写了一个A
class A:
    def go(self):
        print("A")

# 小张写了一个B
class B(A):
    def go(self):
        print("B")

# 小张写了一个B
class C(A):
    def go(self):
        print("C")

# 小张写了一个B
class D(B,C):
    def go(self):
        print("D")
# 小王多继承小李和小张

d = D()  
d.go()
# 此函数要测试__bool__
class A:
    pass
    def __bool__(self):
        print("__bool__方法被调用")
        return False

a =A()

print(bool(a))     #True
if a :
    print("a为真值")
else:
    print("a为假值")
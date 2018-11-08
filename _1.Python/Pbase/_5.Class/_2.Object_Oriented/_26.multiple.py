# 此示例示意多继承标识符冲突的问题
# 小李写了一个A
class A:
    def m(self):
        print("A.m()被调用")

# 小张写了一个B
class B:
    def m(self):
        print("B.m()被调用")

# 小王多继承小李和小张
class AB(A,B):
    pass

ab = AB()
ab.m()    # 写在继承列表前面的被执行,出现了冲突,这个问题很难解决
# A.m()被调用
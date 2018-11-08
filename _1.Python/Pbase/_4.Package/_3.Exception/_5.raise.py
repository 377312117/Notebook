# 此示例示意raise发送错误通知的用法
def make_except():
    print("函数开始")
    # 发出ZeroDivisionError通知给调用者
    # raise ZeroDivisionError
    e = ValueError("值错误")  #创建一个错误对象
    raise e    #将错误信息发送给调用者
    print("函数结束")
try:
    make_except()
except ZeroDivisionError:
    print("接收到make_except发出的错误通知")
except ValueError as err:    #绑定的不是类型而是对象("值错误")
    print("ValueError-->",err)    
print("程序正常结束")

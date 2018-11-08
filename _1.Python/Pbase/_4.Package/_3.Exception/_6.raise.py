#此示例示意raise无参的用法
def fa():
    print("函数开始")
    raise ValueError("故意制造的一个错误!")
    print("函数结束")
def fb():
    print("函数开始")
    try:
        fa()
    except ValueError as err:
        print("fa里发生了值错误已处理")
        #此处如果要将err再次向上传递
        raise
    print("函数结束")
try:
    fb()
except ValueError:
    print("再一次收到fb内部发送的错误")
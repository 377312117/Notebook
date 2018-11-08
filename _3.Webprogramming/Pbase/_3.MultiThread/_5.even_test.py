from threading import Event

# 创建事件对象
e = Event()

e.set()  # 设置 e

e.wait()  # 此时不阻塞,若未设置set,则是阻塞状态

e.clear()  # 清除设置,变回未设置状态
print(e.is_set())  # 判断当前状态,

print("****************")


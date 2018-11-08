import gevent

def foo():
    print("Runing foo")
    gevent.sleep(2)  
    # 遇到阻塞，自动选择现有协程还有哪个可以执行，同一时间只能做一件事
    print('Runing foo again')

def bar():
    print("Runing bar")
    gevent.sleep(3) 
    print("Runing bar again")

f = gevent.spawn(foo)
g = gevent.spawn(bar)

gevent.joinall([f,g])

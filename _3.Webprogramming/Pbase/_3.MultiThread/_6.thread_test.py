from threading import Event,Thread
from time import sleep

s = None

e = Event()

def bar():
    print("Bar 拜山头")
    sleep(1)
    global s
    s = "天王盖地虎"
    e.set()

b = Thread(target = bar)
b.start()

# sleep(2)
print("说对口令你就是自己人")
e.wait()   # 等待分支线程进行完(到达e.set()前的步骤)才能进行,
if s == "天王盖地虎":
    print("确认过眼神,你是对的人")
else:
    print("打死这个人")
e.clear()

b.join()


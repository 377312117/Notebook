import threading 
from time import sleep

# 线程函数
def music():
    global a
    a = 10000
    print(a)
    for i in range(5):
        sleep(2)
        print("播放学猫叫")

# 创建线程对象
t = threading.Thread(target = music)
a = 1
t.start()
for i in range(3):

    sleep(3)
    print("播放卡路里")
t.join()

print("main thread a :", a)

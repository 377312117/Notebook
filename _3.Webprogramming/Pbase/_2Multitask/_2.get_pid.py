import os
import time
pid = os.fork()

if pid < 0:
    print("Error")
elif pid == 0:
    time.sleep(1)
    print("get PID",os.getpid())
    print("get father PID",os.getppid())     #获取父进程pid
else:
    print("Father PID",os.getpid())
    print("os.fork()",os.fork())              # 获取子进程的pid,有可能和实际的子进程pid不一样
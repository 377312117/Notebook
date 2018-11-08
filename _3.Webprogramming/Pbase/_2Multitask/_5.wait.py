#此示例示意利用wait和waitpid退出僵尸进程
import os
from time import sleep

pid = os.fork()

if pid < 0:
    print("create process failed")
elif pid == 0:
    sleep(3)
    print("Child %d process exit" % os.getpid())
    os._exit(2)
else:
    # pid,status = os.wait()
    while True:
        p,status = os.waitpid(-1,os.WNOHANG)   # 非阻塞等待,-1的话等同于wait()
        print("child pid:",p)
        print("child exit status:",os.WEXITSTATUS(status))   # 算法乘关系,status = exit中的整数乘以256
        # os.WEXITSTATUS(status)返回值为原状态2
        if p !=0:
            break
        sleep(1)
    while True:
        print("parent process")
        sleep(2)
# 创建子进程,父进程和子进程各复制一半
import os
from  time import sleep

def copy_count(f):
    size =os.path.getsize("./TCP.png")
    n = size // 2
    return n

def copy_first(f,n):
    f1 = open("copy1.png","wb")
    while True:
        data =f.read(1024)
        f1.write(data)
        n -=1024
        if n < 1024:
            f1.write(data)
            break
    f.close()
    f1.close()

def copy_second(f,n):
    f2 = open("copy2.png","wb")
    f.seek(n,0)
    while True:
        data = f.read(1024)
        if not data:
            break
        f2.write(data)
    f.close()
    f2.close()


def main():
    f =  open("./TCP.png","rb")
    n = copy_count(f)
    pid = os.fork()
    if pid < 0:
        print("创建失败")
    elif pid == 0:
        pass
        sleep(1)
        copy_second(f,n)
    else:
        pass
        copy_first(f,n)

if __name__ == "__main__":
    main()
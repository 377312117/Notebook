import os 
import time

pid = os.fork()

if pid < 0:
    print("Create process failed")
elif pid == 0:
    time.sleep(1)
    print("the new process")
else:
    print("the old process")
print ("fork test over")

# 得到结果为
# the old process     #  父进程
# fork test over      #  父进程
# the new process     #  子进程
# fork test over      #  子进程

# os.fork()创建了一个一模一样的子进程,执行顺序不确定.但是父进程创建在先,大概率会先执行
# 子进程一般都会从pid = os.fork()之后开始执行,子进程的返回值只能为0,父进程的pid由系统分配
# pid = os.fork()和if/else为固定搭配,让父子进程进行搭配,效率提高
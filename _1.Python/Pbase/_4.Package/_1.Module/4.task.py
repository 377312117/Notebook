#写一个程序,以电子时钟格式显示时间
# 格式为:
#     HH:MM:SS      如:15:58:26
import time
# while True:
#     #获取当前时间(当前时间对于计算机元年的秒数)
#     t=time.time()
#     #秒数在使用localtime函数后获得当前时间元组
#     s=time.localtime(t)
#     #每一秒显示一次
#     time.sleep(1)
#     #从元组中提取数据
#     print(s[3],":",s[4],":",s[5])
#方法2
def clock_run():
    while True:
        # 拿到当前时间元组
        t = time.localtime()
        # 显示时间
        print("%02d:%02d:%02d" % (t[3],t[4],t[5]),end="\r")
        time.sleep(1)
clock_run()
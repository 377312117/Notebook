#编写一个程序,启动时设置定时时间,到时间后打印一句"时间到!",然后退出程序
import time
# timing=float(input("请输入定时时间:"))
# time.sleep(timing)
# print("时间到")
#方法2
def alarm(h,m):
    print("闹钟设置时间为:%02d:%02d" % (h,m))
    while True:
        t = time.localtime()[3:5]
        if t == [h,m]:
            print("时间到!")
            break
        print("%02d:%02d" % (t[0],t[1]),end="\r")
        time.sleep(1)
hour=int(input("请输入小时:"))
minute=int(input("请输入分钟:"))
alarm(hour,minute)

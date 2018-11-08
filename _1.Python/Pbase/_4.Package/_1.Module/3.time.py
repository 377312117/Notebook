#写一个程序,输入你的生日,算
# 你已经出生了多少天
# 算出你出生那天是星期几
import time
# 当前时间
now_time=time.time()
# 出生时间
birthday_time=time.mktime((2018,9,17,12,0,0,0,0,0))
#两者相减
life_time=now_time-birthday_time
print(life_time/60/60//24)
t=time.localtime(birthday_time)
d={"0":1,.....}
print(d[t[6]])
# 此示例示意类变量的定义和方法
class Car:
    # 类变量,用于保存汽车对象的个数
    total_count = 0
    def.info = info 
    print("汽车",info,"被创建")
    self.__class__.total_count +=1
    # 析构方法
    def __del__(self):
        print("汽车",self.info,"被销毁")
        self.__class__.total_count -= 1
        Car.total_count -= 1
c1 = Car("BYD Y6")
c2 = Car("吉利 E7")
print("当前有%d个汽车对象"% Car.total_count)  # 2

del c2
print(Car.total_count)   # 1


# 此示例示意类变量的定义和方法
class Car:
    total_count = 0
print(Car.total_count)   # 读取类变量的值
Car.total_count += 100   # 修改类变量
print(Car.total_count)   # 100

c1 = Car()
# 实例调用变量时,先检查自身有无该变量,
# 检查完毕后再查找类变量,如类变量也没有则报错
print(c1.total_count)   # 100借助对象访问类变量

c1.total_count = 999
# 类变量可以通过此类的对象的__class__属性间接访问
c1.__class__.total_count = 88888
print(c1.total_count)     # 999
print(Car.total_count)    # 88888
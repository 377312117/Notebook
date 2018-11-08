# 此示例示意多继承的语法
class Car:
    def run(self,speed):
        print("汽车以",speed,"km/h的速度行驶")
class Plane:
    def fly(self,speed):
        print("汽车以海拔",height,"m高度飞行")

class PlaneCar(Car,Plane):
    """继承自汽车类和飞机类"""
    pass
# 此实例示意为Dog类添加吃,睡,玩等方法,以实现Dog类的相应行为
class Dog:
    """这是一种可爱的小动物"""
    def eat(self,food):  
        # self 传参到 dog1
        # food 传参到 "骨头"
        """此方法用来描述小狗吃的行为"""
        print("小狗正在吃",food)
    def sleep(self,hour):
        print("id为%d的小狗玩了%s"%(id(self),hour))
    def play(self,joy):
        print("id为%d的小狗玩了%s"%(id(self),joy))
        # return 10 可以返回一个对象的引用
dog1 = Dog()      #创建一个实例对象
dog1.eat("骨头")   #调用的是eat函数
# 方法的实质是函数,是定义在类里面的函数,和普通函数略有不同
dog2 = Dog()      #创建另一个实例对象
dog2.eat("狗粮")   #调用的是eat函数

dog1.sleep(1)
dog2.sleep(2)
dog1.play("球")
dog2.play("飞盘")
# 等同于 Dog.play(dog2,"飞盘")   第二类调用语法,不常用
# 此示例示意特例属性的用法
class Student:
    def __init__(self,s):
        self.__score = s

    @property
    def score(self):
        """getter"""
        return self.__score

    @score.setter
    def score(self,s):
        """setter"""
        assert 0<=s<=100,"成绩超出范围"
        self.__score =s
s1 = Student(59)
print(s1.get_score())
print(s1.score)     # 通过 @property 可取值
s1.score =999999   # 赋值  通过装饰器赋值
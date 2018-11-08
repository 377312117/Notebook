# 1.用一个类来描述一个学生的信息
# 姓名,年龄,成绩
# 将学生对象存于列表中
# 可以任意添加和删除学生信息
# 1.打印学生出学生的个数
# 2.打印学生的平均成绩
# 3.打印学生的平均年龄
# (建议用列表的长度来计算学生的个数)
class student:
    infos = []
    def __init__(self,n,a,s):
        self.name = n
        self.age = a
        self.score = s

    # 添加学生信息
    @classmethod
    def input_student(cls):
        while True:
            n = input("请输入姓名:")
            if not n:
                break
            a = int(input("请输入年龄:"))
            s = int(input("请输入成绩"))
            cls.infos.append(student(n,a,s))
        return cls.infos

# 删除学生信息
    @classmethod
    def del_student(cls):
        n = input("请输入要删除的学生姓名:")
        for  index , s  in enumerate(cls.infos):  # s 是学生对象,index是对应的索引值
            if s.name == n:
                del cls.infos[index]
                return
    
    @classmethod
    def get_student_count(cls):
        """1)打印学生的个数"""
        print("学生个数是:",len(cls.infos))

    @classmethod
    def print_avg_score(cls):
        """2)打印所有学生的平均成绩"""
        total_score = sum((x.score for x in cls.infos))
        print("平均成绩是:",total_score/len(cls.infos))
    
    @classmethod
    def output_student(cls):
        for s in cls.infos:
            print(s.name,s.age,s.score)

student.input_student()
student.output_student()
student.del_student()
student.output_student()
student.get_student_count()
student.print_avg_score()
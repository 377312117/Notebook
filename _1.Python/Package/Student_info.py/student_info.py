# 修改原来的学生信息管理系统,将原来用字典存储的学生信息改变用学生Student类型的对象来存储信息
# 要求:
#     1.类Student存于文件student.txt中
#     2.尽量少的在类的外部使用实例变量(建议增加方法来获取实例变量的信息)

from student import Student

# 添加学生信息
def input_studentinfo():
    L= []
    while True:
        n = input("请输入姓名:")
        if not n:
            break
        a = int(input("请输入年龄:"))
        s = int(input("请输入成绩"))
        L.append(Student(n,a,s))
    return L

# 删除学生信息
def delete_studentinfo(lst):
    n = input("请输入要删除的学生姓名:")
    for  index , s  in enumerate(lst):  # s 是学生对象,index是对应的索引值
        if s.__name == n:
            del lst[index]
            return

# 显示学生信息          
def print_studentinfo(lst):
    c1="+---------------+--------+--------+"
    c2="|     name      |   age  |  score |"
    print(c1)
    print(c2)
    print(c1)
    for  s  in lst:
        c3=s.name.center(15)
        c4=str(s.__age).center(8)
        c5=str(s.__score).center(8)
        print("|"+c3+"|"+c4+"|"+c5+"|")
    print(c1)

# 修改学生成绩
def alter_studentscore(lst):
    t1=input("请输入需要修改成绩的学员姓名:")
    t2=int(input("请输入成绩:"))
    for s in lst:
        if s.name == t1:
            s.score = t2
            print("您已修改学生%s的成绩为%s!" % (t1,t2))
            break
# 读取学生信息
def read_from_file():
    L = []
    try:
        f = open("si.txt","r")
        for line in f:
            # 去掉\n
            line =line.strip()
            items = line.split(",")
            n ,a ,s = items
            a = int (a)
            s = int (s)
            L.append(Student(n,a,s))
        f.close()
        print("读取文件成功")
    except OSError:
        print("打开文件失败")
    return L

#保存学生信息
def save_to_file(L):
    try:
        f = open("si.txt","w")
        for d in L:
            d.write_to_file(f)
        f.close()
        print("保存成功")
    except OSError:
        print("保存文件失败")

# 用来通过不同顺序查看学生的信息

def print_score_desc(l):
    def get_score(d):  # d为字典
        return d.get_age()
    # 得到排序后的列表
    lst = sorted(l, key=get_score, reverse=True)
    print_studentinfo(lst)

def print_score_asc(l):
    lst = sorted(l,
                key=lambda d:d.get_age()
                )
    print_studentinfo(lst)

def print_age_desc(l):
    lst = sorted(l,
                key=lambda d:d.get_score(),
                reverse=True
                )
    print_studentinfo(lst)

def print_age_asc(l):
    lst = sorted(l,
                key=lambda d:d.get_score()
                )
    print_studentinfo(lst)
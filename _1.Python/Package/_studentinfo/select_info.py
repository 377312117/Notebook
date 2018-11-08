# 用来通过不同顺序查看学生的信息
from print_info import print_studentinfo
def print_score_desc(l):
    def get_score(d):  # d为字典
        return d['score']
    # 得到排序后的列表
    lst = sorted(l, key=get_score, reverse=True)
    print_studentinfo(lst)

def print_score_asc(l):
    lst = sorted(l,
                 key=lambda d:d['score']
                 )
    print_studentinfo(lst)

def print_age_desc(l):
    lst = sorted(l,
                 key=lambda d:d['age'],
                 reverse=True
                 )
    print_studentinfo(lst)

def print_age_asc(l):
    lst = sorted(l,
                 key=lambda d:d['age']
                 )
    print_studentinfo(lst)

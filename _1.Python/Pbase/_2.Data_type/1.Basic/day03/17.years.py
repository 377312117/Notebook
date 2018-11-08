# 给出一个年份，判断是否为闰年
# 四年一闰，百年不闰，四百年闰
year=int(input("请输入年份："))
if (year%4==0 and year%100!=0) or year%400==0:
    print("%d年是闰年"%year)
else:
    print("%d年不是闰年"%year)
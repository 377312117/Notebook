# 算出１００－９９９之间的水仙花数（narcissistic）
# 水仙花数指百位数平方＋十位数三次方＋个位数的
# ３次方等于原数的整数
# 如：153=**3+5**3+3**3
for x in range(100,1000):
    m=x//100
    n=(x%100)//10
    l=x%10
    if x == m**3+n**3+l**3:
        print(x)
#方法２：转为字符串然后切割
#方法３：分别将百位，十位，个位分别循环
for bai in range(1,10):
    for shi in range(1,10):
        for ge in range(1,10):
            x=bai*100+shi*10+ge
            y=bai**3....
            if x==y:
                ...


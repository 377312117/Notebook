#生成一元二次方程
def get_fx(a,b,c):
    def fx(x):
        return a*x**2+b*x+c
    return fx
f234=get_fx(2,3,4)     #f234绑定一个闭包
print(f234(20))
print(f234(50))
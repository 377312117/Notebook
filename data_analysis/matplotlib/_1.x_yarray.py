import numpy as np
import matplotlib.pyplot as mp


x = [1,2,3,4,5]
y = [7,8,9,2,3]
mp.plot(x,y)
# 绘制水平线和垂直线
mp.vlines(5,0,10)
mp.hlines(5,0,10)
# 绘制一条抛物线,在[-10,10]区间中均分10个点
# x = np.linspace(-10,10,1000)
# y = x**2
# mp.plot(x,y,color='r',linewidth=5,linestyle='--')

x = np.linspace(-np.pi,np.pi,1000)
cos_x = np.cos(x)
sin_x = np.sin(x)
 


# 设置坐标轴的可视范围
mp.xlim(0,np.pi)
mp.ylim(0,2)

# 设置坐标轴的颜色和位置
ax = mp.gca()
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['left'].set_position(('data',0))
ax.spines['bottom'].set_position(('data',0))


# 绘制两个特殊点
point_x = np.pi/2
point_cos_x = np.cos(point_x)/2
point_sin_x = np.sin(point_x)
mp.scatter(point_x,point_cos_x,facecolor='limegreen',s=60,marker='D',zorder=3)
mp.scatter(point_x,point_sin_x,facecolor='limegreen',s=60,marker='*',zorder=3)

# 为特殊点添加备注
mp.annotate(
    r'$(\frac{\pi}{2},1)$',
    # 备注目标点使用的坐标系
    xycoords='data',
	# 备注目标点的坐标
    xy=(np.pi/2,1),
	# 备注文本使用的坐标系
    textcoords='offset points',
    # 备注文本的坐标
    xytext=(40,10),
    # 备注文本的字体的大小
    fontsize=14,
	# 指示箭头的属性
    arrowprops=dict(
        arrowstyle='->',
        connectionstyle='arc3'
    )
)

# 设置坐标值刻度
# 坐标值列表
x_val_list = [-np.pi,-np.pi/2,0,np.pi/2,np.pi]
# 显示坐标值列表
x_text_list = ['-π',r'$-\frac{\pi}{2}$','0',r'$\frac{\pi}{2}$','π']

mp.xticks(x_val_list,x_text_list)


# 绘制线
mp.plot(x,cos_x,color='dodgerblue',linewidth=1,linestyle='--',label=r'$y=\frac{1}{2}cos(x)$')
mp.plot(x,sin_x,color='orangered',linewidth=2,linestyle='dashdot',label=r'$y=sin(x)$')

mp.legend()
mp.show()


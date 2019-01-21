"""
刻度网格线
"""



import numpy as np
import matplotlib.pyplot as mp


y=[
    1,
    10,
    100,
    1000,
    100,
    10,
    1
]

mp.figure(
    'GridLine',
    facecolor='lightgray',
)

mp.title('GridLine',fontsize=18)
mp.xlabel('x',fontsize=14)
mp.xlabel('x',fontsize=14)

ax = mp.gca()
ax.xaxis.set_major_locator(mp.NullLocator())
ax.xaxis.set_minor_locator(mp.MultipleLocator(0.1))
ax.grid(which='major',axis='both',linewidth=0.75,color='orange')
mp.plot(y,'o-',c='dodgerblue',label='p')
mp.legend()
mp.show()
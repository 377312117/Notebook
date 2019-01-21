"""
测试刻度定位器
"""

import numpy as np
import matplotlib.pyplot as mp


locators = [
    'mp.'
]


mp.figure(
    'Locators',
    facecolor='lightgray',
)

mp.xlim(0,10)
mp.ylim(-10,10)
mp.yticks([])


ax = mp.gca()
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['left'].set_color('none')
ax.spines['bottom'].set_position(('data',0))

ax.xaxis.set_major_locator(mp.NullLocator())
ax.xaxis.set_minor_locator(mp.MultipleLocator(0.1))

mp.text(5,0.3,'NullLocator',ha='center',size=12)

mp.tight_layout()
mp.show()

import numpy as np
import matplotlib.pyplot as mp



mp.figure(
    'Sub Layout',
    figsize=(4,3),
    facecolor='lightgray',
)

mp.axes([0.1,0.2,0.5,0.8])
mp.text(
    0.5,
    0.5,
    1,
    ha='center',
    va='center',
    size=36,
    alpha=0.8
)
mp.show()
import numpy as np
import matplotlib.pyplot as mp

mp.figure(
    'Sub Layout',
    figsize=(4,3),
    facecolor='lightgray',
)

mp.subplot(3,3,1)
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
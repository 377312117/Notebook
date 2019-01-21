import numpy as np
import matplotlib.pyplot as mp


mp.figure('Pie',facecolor='lightgray')
mp.title('Pie',fontsize=18)

values = [26,17,21,29,11]
spaces = [0.05,0.01,0.01,0.02,0.01]
labels = [
    'Python',
    'JavaScript',
    'C++',
    'Java',
    'PHP'
]

colors = [
    'dodgerblue',
    'orangered',
    'lightgreen',
    'violet',
    'gold',
]


mp.pie(
    values,
    spaces,
    labels,
    colors,
    '%d%%',
    shadow=True,
    radius=1,
)


mp.legend()
mp.show()

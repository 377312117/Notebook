import numpy as np
import matplotlib.pyplot as mp

import matplotlib.gridspec as mg


gs = mg.GridSpec(3,3)
mp.subplot(gs[0,:2])
mp.text(0.5,0.5,1,va='center',ha='center',size=36)
mp.xticks([])
mp.yticks([])
mp.tight_layout()
mp.show()
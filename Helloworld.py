#%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

num = 1000
layers = 5
maxHeight = 30.0
bottom = 0.0
radian, width = np.linspace(0.0, 2.0 * np.pi * layers, num, endpoint = False, retstep = True)
height = np.linspace(maxHeight, 0.0, num, False)

ax = plt.subplot(111, projection='polar')
bars = ax.bar(radian, height, width, bottom)
for r, bar in zip(radian, bars):
    #bar.set_alpha(1.0 / layers)
    bar.set_facecolor(plt.cm.plasma(r / (2.0 * np.pi * layers)))

plt.yticks([])
plt.show()

import pylab
import random
import seaborn as sns
import os.path
import matplotlib.pyplot as plt

sampleSize = 500

x = []
y = []

for i in range(sampleSize):
    newVal = random.normalvariate(100,10)
    x.append(newVal)
    y.append(newVal / 2.0 + random.normalvariate(50,5))

font = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 16,
        }
fig = plt.figure() #para cv
ax = fig.add_subplot(1,1,1)
plt.scatter(x,y, c= sns.xkcd_rgb["light green"], marker="o", s=30,  edgecolor='black')
plt.plot([64, 129],[75,120], c="red", linewidth=3)#, linewidth=0.9)
k = ((120-75) * (100-64) - (129-64) * (100-75)) / ((120-75)^2 + (129-64)^2)
x4 = 100 - k * -400
y4 = 100 + k * -400
x5 = 100 - k * 400
y5 = 100 + k * 400
plt.plot([100, x4], [100, y4], c="red", linewidth=3)
plt.plot([100, x5], [100, y5], c="red", linewidth=3)
plt.text(0.88, 0.91, 'PC1',                                   #
            transform=ax.transAxes, fontsize=20,  fontdict=font)  #
plt.text(0.15, 0.9, 'PC2',                                   #
            transform=ax.transAxes, fontsize=20,  fontdict=font)  #

plt.tick_params(axis='x', labelsize=25) 
plt.tick_params(axis='y', labelsize=25)
plt.xlabel("X" , fontsize= 30)
plt.ylabel("Y", fontsize= 30)
plt.tight_layout()
plt.tight_layout()
pltfile = 'pca-example.pdf'
save_path = '../../Dropbox/JPAS/Tesis/Fig/'
file_save = os.path.join(save_path, pltfile)
plt.savefig(file_save)

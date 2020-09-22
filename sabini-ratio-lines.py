'''
Make color-color diagram for SPLUS
'''
from __future__ import print_function
import numpy as np
import glob
import json
import matplotlib.pyplot as plt
#import seaborn as sns
from scipy.stats import gaussian_kde
import sys
import pandas as pd
from scipy.optimize import fsolve
import seaborn as sns
import os.path

m = [6.515E-16, 1.354E-15, 3.246E-15, 2.204E-15, 6.471E-15, 9.620E-16, 1.213E-14, 7.232E-16, 1.726E-15, 9.880E-16]

i1 = np.log10(m[6] / m[7])
i2 = np.log10(m[6] / (m[8] + m[9]))
print(i2)

fig = plt.figure(figsize=(7, 6))
ax1 = fig.add_subplot(111, axisbg="#eeeeee")
ax1.set_xlim(xmin=-0.5,xmax=2.5)
ax1.set_ylim(ymin=-1.5,ymax=1.5)
#ax1.set_xlim(xmin=-2.5,xmax=2.0)
plt.tick_params(axis='x', labelsize=22) 
plt.tick_params(axis='y', labelsize=22)
plt.xlabel(r'$\log (H\alpha\ /\ [S II]\ 6716 + 6730)$', fontsize= 22)
plt.ylabel(r'$\log (H\alpha\ /\ [N II]\ 6583)$', fontsize= 22)
ax1.scatter( i2, i1, c=sns.xkcd_rgb['cerulean'], alpha=0.9, marker='*', s=400, edgecolor='black', zorder=150.0)
ax1.minorticks_on()
#ax1.grid(which='minor')#, lw=0.3)
#ax1.legend(scatterpoints=1, ncol=2, fontsize=11.0, loc='lower right', **lgd_kws)
#ax1.grid()

plt.tight_layout()
#plt.savefig('luis-JPLUS-Viironen.pdf')#,  bbox_extra_artists=(lgd,), bbox_inches='tight')
pltfile = 'ratio-sabadini.pdf'
save_path = '../../Dropbox/JPAS/paper-phot/'
file_save = os.path.join(save_path, pltfile)
plt.savefig(file_save)
#plt.savefig('Fig1-JPLUS17-Viironen.pdf')
plt.clf()

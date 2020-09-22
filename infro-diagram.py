'''
Make color-color diagram to infrered
'''
from __future__ import print_function
import numpy as np
import glob
import json
import matplotlib.pyplot as plt
import seaborn as sns
import sys

dHK, dJH = [], []
dHK1, dJH1 = [], []


dt = np.dtype([ ('Tile', 'S13'), ('Number', 'S13'),  ('J', 'f4'), ('H', 'f4'), ('K', 'f4'), ('e_J', 'f4'), ('e_H', 'f4'), ('e_K', 'f4')])
x = np.loadtxt('TWOmass-syst-cand.txt', delimiter = None, converters = None, skiprows = 0, 
                         usecols = None, unpack = False, ndmin = 0, dtype = dt)

dt1 = np.dtype([ ('Name', 'S13'),  ('J', 'f4'), ('H', 'f4'), ('K', 'f4'), ('J-H', 'f4'), ('H-Ks', 'f4')])
x1 = np.loadtxt('TWOmass-syst-known.txt', delimiter = None, converters = None, skiprows = 0, 
                         usecols = None, unpack = False, ndmin = 0, dtype = dt1)

mag1 = x['J']
mag2 = x['H']
mag3 = x['K']
d_mag1 = mag2 - mag3
d_mag2 = mag1 - mag2
dHK.append(d_mag1)
dJH.append(d_mag2)

#Symbiotic stars
mag11 = x1['J']
mag21 = x1['H']
mag31 = x1['K']
d_mag11 = mag21 - mag31
d_mag21 = mag11 - mag21
dHK1.append(d_mag11)
dJH1.append(d_mag21)


#print(columns[0])
lgd_kws = {'frameon': True, 'fancybox': True, 'shadow': True}
sns.set(style="dark")#, context="talk")
#sns.set_style('ticks')       
fig = plt.figure(figsize=(7, 6))
ax1 = fig.add_subplot(111)
ax1.set_xlim(xmin=-0.5,xmax=2.5)
ax1.set_ylim(ymin=-0.5,ymax=2.5)
plt.xlabel('H - Ks', size = 12)
plt.ylabel('J - H', size = 12)
ax1.scatter(dHK, dJH, c='green', alpha=0.8, marker ='D',  s=35, label='J-PLUS SySt candidates')
ax1.scatter(dHK1, dJH1, c='red', alpha=0.8, marker ='o',  s=35, label='Known SySt')
# for label_, x, y in zip(can_alh, dHK, dJH):
#     ax1.annotate(label_, (x, y), alpha=0.9, size=8,
#                    xytext=(3,-8), textcoords='offset points', ha='left', va='bottom',)
ax1.minorticks_on()
#ax1.grid(which='minor')#, lw=0.3)
ax1.legend(scatterpoints=1, **lgd_kws)
ax1.grid()
#sns.despine(bottom=True)
plt.tight_layout()
plt.savefig('col-infrared.pdf')

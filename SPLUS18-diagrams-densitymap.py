# -*- coding: utf-8 -*-
'''
Make color-color diagram for SPLUS form 2018 curves transmition 
'''
from __future__ import print_function
import numpy as np
import glob
import json
import matplotlib.pyplot as plt
#import seaborn as sns
import sys
from scipy.stats import gaussian_kde
import pandas as pd
from scipy.optimize import fsolve

# fit curve models
def fit(ax, x,y, sort=True): #linel
    z = np.polyfit(x, y, 1)
    fit = np.poly1d(z)
    print(fit)
    if sort:
        x = np.sort(x)
    ax.plot(x, fit(x), label="fit func", color="k", alpha=1, lw=2.5)

def fit1(ax, x,y, sort=True): #curve
    z = np.polyfit(x, y, 2)
    fit1 = np.poly1d(z)
    print(fit1)
    if sort:
        x = np.sort(x)
    ax.plot(x, fit1(x), label="fit func", color="k", alpha=1, lw=2.5)

#Find the point inteception between two lines     
def findIntersection(m, y, m1, y1, x0):
    x = np.linspace(-10.0, 15.5, 200)
    return fsolve(lambda x : (m*x + y) - (m1*x + y1), x0)

pattern = "*-spectros/*-SPLUS18-magnitude.json"
file_list = glob.glob(pattern)

def filter_mag(e, s, f1, f2, f3):
    col, col0 = [], []
    if data['id'].endswith(e):
        if data['id'].startswith(str(s)):
            filter1 = data[f1]
            filter2 = data[f2]
            filter3 = data[f3]
            diff = filter1 - filter2
            diff0 = filter1 - filter3
            col.append(diff)
            col0.append(diff0)
    
    return col, col0

def plot_mag(f1, f2, f3):
    x, y = filter_mag("HPNe", "", f1, f2, f3)
    x1, y1 = filter_mag("CV", "", f1, f2, f3)
    x2, y2 = filter_mag("E00_300", "", f1, f2, f3)
    x3, y3 = filter_mag("E01_300", "", f1, f2, f3)
    x4, y4 = filter_mag("E02_300", "", f1, f2, f3)
    x5, y5 = filter_mag("E00_600", "", f1, f2, f3)
    x6, y6 = filter_mag("E01_600", "", f1, f2, f3)
    x7, y7 = filter_mag("E02_600", "", f1, f2, f3)
    x8, y8= filter_mag("-DPNe", "", f1, f2, f3)
    x9, y9= filter_mag("QSOs-13", "", f1, f2, f3)
    x10, y10 = filter_mag("QSOs-24", "",  f1, f2, f3)
    x11, y11 = filter_mag("QSOs-32", "", f1, f2, f3)
    x12, y12 = filter_mag("-SFGs", "", f1, f2, f3)
    x13, y13 = filter_mag("-sys", "", f1, f2, f3)
    x14, y14 = filter_mag("-sys-IPHAS", "", f1, f2, f3) 
    x15, y15 = filter_mag("-ExtHII", "", f1, f2, f3)
    x16, y16 = filter_mag("-sys-Ext", '', f1, f2, f3)
    x17, y17 = filter_mag("-survey", '', f1, f2, f3)
    x18, y18 = filter_mag("-SNR", '', f1, f2, f3)
    x19, y19 = filter_mag("extr-SySt", '', f1, f2, f3)
    x20, y20 = filter_mag("-extr-SySt", '', f1, f2, f3)
    x21, y21 = filter_mag("-sys", "", f1, f2, f3)
    x22, y22 = filter_mag("-sys-IPHAS", "", f1, f2, f3)
    x23, y23 = filter_mag("ngc185", "", f1, f2, f3)
    x24, y24 = filter_mag("SySt-ic10", "", f1, f2, f3)
    x25, y25 = filter_mag("LOAN-HPNe-", "", f1, f2, f3)
    x26, y26 = filter_mag("1359559-HPNe-", "", f1, f2, f3)
    x27, y27 = filter_mag("DdDm-1-HPNe-", "", f1, f2, f3)
    x28, y28 = filter_mag("E00_100", "", f1, f2, f3)
    x29, y29 = filter_mag("E01_100", "", f1, f2, f3)
    x30, y30 = filter_mag("E02_100", "", f1, f2, f3)
    x31, y31 = filter_mag("YSOs", "", f1, f2, f3)
    # x28, y28 = filter_mag("E00_300", "", f1, f2, f3)
    # x29, y29 = filter_mag("E00_600", "", f1, f2, f3)
    x32, y32 = filter_mag("-PN_casual", "", f1, f2, f3)

    for a, b in zip(x, y):
        A1[0].append(a)
        B1[0].append(b)
    for a, b in zip(x1, y1):
        A1[1].append(a)
        B1[1].append(b)
    for a, b in zip(x2, y2):
        A1[2].append(a)
        B1[2].append(b)
    for a, b in zip(x3, y3):
        A1[2].append(a)
        B1[2].append(b)
    for a, b in zip(x4, y4):
        A1[2].append(a)
        B1[2].append(b)
    for a, b in zip(x5, y5):
        A1[2].append(a)
        B1[2].append(b)
    for a, b in zip(x6, y6):
        A1[2].append(a)
        B1[2].append(b)
    for a, b in zip(x7, y7):
        A1[2].append(a)
        B1[2].append(b)
    for a, b in zip(x8, y8):
        A1[3].append(a)
        B1[3].append(b)
    for a, b in zip(x9, y9):
        A1[4].append(a)
        B1[4].append(b)
    for a, b in zip(x10, y10):
        A1[5].append(a)
        B1[5].append(b)
    for a, b in zip(x11, y11):
        A1[6].append(a)
        B1[6].append(b)
    for a, b in zip(x12, y12):
        A1[7].append(a)
        B1[7].append(b)
    for a, b in zip(x13, y13):
        A1[8].append(a)
        B1[8].append(b)
    for a, b in zip(x14, y14):
        A1[9].append(a)
        B1[9].append(b)
    for a, b in zip(x15, y15):
        A1[10].append(a)
        B1[10].append(b)
    for a, b in zip(x16, y16):
        A1[11].append(a)
        B1[11].append(b)
    for a, b in zip(x17, y17):
        A1[12].append(a)
        B1[12].append(b)
    for a, b in zip(x18, y18):
        A1[13].append(a)
        B1[13].append(b)
    for a, b in zip(x19, y19):
        A1[14].append(a)
        B1[14].append(b)
    for a, b in zip(x20, y20):
        A1[15].append(a)
        B1[15].append(b)
    for a, b in zip(x21, y21):
        A1[16].append(a)
        B1[16].append(b)
    for a, b in zip(x22, y22):
        A1[17].append(a)
        B1[17].append(b)
    for a, b in zip(x23, y23):
        A1[18].append(a)
        B1[18].append(b)
    for a, b in zip(x24, y24):
        A1[19].append(a)
        B1[19].append(b)
    for a, b in zip(x25, y25):
        A1[20].append(a)
        B1[20].append(b)
    for a, b in zip(x26, y26):
        A1[21].append(a)
        B1[21].append(b)
    for a, b in zip(x27, y27):
        A1[22].append(a)
        B1[22].append(b)
    for a, b in zip(x28, y28):
        A1[2].append(a)
        B1[2].append(b)
    for a, b in zip(x29, y29):
        A1[2].append(a)
        B1[2].append(b)
    for a, b in zip(x30, y30):
        A1[2].append(a)
        B1[2].append(b)
    for a, b in zip(x31, y31):
        A1[23].append(a)
        B1[23].append(b)
    for a, b in zip(x32, y32):
        A1[24].append(a)
        B1[24].append(b)

label = []
label1 = ["H4-1", "PNG 135.9+55.9"]
n = 25
A1, B1 = [[] for _ in range(n)], [[] for _ in range(n)]
d_644_jplus, d_768_jplus = [], []
d_644_jplus1, d_768_jplus1 = [], []

for file_name in file_list:
    with open(file_name) as f:
        data = json.load(f)
        # if data['id'].endswith("1-HPNe"):
        #     label.append("")
        # elif data['id'].endswith("SLOAN-HPNe-"):
        #     label.append("H4-1")
        # elif data['id'].endswith("1359559-HPNe"):
        #     label.append("PNG 135.9+55.9")
        if data['id'].startswith("ngc"):
            label.append("")
        elif data['id'].startswith("mwc"):
            label.append("")
        plot_mag("F625_R", "F660", "F766_I")
        
AB = np.vstack([A1[2],B1[2]])
z = gaussian_kde(AB)(AB)
df=pd.DataFrame({'x': np.array(B1[2]), 'y': np.array(A1[2]) })
print(len(A1[2]))
# Sort the points by density, so that the densest points are plotted last
idx = z.argsort()
x, y, z = np.array(A1[2])[idx], np.array(B1[2])[idx], z[idx]

# PN in HASH and S-PLUS Fr

mag=[13.61, 13.74, 13.81, 13.79, 13.85, 14.11, 14.17, 14.55, 14.67, 14.96, 15.2, 15.28]

colx = mag[7]-mag[9]
coly = mag[7]-mag[8]

lgd_kws = {'frameon': True, 'fancybox': True, 'shadow': True}
#sns.set(style="dark", context="talk")
#sns.set_style('ticks')
fig = plt.figure(figsize=(7, 6))
ax1 = fig.add_subplot(111, axisbg="#eeeeee")
ax1.set_xlim(xmin=-2.8,xmax=2.8)
ax1.set_ylim(ymin=-0.6,ymax=2.5)
#ax1.set_xlim(xmin=-2.5,xmax=2.0)
plt.tick_params(axis='x', labelsize=22) 
plt.tick_params(axis='y', labelsize=22)
plt.xlabel(r'$r - i$', fontsize=22)
plt.ylabel(r'$r - J0660$', fontsize=22)
#plt.plot( 'x', 'y', data=df, linestyle='', marker='o')
ax1.scatter(y, x, c=z, s=50, edgecolor='')
ax1.scatter(B1[0], A1[0], c='black', alpha=0.8, s=40, label='Obs. halo PNe')
(_, caps, _) = ax1.errorbar(B1[0], A1[0], xerr=0.0, yerr=0.0, marker='.', fmt='k.', elinewidth=0.8, markeredgewidth=0.8, markersize=8,)
for cap in caps:
    cap.set_markeredgewidth(1)

ax1.scatter(B1[20], A1[20], c='black', alpha=0.8, s=40)#, label='Obs. halo PNe')
ax1.errorbar(B1[20], A1[20], yerr=0.2,  lolims= True,  marker='.', fmt='k.', elinewidth=.8, markeredgewidth=.8, markersize=8,)
ax1.errorbar(B1[20], A1[20], xerr=0.2,  xuplims= True,  marker='.', fmt='k.', elinewidth=.8, markeredgewidth=.8, markersize=8,)

ax1.scatter(B1[21], A1[21], c='black', alpha=0.8, s=40)
(_, caps, _) = ax1.errorbar(B1[21], A1[21], xerr=0.0, yerr=0.0, marker='.', fmt='k.', elinewidth=0.8, markeredgewidth=0.8, markersize=8,)
for cap in caps:
    cap.set_markeredgewidth(1)
ax1.scatter(B1[22], A1[22], c='black', alpha=0.8, s=40)
(_, caps, _) = ax1.errorbar(B1[22], A1[22], xerr=0.0, yerr=0.0, marker='.', fmt='k.', elinewidth=0.8, markeredgewidth=0.8, markersize=8,)
for cap in caps:
    cap.set_markeredgewidth(1)

ax1.scatter(B1[1], A1[1], c='purple', alpha=0.6, s=40, label='SDSS CVs')
ax1.scatter(B1[4], A1[4],  c= "mediumaquamarine" , alpha=0.6, s=40, marker='D',  label='SDSS QSOs')
ax1.scatter(B1[5], A1[5],  c= "mediumaquamarine", alpha=0.6, s=40, marker='D')#,  label='SDSS QSOs (2.4<z<2.6)')
ax1.scatter(B1[6], A1[6],  c= "mediumaquamarine", alpha=0.6, s=40, marker='D')#,  label='SDSS QSOs (3.2<z<3.4)')
ax1.scatter(B1[7], A1[7],  c= "goldenrod", alpha=0.6, s=38, marker='^', label='SDSS SFGs ')
ax1.scatter(B1[8], A1[8],  facecolors='none', edgecolors='red', alpha=0.6, s=40, marker='s')#, label='Obs. SySts ')
ax1.scatter(B1[16], A1[16],  c= "red", alpha=0.6, s=40, marker='s', label='Obs. SySts ')
#ax1.scatter(B1[72], A1[72],  c= "red", alpha=0.8, marker='D', label='Symbiotics in NGC 55')
ax1.scatter(B1[14], A1[14],  c= "red", alpha=0.6, s=40, marker='D', label='Obs. SySts in NGC 205')
ax1.scatter(B1[15], A1[15],  facecolors='none', edgecolors='red', alpha=0.6, s=40, marker='D')  #label=' SySts in NGC 205')
ax1.scatter(B1[9], A1[9],  facecolors='none', edgecolors='red', alpha=0.6, s=40, marker='^')#,  label='IPHAS SySts')
ax1.scatter(B1[17], A1[17],  c= "red", alpha=0.6, s=40, marker='^', label='IPHAS SySts')
ax1.scatter(B1[19], A1[19],  facecolors='none', edgecolors='red', alpha=0.8, s=38, marker='o',  label='Obs. SySts in IC10 ')
ax1.scatter(B1[18], A1[18],  c= "red", alpha=0.6, s=40, marker='v', label=' Obs. SySts in NGC 185')
#ax1.scatter(B1[73], A1[73],  c= "red", alpha=0.8, marker='o', label='C. Buil Symbiotics')
ax1.scatter(B1[10], A1[10],  c= "gray", alpha=0.8, marker='D', label='Obs. HII region in NGC 55')
ax1.scatter(B1[23], A1[23],  c= "lightsalmon", alpha=0.8, s=42, marker='*', label='Obs. YSOs')
ax1.scatter(B1[24], A1[24],  c= "red", alpha=0.9, s=100, marker='*', label='PN casual')
#ax1.scatter(colx, coly,  c= "red", alpha=0.8, s=300, marker='*', label='HASH PN')
#ax1.scatter(B1[74], A1[74],  c= "black", alpha=0.8, marker='.', label='SN Remanents')


for label_, x, y in zip(label, B1[0], A1[0]):
    ax1.annotate(label_, (x, y), alpha=5, size=8,
                   xytext=(-4.0, 3.6), textcoords='offset points', ha='right', va='bottom',)
###################################################################
# ax1.annotate("H4-1", (np.array(B1[139]), np.array(A1[139])), alpha=5, size=8,
#                    xytext=(-5, -10), textcoords='offset points', ha='right', va='bottom',)
# ax1.annotate("PNG 135.9+55.9", (np.array(B1[140]), np.array(A1[140])), alpha=5, size=8,
#                    xytext=(-5, -10), textcoords='offset points', ha='right', va='bottom',)
# ax1.annotate("DdDm-1", (np.array(B1[141]), np.array(A1[141])), alpha=10, size=8,
#                    xytext=(35, -10), textcoords='offset points', ha='right', va='bottom',)
##################################################################
#Obersevado porJPLUS
#for label_, x, y in zip(label1, d_768_jplus[0], d_644_jplus[0]):
# ax1.annotate("H4-1", (d_768_jplus[0], d_644_jplus[0]), alpha=8, size=8,
#                    xytext=(-5, 3), textcoords='offset points', ha='right', va='bottom', color='blue',)

# ax1.annotate("PNG 135.9+55.9", (d_768_jplus[1], d_644_jplus[1]), alpha=8, size=8,
#                    xytext=(68, -10), textcoords='offset points', ha='right', va='bottom', color='green',)

# ax1.annotate("CI Cyg", (d_768_jplus[2], d_644_jplus[2]), alpha=20, size=8,
#                    xytext=(-5, 3), textcoords='offset points', ha='right', va='bottom', color='yellow',)

# ax1.annotate("TX CVn", (d_768_jplus[3], d_644_jplus[3]), alpha=20, size=8,
#                    xytext=(18, -13), textcoords='offset points', ha='right', va='bottom', color='m',)


#for label_, x, y in zip(can_alh, d_768_cAlh, d_644_cAlh):
    #ax1.annotate(label_, (x, y), alpha=0.9, size=8,
                   #xytext=(3,-10), textcoords='offset points', ha='left', va='bottom',)
# plt.annotate(
#     '', xy=(B1[2][0],  A1[2][0]+0.35), xycoords='data',                    #
#     xytext=(B1[42][0]+0.4, A1[42][0]+0.4), textcoords='data', fontsize = 7,# vector extinction
#     arrowprops=dict(edgecolor='black',arrowstyle= '<-'))                   #
# plt.annotate(
#     '', xy=(B1[2][0]+0.35,  A1[2][0]+0.35), xycoords='data',
#     xytext=(5, 0), textcoords='offset points', fontsize='x-small')

#fit1(ax1, B1[2], A1[2]) # curve fit: -0.7744 x**2 - 2.605 x + 0.2183 

# t = np.linspace(-3.0, 0.5, 200)
# m = -0.8*t**2 - 2.8*t + 0.35 >= 0.2206
# tt = -0.8*t**2 - 2.8*t + 0.35
# ax1.plot(t[m], tt[m], c="r")

# Region where are located the PNe
result = findIntersection(0.43, 0.65, -6.8, -1.3, 0.0)
result_y = 8.0*result + 4.50

x_new = np.linspace(-15.0, result, 200)
x_new2 = np.linspace(-15.0, result, 200)
#x_new3 = np.linspace(-10.0, 1.1, 200)
y =  0.43*x_new + 0.65
yy = -6.8*x_new2 - 1.3

#Mask
#mask = y >= result_y - 0.5
ax1.plot(x_new, y, color='k', linestyle='-')
ax1.plot(x_new2, yy , color='k', linestyle='-')

#Viironen
x_new4 = np.linspace(-10.0, 11.1, 200)
y_v =  0.25*x_new4 + 1.9
ax1.plot(x_new4, y_v, color='k', linestyle='--')

# Region of the simbiotic stars
result1 = findIntersection(-220, +40.4, 0.39, 0.73, 0.0)
x_new_s = np.linspace(-15.5, result1, 200)
x_new2_s = np.linspace(result1, 15.5, 200)
y_s = -220*x_new_s + 40.4
yy_s = 0.39*x_new2_s + 0.73

ax1.plot(x_new_s, y_s, color='r', linestyle='--')
ax1.plot(x_new2_s, yy_s , color='r', linestyle='--')


#for Z, x, y in zip(z, d_768_Qz, d_644_Qz):
    #ax1.annotate("{:.3f}".format(Z), (x, y), fontsize='x-small',
                       #xytext=(5,-5), textcoords='offset points', ha='left', bbox={"boxstyle": "round", "fc": "white", "ec": "none", "alpha": 0.5}, alpha=0.7)
#ax1.set_title(" ".join([cmd_args.source]))
#ax1.grid(True)
#ax1.annotate('Higher z(3.288)', xy=(0.08749580383300781, 0.181182861328125), xytext=(-0.5, -0.58),
             #arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))
#ax1.annotate('Lower z(3.065)', xy=(0.3957328796386719, 0.1367034912109375), xytext=(0.5, -0.58),
             #arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))
ax1.minorticks_on()
#ax1.grid(which='minor')#, lw=0.3)
ax1.legend(scatterpoints=1, ncol=1, fontsize=9.0, loc='center left', **lgd_kws)
#ax1.grid()
#lgd = ax1.legend(loc='center right', bbox_to_anchor=(1.27, 0.5), fontsize=7.5, **lgd_kws)
#ax1.grid(which='minor', lw=0.5)
#sns.despine(bottom=True)
plt.tight_layout()
#plt.savefig('luis-JPLUS-Viironen.pdf')#,  bbox_extra_artists=(lgd,), bbox_inches='tight')
plt.savefig('Fig1-SPLUS18-Viironen-densitymap.pdf')
plt.clf()
sys.exit()
##########################################################################################################################################
label = []
label1 = ["H4-1", "PNG 135.9+55.9"]
n = 24
A1, B1 = [[] for _ in range(n)], [[] for _ in range(n)]
d_644_jplus, d_768_jplus = [], []
d_644_jplus1, d_768_jplus1 = [], []

for file_name in file_list:
    with open(file_name) as f:
        data = json.load(f)
        # if data['id'].endswith("1-HPNe"):
        #     label.append("")
        # elif data['id'].endswith("SLOAN-HPNe-"):
        #     label.append("H4-1")
        # elif data['id'].endswith("1359559-HPNe"):
        #     label.append("PNG 135.9+55.9")
        if data['id'].startswith("ngc"):
            label.append("NGC 2242")
        elif data['id'].startswith("mwc"):
            label.append("MWC 574")
        plot_mag("F515", "F660", "F861")
        
AB = np.vstack([A1[2],B1[2]])
z = gaussian_kde(AB)(AB)
df=pd.DataFrame({'x': np.array(B1[2]), 'y': np.array(A1[2]) })

# Sort the points by density, so that the densest points are plotted last
idx = z.argsort()
x, y, z = np.array(A1[2])[idx], np.array(B1[2])[idx], z[idx]

# Canditade find in the JPLUS data
colx2 = mag[6]-mag[10]
coly2 = mag[6]-mag[8]

lgd_kws = {'frameon': True, 'fancybox': True, 'shadow': True}
#sns.set(style="dark", context="talk")
#sns.set_style('ticks')
fig = plt.figure(figsize=(7, 6))
ax2 = fig.add_subplot(111, axisbg="#eeeeee")
ax2.set_xlim(xmin=-2.5,xmax=5.5)
ax2.set_ylim(ymin=-2.0,ymax=5.0)
#ax2.set_xlim(xmin=-2.5,xmax.=2.0)
plt.tick_params(axis='x', labelsize=22) 
plt.tick_params(axis='y', labelsize=22)
plt.xlabel(r'$J0515 - J0861$', fontsize= 22)                 # "F515", "F660", "F861"
plt.ylabel(r'$J0515 - J0660$', fontsize= 22)
#ax2.plot( 'x', 'y', data=df, alpha= 0.5, linestyle='', marker='o')
ax2.scatter(y, x, c=z, s=50, edgecolor='')
ax2.scatter(B1[0], A1[0], c='black', alpha=0.8, s=40, cmap=plt.cm.hot, label='Obs. halo PNe')
(_, caps, _) = ax2.errorbar(B1[0], A1[0], xerr=0.0, yerr=0.0, marker='.', fmt='k.', elinewidth=0.8, markeredgewidth=0.8, markersize=8,)
for cap in caps:
    cap.set_markeredgewidth(1)

ax2.scatter(B1[20], A1[20], c='black', alpha=0.8, s=40, cmap=plt.cm.hot)#, label='Obs. halo PNe')
ax2.errorbar(B1[20], A1[20], yerr=0.3,  lolims= True,  marker='.', fmt='k.', elinewidth=.8, markeredgewidth=.8, markersize=8,)
#ax2.errorbar(B1[20], A1[20], xerr=0.2,  xuplims= True,  marker='.', fmt='k.', elinewidth=.8, markeredgewidth=.8, markersize=8,)

ax2.scatter(B1[21], A1[21], c='black', alpha=0.8, s=40, cmap=plt.cm.hot)
(_, caps, _) = ax2.errorbar(B1[21], A1[21], xerr=0.0, yerr=0.0, marker='.', fmt='k.', elinewidth=0.8, markeredgewidth=0.8, markersize=8,)
for cap in caps:
    cap.set_markeredgewidth(1)
ax2.scatter(B1[22], A1[22], c='black', alpha=0.8, s=40)
(_, caps, _) = ax2.errorbar(B1[22], A1[22], xerr=0.0, yerr=0.0, marker='.', fmt='k.', elinewidth=0.8, markeredgewidth=0.8, markersize=8,)
for cap in caps:
    cap.set_markeredgewidth(1)

ax2.scatter(B1[1], A1[1], c='purple', alpha=0.6, s=40, cmap=plt.cm.hot, label='SDSS CVs')
ax2.scatter(B1[4], A1[4],  c= "mediumaquamarine" , alpha=0.6, s=40, marker='D', cmap=plt.cm.hot, label='SDSS QSOs')
ax2.scatter(B1[5], A1[5],  c= "mediumaquamarine", alpha=0.6, s=40, marker='D', cmap=plt.cm.hot)#, label='SDSS QSOs (2.4<z<2.6)')
ax2.scatter(B1[6], A1[6],  c= "mediumaquamarine", alpha=0.6, s=40, marker='D', cmap=plt.cm.hot)#, label='SDSS QSOs (3.2<z<3.4)')
ax2.scatter(B1[7], A1[7],  c= "goldenrod", alpha=0.6, s=40, marker='^', cmap=plt.cm.hot, label='SDSS SFGs ')
ax2.scatter(B1[8], A1[8],  c= "red", alpha=0.6, s=40, marker='s', cmap=plt.cm.hot)#, label='Obs. SySts ')
ax2.scatter(B1[16], A1[16],  c= "red", alpha=0.6, s=40, marker='s', cmap=plt.cm.hot, label='Obs. SySts ')
#ax2.scatter(B1[72], A1[72],  c= "red", alpha=0.8, marker='D', label='Symbiotics in NGC 55')
ax2.scatter(B1[14], A1[14],  c= "red", alpha=0.6, s=40, marker='D', cmap=plt.cm.hot, label='Obs. SySts in NGC 205')
ax2.scatter(B1[15], A1[15],  c= "red", alpha=0.6, s=40, marker='D', cmap=plt.cm.hot)  #label=' SySts in NGC 205')
ax2.scatter(B1[9], A1[9],  c= "red", alpha=0.6, s=40, marker='^', cmap=plt.cm.hot)#,  label='IPHAS SySts')
ax2.scatter(B1[17], A1[17],  c= "red", alpha=0.6, s=40, marker='^', cmap=plt.cm.hot, label='IPHAS SySts')
ax2.scatter(B1[19], A1[19],  c= "red", alpha=0.6, s=40, marker='o', cmap=plt.cm.hot, label='Obs. SySts in IC10 ')
ax2.scatter(B1[18], A1[18],  c= "red", alpha=0.6, s=40, marker='v', cmap=plt.cm.hot, label='Obs. SySts in NGC 185')
#ax2.scatter(B1[73], A1[73],  c= "red", alpha=0.8, marker='o', label='C. Buil Symbiotics')
ax2.scatter(B1[10], A1[10],  c= "gray", alpha=0.6, s=40, marker='D', cmap=plt.cm.hot, label='Obs. HII region in NGC 55')
ax2.scatter(B1[23], A1[23],  c= "lightsalmon", alpha=0.6, s=42, marker='*', label='Obs. YSOs')
#ax2.scatter(B1[74], A1[74],  c= "black", alpha=0.8, marker='.', label='SN Remanents')
#ax2.scatter(colx2, coly2,  c= "red", alpha=0.8, s=300, marker='*', label='HASH PN')

for label_, x, y in zip(label, B1[0], A1[0]):
    ax2.annotate(label_, (x, y), alpha=5, size=8,
                   xytext=(-4.0, 2.6), textcoords='offset points', ha='right', va='bottom',)
###################################################################
ax2.annotate("H4-1", (np.array(B1[20]), np.array(A1[20])), alpha=5, size=8,
                   xytext=(25.3, -10), textcoords='offset points', ha='right', va='bottom',)
ax2.annotate("PNG 135.9+55.9", (np.array(B1[21]), np.array(A1[21])), alpha=5, size=8,
                   xytext=(-5, -10), textcoords='offset points', ha='right', va='bottom',)
ax2.annotate("DdDm-1", (np.array(B1[22]), np.array(A1[22])), alpha=10, size=8,
                   xytext=(-4.5, -8), textcoords='offset points', ha='right', va='bottom',)
##################################################################
#Obersevado porJPLUS
#for label_, x, y in zip(label1, d_768_jplus[0], d_644_jplus[0]):
# ax2.annotate("H4-1", (d_768_jplus[0], d_644_jplus[0]), alpha=8, size=8,
#                    xytext=(-5, 3), textcoords='offset points', ha='right', va='bottom', color='blue',)

# ax2.annotate("PNG 135.9+55.9", (d_768_jplus[1], d_644_jplus[1]), alpha=8, size=8,
#                    xytext=(68, -10), textcoords='offset points', ha='right', va='bottom', color='green',)

# ax2.annotate("CI Cyg", (d_768_jplus[2], d_644_jplus[2]), alpha=20, size=8,
#                    xytext=(-5, 3), textcoords='offset points', ha='right', va='bottom', color='yellow',)

# ax2.annotate("TX CVn", (d_768_jplus[3], d_644_jplus[3]), alpha=20, size=8,
#                    xytext=(18, -13), textcoords='offset points', ha='right', va='bottom', color='m',)


# Region where are located the PNe
result = findIntersection(2.7, 2.15, 0.0, 0.22058956, 0.0)
result_y = 2.5*result + 2.15

x_new = np.linspace(result, 15.5, 200)
x_new2 = np.linspace(-10.0, result, 200)
x_new3 = np.linspace(-10.0, 10.0, 200)
y = 2.7*x_new + 2.15
yy = 0.0*x_new2 + 0.22058956
#Mask
#mask = y >= result_y - 0.5
ax2.plot(x_new, y, color='k', linestyle='-')
ax2.plot(x_new2, yy , color='k', linestyle='-')

# Region of the simbiotic stars
result1 = findIntersection(5.5, -6.45, 0.98, -0.16, 0.0)
x_new_s = np.linspace(result1, 15.5, 200)
x_new2_s = np.linspace(result1, 15.5, 200)
y_s = 5.5*x_new_s - 6.45
yy_s = 0.98*x_new2_s - 0.16

ax2.plot(x_new_s, y_s, color='r', linestyle='--')
ax2.plot(x_new2_s, yy_s , color='r', linestyle='--')

#fit(ax2, B1[2], A1[2]) # lineal fit: 0.8953 x + 3.556

# t = np.linspace(-3.0, 5.5, 200)
# tt = 2.5*t + 2.15
# m = tt >= 0.22058956
# ax2.plot(t[m], tt[m], color="k", linestyle='-')
# ax2.axhline(y=0.22058956, color='k', linestyle='-')

#for Z, x, y in zip(z, d_768_Qz, d_644_Qz):
    #ax2.annotate("{:.3f}".format(Z), (x, y), fontsize='x-small',
                       #xytext=(5,-5), textcoords='offset points', ha='left', bbox={"boxstyle": "round", "fc": "white", "ec": "none", "alpha": 0.5}, alpha=0.7)
#ax2.set_title(" ".join([cmd_args.source]))
#ax2.grid(True)
#ax2.annotate('Higher z(3.288)', xy=(0.08749580383300781, 0.181182861328125), xytext=(-0.5, -0.58),
             #arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))
#ax2.annotate('Lower z(3.065)', xy=(0.3957328796386719, 0.1367034912109375), xytext=(0.5, -0.58),
             #arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))
#ax2.minorticks_on()
#ax2.grid(which='minor')#, lw=0.3)
ax2.legend(scatterpoints=1, ncol=1, fontsize=10.0, loc='lower right', **lgd_kws)
#ax2.grid()
#lgd = ax2.legend(loc='center right', bbox_to_anchor=(1.27, 0.5), fontsize=7.5, **lgd_kws)
#ax2.grid(which='minor', lw=0.5)
#sns.despine(bottom=True)
#plt.tight_layout()
#plt.savefig('luis-JPLUS-Viironen.pdf')#,  bbox_extra_artists=(lgd,), bbox_inches='tight')
plt.tight_layout()
plt.savefig('Fig2-SPLUS18-j0515-halpha-densitymap.jpg')
plt.clf()

##########################################################################################################################################
label = []
label1 = ["H4-1", "PNG 135.9+55.9"]
n = 24
A1, B1 = [[] for _ in range(n)], [[] for _ in range(n)]
d_644_jplus, d_768_jplus = [], []
d_644_jplus1, d_768_jplus1 = [], []

for file_name in file_list:
    with open(file_name) as f:
        data = json.load(f)
        # if data['id'].endswith("1-HPNe"):
        #     label.append("")
        # elif data['id'].endswith("SLOAN-HPNe-"):
        #     label.append("H4-1")
        # elif data['id'].endswith("1359559-HPNe"):
        #     label.append("PNG 135.9+55.9")
        if data['id'].startswith("ngc"):
            label.append("NGC 2242")
        elif data['id'].startswith("mwc"):
            label.append("MWC 574")
        plot_mag("F910_zSDSS", "F660", "F480_gSDSS")
        
AB = np.vstack([A1[2],B1[2]])
z = gaussian_kde(AB)(AB)
df=pd.DataFrame({'x': np.array(B1[2]), 'y': np.array(A1[2]) })
print(AB)


# Sort the points by density, so that the densest points are plotted last
idx = z.argsort()
x, y, z = np.array(A1[2])[idx], np.array(B1[2])[idx], z[idx]

# Canditade find in the JPLUS data
colx3 = mag[11]-mag[5]
coly3 = mag[11]-mag[8]

lgd_kws = {'frameon': True, 'fancybox': True, 'shadow': True}
#sns.set(style="dark", context="talk")
#sns.set_style('ticks')
fig = plt.figure(figsize=(7, 6))
ax3 = fig.add_subplot(111, axisbg="#eeeeee")
ax3.set_xlim(xmin=-5.8,xmax=2.5)
ax3.set_ylim(ymin=-3.0,ymax=5.0)
#ax3.set_xlim(xmin=-2.5,xmax=2.0)
plt.tick_params(axis='x', labelsize=20) 
plt.tick_params(axis='y', labelsize=20)
plt.xlabel(r'$zSDSS - gSDSS$', fontsize= 20)
plt.ylabel(r'$zSDSS - J0660$', fontsize= 20)
#ax3.plot( 'x', 'y', data=df, alpha= 0.5, linestyle='', marker='o')
ax3.scatter(y, x, c=z, s=50, edgecolor='')
ax3.scatter(B1[0], A1[0], c='black', alpha=0.8, s=40, cmap=plt.cm.hot, label='Obs. halo PNe')
(_, caps, _) = ax3.errorbar(B1[0], A1[0], xerr=0.0, yerr=0.0, marker='.', fmt='k.', elinewidth=0.8, markeredgewidth=0.8, markersize=8,)
for cap in caps:
    cap.set_markeredgewidth(1)

ax3.scatter(B1[20], A1[20], c='black', alpha=0.8, s=40, cmap=plt.cm.hot)#, label='Obs. halo PNe')
ax3.errorbar(B1[20], A1[20], yerr=0.3,  lolims= True,  marker='.', fmt='k.', elinewidth=.8, markeredgewidth=.8, markersize=8,)
ax3.errorbar(B1[20], A1[20], xerr=0.3,  xlolims= True,  marker='.', fmt='k.', elinewidth=.8, markeredgewidth=.8, markersize=8,)

ax3.scatter(B1[21], A1[21], c='black', alpha=0.8, s=40, cmap=plt.cm.hot)
(_, caps, _) = ax3.errorbar(B1[21], A1[21], xerr=0.0, yerr=0.0, marker='.', fmt='k.', elinewidth=0.8, markeredgewidth=0.8, markersize=8,)
for cap in caps:
    cap.set_markeredgewidth(1)
ax3.scatter(B1[22], A1[22], c='black', alpha=0.8, s=40)
(_, caps, _) = ax3.errorbar(B1[22], A1[22], xerr=0.0, yerr=0.0, marker='.', fmt='k.', elinewidth=0.8, markeredgewidth=0.8, markersize=8,)
for cap in caps:
    cap.set_markeredgewidth(1)

ax3.scatter(B1[1], A1[1], c='purple', alpha=0.6, s=40, cmap=plt.cm.hot, label='SDSS CVs')
ax3.scatter(B1[4], A1[4],  c= "mediumaquamarine" , alpha=0.6, s=40, marker='D', cmap=plt.cm.hot, label='SDSS QSOs')
ax3.scatter(B1[5], A1[5],  c= "mediumaquamarine", alpha=0.6, s=40, marker='D', cmap=plt.cm.hot)#, label='SDSS QSOs (2.4<z<2.6)')
ax3.scatter(B1[6], A1[6],  c= "mediumaquamarine", alpha=0.6, s=40, marker='D', cmap=plt.cm.hot)#, label='SDSS QSOs (3.2<z<3.4)')
ax3.scatter(B1[7], A1[7],  c= "goldenrod", alpha=0.6, s=40, marker='^', cmap=plt.cm.hot, label='SDSS SFGs ')
ax3.scatter(B1[8], A1[8],  c= "red", alpha=0.6, s=40, marker='s', cmap=plt.cm.hot)#, label='Obs. SySts ')
ax3.scatter(B1[16], A1[16],  c= "red", alpha=0.6, s=40, marker='s', cmap=plt.cm.hot, label='Obs. SySts ')
#ax3.scatter(B1[72], A1[72],  c= "red", alpha=0.8, marker='D', label='Symbiotics in NGC 55')
ax3.scatter(B1[14], A1[14],  c= "red", alpha=0.6, s=40, marker='D', cmap=plt.cm.hot, label='Obs. SySts in NGC 205')
ax3.scatter(B1[15], A1[15],  c= "red", alpha=0.6, s=40, marker='D', cmap=plt.cm.hot)  #label=' SySts in NGC 205')
ax3.scatter(B1[9], A1[9],  c= "red", alpha=0.6, s=40, marker='^', cmap=plt.cm.hot)#,  label='IPHAS SySts')
ax3.scatter(B1[17], A1[17],  c= "red", alpha=0.6, s=40, marker='^', cmap=plt.cm.hot, label='IPHAS SySts')
ax3.scatter(B1[19], A1[19],  c= "red", alpha=0.6, s=40, marker='o', cmap=plt.cm.hot, label='Obs. SySts in IC10 ')
ax3.scatter(B1[18], A1[18],  c= "red", alpha=0.6, s=40, marker='v', cmap=plt.cm.hot, label='Obs. SySts in NGC 185')
#ax3.scatter(B1[73], A1[73],  c= "red", alpha=0.8, marker='o', label='C. Buil Symbiotics')
ax3.scatter(B1[10], A1[10],  c= "gray", alpha=0.6, s=40, marker='D', cmap=plt.cm.hot, label='Obs. HII region in NGC 55')
ax3.scatter(B1[23], A1[23],  c= "lightsalmon", alpha=0.6, s=42, marker='*', label='Obs. YSOs')
#ax3.scatter(B1[74], A1[74],  c= "black", alpha=0.8, marker='.', label='SN Remanents')
#ax3.scatter(colx3, coly3,  c= "red", alpha=0.8, s=300, marker='*', label='HASH PN')    

for label_, x, y in zip(label, B1[0], A1[0]):
    ax3.annotate(label_, (x, y), alpha=5, size=8,
                   xytext=(-4.0, -5.0), textcoords='offset points', ha='right', va='bottom',)
###################################################################
ax3.annotate("H4-1", (np.array(B1[20]), np.array(A1[20])), alpha=5, size=8,
                   xytext=(25.3, -10), textcoords='offset points', ha='right', va='bottom',)
ax3.annotate("PNG 135.9+55.9", (np.array(B1[21]), np.array(A1[21])), alpha=5, size=8,
                   xytext=(65.0, -10), textcoords='offset points', ha='right', va='bottom',)
ax3.annotate("DdDm-1", (np.array(B1[22]), np.array(A1[22])), alpha=10, size=8,
                   xytext=(-4.5, -8), textcoords='offset points', ha='right', va='bottom',)
##################################################################
#Obersevado porJPLUS
#for label_, x, y in zip(label1, d_768_jplus[0], d_644_jplus[0]):
# ax3.annotate("H4-1", (d_768_jplus[0], d_644_jplus[0]), alpha=8, size=8,
#                    xytext=(-5, 3), textcoords='offset points', ha='right', va='bottom', color='blue',)

# ax3.annotate("PNG 135.9+55.9", (d_768_jplus[1], d_644_jplus[1]), alpha=8, size=8,
#                    xytext=(68, -10), textcoords='offset points', ha='right', va='bottom', color='green',)

# ax3.annotate("CI Cyg", (d_768_jplus[2], d_644_jplus[2]), alpha=20, size=8,
#                    xytext=(-5, 3), textcoords='offset points', ha='right', va='bottom', color='yellow',)

# ax3.annotate("TX CVn", (d_768_jplus[3], d_644_jplus[3]), alpha=20, size=8,
#                    xytext=(18, -13), textcoords='offset points', ha='right', va='bottom', color='m',)

#fit(ax3, B1[2], A1[2]) # lineal fit: 0.2316 x + 2.825

# t = np.linspace(-6.0, 3.5, 200)
# ttx = 0.2319*t + 0.85
# tty = -1.3*t + 1.7
# ax3.plot(t, ttx, color="k", linestyle='-')
# ax3.plot(t, tty, color="k", linestyle='-')

# Region where stay the PNe
result = findIntersection(0.2319, 0.85, -1.3, 1.7, 0.0)
result_y = 0.2319*result + 0.85

x_new = np.linspace(result, 15.5, 200)
x_new2 = np.linspace(-10.0, result, 200)

y = 0.2319*x_new + 0.85
yy = -1.3*x_new2 +  1.7
#Mask
#mask = y >= result_y - 0.5
ax3.plot(x_new, y, color='k', linestyle='-')
ax3.plot(x_new2, yy , color='k', linestyle='-')

# Region of the simbiotic stars=>
result1 = findIntersection(-1.96, -3.15, 0.2, 0.44, 0.0)
x_new_s = np.linspace(-15.5, result1, 200)
x_new2_s = np.linspace(-15.5, result1, 200)
y_s = -1.96*x_new_s - 3.15
yy_s = 0.2*x_new2_s + 0.44

ax3.plot(x_new_s, y_s, color='r', linestyle='--')
ax3.plot(x_new2_s, yy_s , color='r', linestyle='--')



#for Z, x, y in zip(z, d_768_Qz, d_644_Qz):
    #ax3.annotate("{:.3f}".format(Z), (x, y), fontsize='x-small',
                       #xytext=(5,-5), textcoords='offset points', ha='left', bbox={"boxstyle": "round", "fc": "white", "ec": "none", "alpha": 0.5}, alpha=0.7)
#ax3.set_title(" ".join([cmd_args.source]))
#ax3.grid(True)
#ax3.annotate('Higher z(3.288)', xy=(0.08749580383300781, 0.181182861328125), xytext=(-0.5, -0.58),
             #arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))
#ax3.annotate('Lower z(3.065)', xy=(0.3957328796386719, 0.1367034912109375), xytext=(0.5, -0.58),
             #arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))
#ax3.minorticks_on()
#ax3.grid(which='minor')#, lw=0.3)
ax3.legend(scatterpoints=1, ncol=1, fontsize=10.0, loc='upper left', **lgd_kws)
#ax3.grid()
#lgd = ax3.legend(loc='center right', bbox_to_anchor=(1.27, 0.5), fontsize=7.5, **lgd_kws)
#ax3.grid(which='minor', lw=0.5)
#sns.despine(bottom=True)
#plt.tight_layout()
#plt.savefig('luis-JPLUS-Viironen.pdf')#,  bbox_extra_artists=(lgd,), bbox_inches='tight')
plt.tight_layout()
plt.savefig('Fig3-SPLUS18-z-g-densitymap.pdf')
plt.clf()

##########################################################################################################################################
label = []
label1 = ["H4-1", "PNG 135.9+55.9"]
n = 24
A1, B1 = [[] for _ in range(n)], [[] for _ in range(n)]
d_644_jplus, d_768_jplus = [], []
d_644_jplus1, d_768_jplus1 = [], []

for file_name in file_list:
    with open(file_name) as f:
        data = json.load(f)
        # if data['id'].endswith("1-HPNe"):
        #     label.append("")
        # elif data['id'].endswith("SLOAN-HPNe-"):
        #     label.append("H4-1")
        # elif data['id'].endswith("1359559-HPNe"):
        #     label.append("PNG 135.9+55.9")
        if data['id'].startswith("ngc"):
            label.append("NGC 2242")
        elif data['id'].startswith("mwc"):
            label.append("MWC 574")
        plot_mag("F660", "F480_gSDSS", "F625")
        
AB = np.vstack([A1[2],B1[2]])
z = gaussian_kde(AB)(AB)
df=pd.DataFrame({'x': np.array(B1[2]), 'y': np.array(A1[2]) })


# Sort the points by density, so that the densest points are plotted last
idx = z.argsort()
x, y, z = np.array(A1[2])[idx], np.array(B1[2])[idx], z[idx]

# Canditade find in the JPLUS data
colx4 = mag[8]-mag[7]
coly4 = mag[8]-mag[5]

lgd_kws = {'frameon': True, 'fancybox': True, 'shadow': True}
#sns.set(style="dark", context="talk")
#sns.set_style('ticks')
fig = plt.figure(figsize=(7, 6))
ax4 = fig.add_subplot(111, axisbg="#eeeeee")
ax4.set_xlim(xmin=-2.5,xmax=0.5)
ax4.set_ylim(ymin=-5.0,ymax=1.5)
#ax4.set_xlim(xmin=-2.5,xmax=2.0)
plt.tick_params(axis='x', labelsize=20) 
plt.tick_params(axis='y', labelsize=20)
plt.xlabel(r'$J0660 - rSDSS$', fontsize= 20)
plt.ylabel(r'$J0660 - gSDSS$', fontsize= 20)
#ax4.plot( 'x', 'y', data=df, alpha= 0.5, linestyle='', marker='o')
ax4.scatter(y, x, c=z, s=50, edgecolor='')
ax4.scatter(B1[0], A1[0], c='black', alpha=0.8, s=40, cmap=plt.cm.hot, label='Obs. halo PNe')
(_, caps, _) = ax4.errorbar(B1[0], A1[0], xerr=0.0, yerr=0.0, marker='.', fmt='k.', elinewidth=0.8, markeredgewidth=0.8, markersize=8,)
for cap in caps:
    cap.set_markeredgewidth(1)

ax4.scatter(B1[20], A1[20], c='black', alpha=0.8, s=40, cmap=plt.cm.hot)#, label='Obs. halo PNe')
ax4.errorbar(B1[20], A1[20], yerr=0.3,  uplims= True,  marker='.', fmt='k.', elinewidth=.8, markeredgewidth=.8, markersize=8,)
ax4.errorbar(B1[20], A1[20], xerr=0.2,  xuplims= True,  marker='.', fmt='k.', elinewidth=.8, markeredgewidth=.8, markersize=8,)

ax4.scatter(B1[21], A1[21], c='black', alpha=0.8, s=40, cmap=plt.cm.hot)
(_, caps, _) = ax4.errorbar(B1[21], A1[21], xerr=0.0, yerr=0.0, marker='.', fmt='k.', elinewidth=0.8, markeredgewidth=0.8, markersize=8,)
for cap in caps:
    cap.set_markeredgewidth(1)
ax4.scatter(B1[22], A1[22], c='black', alpha=0.8, s=40)
(_, caps, _) = ax4.errorbar(B1[22], A1[22], xerr=0.0, yerr=0.0, marker='.', fmt='k.', elinewidth=0.8, markeredgewidth=0.8, markersize=8,)
for cap in caps:
    cap.set_markeredgewidth(1)

ax4.scatter(B1[1], A1[1], c='purple', alpha=0.6, s=40, cmap=plt.cm.hot, label='SDSS CVs')
ax4.scatter(B1[4], A1[4],  c= "mediumaquamarine" , alpha=0.6, s=40, marker='D', cmap=plt.cm.hot, label='SDSS QSOs')
ax4.scatter(B1[5], A1[5],  c= "mediumaquamarine", alpha=0.6, s=40, marker='D', cmap=plt.cm.hot)#, label='SDSS QSOs (2.4<z<2.6)')
ax4.scatter(B1[6], A1[6],  c= "mediumaquamarine", alpha=0.6, s=40, marker='D', cmap=plt.cm.hot)#, label='SDSS QSOs (3.2<z<3.4)')
ax4.scatter(B1[7], A1[7],  c= "goldenrod", alpha=0.6, s=40, marker='^', cmap=plt.cm.hot, label='SDSS SFGs ')
ax4.scatter(B1[8], A1[8],  c= "red", alpha=0.6, s=40, marker='s', cmap=plt.cm.hot)#, label='Obs. SySts ')
ax4.scatter(B1[16], A1[16],  c= "red", alpha=0.6, s=40, marker='s', cmap=plt.cm.hot, label='Obs. SySts ')
#ax4.scatter(B1[72], A1[72],  c= "red", alpha=0.8, marker='D', label='Symbiotics in NGC 55')
ax4.scatter(B1[14], A1[14],  c= "red", alpha=0.6, s=40, marker='D', cmap=plt.cm.hot, label='Obs. SySts in NGC 205')
ax4.scatter(B1[15], A1[15],  c= "red", alpha=0.6, s=40, marker='D', cmap=plt.cm.hot)  #label=' SySts in NGC 205')
ax4.scatter(B1[9], A1[9],  c= "red", alpha=0.6, s=40, marker='^', cmap=plt.cm.hot)#,  label='IPHAS SySts')
ax4.scatter(B1[17], A1[17],  c= "red", alpha=0.6, s=40, marker='^', cmap=plt.cm.hot, label='IPHAS SySts')
ax4.scatter(B1[19], A1[19],  c= "red", alpha=0.6, s=40, marker='o', cmap=plt.cm.hot, label='Obs. SySts in IC10 ')
ax4.scatter(B1[18], A1[18],  c= "red", alpha=0.6, s=40, marker='v', cmap=plt.cm.hot, label='Obs. SySts in NGC 185')
#ax4.scatter(B1[73], A1[73],  c= "red", alpha=0.8, marker='o', label='C. Buil Symbiotics')
ax4.scatter(B1[10], A1[10],  c= "gray", alpha=0.6, s=40, marker='D', cmap=plt.cm.hot, label='Obs. HII region in NGC 55')
ax4.scatter(B1[23], A1[23],  c= "lightsalmon", alpha=0.6, s=42, marker='*', label='Obs. YSOs')
#ax2.scatter(B1[74], A1[74],  c= "black", alpha=0.8, marker='.', label='SN Remanents')
ax4.scatter(colx4, coly4,  c= "red", alpha=0.8, s=300, marker='*', label='HASH PN')

for label_, x, y in zip(label, B1[0], A1[0]):
    ax4.annotate(label_, (x, y), alpha=5, size=8,
                   xytext=(-4.0, 3.6), textcoords='offset points', ha='right', va='bottom',)
###################################################################
ax4.annotate("H4-1", (np.array(B1[20]), np.array(A1[20])), alpha=5, size=8,
                   xytext=(25.3, -10), textcoords='offset points', ha='right', va='bottom',)
ax4.annotate("PNG 135.9+55.9", (np.array(B1[21]), np.array(A1[21])), alpha=5, size=8,
                   xytext=(65.0, -10), textcoords='offset points', ha='right', va='bottom',)
ax4.annotate("DdDm-1", (np.array(B1[22]), np.array(A1[22])), alpha=10, size=8,
                   xytext=(-4.5, -8), textcoords='offset points', ha='right', va='bottom',)
##################################################################
#Obersevado porJPLUS
#for label_, x, y in zip(label1, d_768_jplus[0], d_644_jplus[0]):
# ax4.annotate("H4-1", (d_768_jplus[0], d_644_jplus[0]), alpha=8, size=8,
#                    xytext=(-5, 3), textcoords='offset points', ha='right', va='bottom', color='blue',)

# ax4.annotate("PNG 135.9+55.9", (d_768_jplus[1], d_644_jplus[1]), alpha=8, size=8,
#                    xytext=(68, -10), textcoords='offset points', ha='right', va='bottom', color='green',)

# ax4.annotate("CI Cyg", (d_768_jplus[2], d_644_jplus[2]), alpha=20, size=8,
#                    xytext=(-5, 3), textcoords='offset points', ha='right', va='bottom', color='yellow',)

# ax4.annotate("TX CVn", (d_768_jplus[3], d_644_jplus[3]), alpha=20, size=8,
#                    xytext=(18, -13), textcoords='offset points', ha='right', va='bottom', color='m',)

# Region where stay the PNe
result = findIntersection(1.559, 0.58, -0.5, 0.0, 0.0)
result_y = 1.559*result + 0.58

x_new = np.linspace(-15, -0.5, 200)
x_new2 = -0.5
x_new3 = np.linspace(-10.0, 1.1, 200)
y = 1.559*x_new + 0.58
yy = 0.0*x_new2 
#Mask
#mask = y >= result_y - 0.5
ax4.plot(x_new, y, color='k', linestyle='-')
plt.axvline(x=-0.5, ymin=0.74, ymax = 1.79, color='k', linestyle='-')
#plt.axvline(x=0.1, ymin=0.18, ymax = 1.79, linewidth=2, color='k')

#fit(ax4, B1[2], A1[2]) # linel afit: 1.559 x + 1.067

# t = np.linspace(-3.0, 0.5, 200)
# tt = 1.559*t + 0.58
# ax4.plot(t, tt, color='k', linestyle='-')
# ax4.axvline(x=-0.5, color='k', linestyle='-')

#for Z, x, y in zip(z, d_768_Qz, d_644_Qz):
    #ax4.annotate("{:.3f}".format(Z), (x, y), fontsize='x-small',
                       #xytext=(5,-5), textcoords='offset points', ha='left', bbox={"boxstyle": "round", "fc": "white", "ec": "none", "alpha": 0.5}, alpha=0.7)
#ax4.set_title(" ".join([cmd_args.source]))
#ax4.grid(True)
#ax4.annotate('Higher z(3.288)', xy=(0.08749580383300781, 0.181182861328125), xytext=(-0.5, -0.58),
             #arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))
#ax4.annotate('Lower z(3.065)', xy=(0.3957328796386719, 0.1367034912109375), xytext=(0.5, -0.58),
             #arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))
#ax4.minorticks_on()
#ax4.grid(which='minor')#, lw=0.3)
ax4.legend(scatterpoints=1, ncol=1, fontsize=8.0, loc='lower right', **lgd_kws)
#ax4.grid()
#lgd = ax4.legend(loc='center right', bbox_to_anchor=(1.27, 0.5), fontsize=7.5, **lgd_kws)
#ax4.grid(which='minor', lw=0.5)
#sns.despine(bottom=True)
#plt.tight_layout()
#plt.savefig('luis-JPLUS-Viironen.pdf')#,  bbox_extra_artists=(lgd,), bbox_inches='tight')
plt.tight_layout() # Para los espacios en los ejes
plt.savefig('Fig4-SPLUS18-f660-r-densitymap.pdf')
plt.clf()



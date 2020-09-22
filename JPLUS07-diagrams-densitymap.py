# -*- coding: utf-8 -*-
'''
Make color-color diagrams for JPLUS 2017
'''
from __future__ import print_function
import numpy as np
import glob
import json
import matplotlib.pyplot as plt
import seaborn as sns
import sys
from scipy.stats import gaussian_kde
import pandas as pd
from astropy.table import Table
#import StringIO
from sympy import S, symbols
from scipy.optimize import fsolve
import os
from astropy.io import fits
import scipy.stats as st
from mpl_toolkits.axes_grid1.inset_locator import inset_axes


#Find the point inteception between two lines     
def findIntersection(m, y, m1, y1, x0):
    x = np.linspace(-10.0, 15.5, 200)
    return fsolve(lambda x : (m*x + y) - (m1*x + y1), x0)

#reading the files .json

pattern = "*-spectros/*-JPLUS17-magnitude.json"
file_list = glob.glob(pattern)

#reddenign vector
def redde_vector(x0, y0, x1, y1, a, b, c, d):
    plt.arrow(x0+a, y0+b, (x1+a)-(x0+a), (y1+b)-(y0+b),  fc="k", ec="k", width=0.01,
              head_width=0.07, head_length=0.15) #head_width=0.05, head_length=0.1)
    plt.text(x0+a+c, y0+b+d, 'A$_\mathrm{V}=2$', va='center', fontsize='x-large')


def filter_mag(e, s, f1, f2, f3):
    '''
    Calculate the colors using any of set of filters
    '''
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
    x20, y20 = filter_mag("ngc185", "", f1, f2, f3)
    x21, y21 = filter_mag("SySt-ic10", "", f1, f2, f3)
    x22, y22 = filter_mag("H41-HPNe-", "", f1, f2, f3)
    x23, y23 = filter_mag("1359559-HPNe-", "", f1, f2, f3)
    x24, y24 = filter_mag("DdDm-1-HPNe-", "", f1, f2, f3)
    x25, y25 = filter_mag("YSOs", "", f1, f2, f3)
    x26, y26 = filter_mag("E00_100", "", f1, f2, f3)
    x27, y27 = filter_mag("E01_100", "", f1, f2, f3)
    x28, y28 = filter_mag("E02_100", "", f1, f2, f3)
    x29, y29 = filter_mag("Be", "", f1, f2, f3)
    x30, y30 = filter_mag("STAR", "", f1, f2, f3)
    # x28, y28 = filter_mag("E00_300", "", f1, f2, f3)
    # x29, y29 = filter_mag("E00_600", "", f1, f2, f3)

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
    for a, b in zip(x19, y19):
        A1[12].append(a)
        B1[12].append(b)
    for a, b in zip(x20, y20):
        A1[13].append(a)
        B1[13].append(b)
    for a, b in zip(x21, y21):
        A1[14].append(a)
        B1[14].append(b)
    for a, b in zip(x22, y22):
        A1[15].append(a)
        B1[15].append(b)
    for a, b in zip(x23, y23):
        A1[16].append(a)
        B1[16].append(b)
    for a, b in zip(x24, y24):
        A1[17].append(a)
        B1[17].append(b)
    for a, b in zip(x25, y25):
        A1[18].append(a)
        B1[18].append(b)
    for a, b in zip(x26, y26):
        A1[2].append(a)
        B1[2].append(b)
    for a, b in zip(x27, y27):
        A1[2].append(a)
        B1[2].append(b)
    for a, b in zip(x28, y28):
        A1[2].append(a)
        B1[2].append(b)
    for a, b in zip(x29, y29):
        A1[19].append(a)
        B1[19].append(b)
    for a, b in zip(x30, y30):
        A1[20].append(a)
        B1[20].append(b)
        
label = []
label1 = ["H4-1", "PNG 135.9+55.9"]
n = 21
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
        plot_mag("F625_r_sdss", "F660", "F766_i_sdss")
        
AB = np.vstack([A1[2],B1[2]])
z = gaussian_kde(AB)(AB)
df=pd.DataFrame({'x': np.array(B1[2]), 'y': np.array(A1[2]) })

# Sort the points by density, so that the densest points are plotted last
idx = z.argsort()
x, y, z = np.array(A1[2])[idx], np.array(B1[2])[idx], z[idx]

# Canditade find in the JPLUS data

mag=[100.0, 100.0, 22.0102539, 21.7526703, 22.1947689,  21.7716465, 21.549675, 20.6785908,  19.4841557, 21.4224014, 20.7914772, 21.0010147]

colx = mag[7]-mag[9]
coly = mag[7]-mag[8]

#Candidate for symbiotic star in JPLUS data=>
tab = Table.read("EDR-JPLUS/SySts-allcolour_4.tab", format="ascii.tab")

x1 = tab['rSDSS'] - tab['iSDSS']
y1  = tab['rSDSS'] - tab['J0660']

x2 = tab['J0515'] - tab['J0861']
y2 = tab['J0515'] - tab['J0660']

x3 = tab['zSDSS'] - tab['gSDSS']
y3 = tab['zSDSS'] - tab['J0660']

#Data science verification===>
#error computing by Valera
x_color_vii_h4 = []
y_color_vii_h4 = []

x_color_vii_pg = []
y_color_vii_pg = []

# The J0515 color
x_color_j0515_h4 = []
y_color_j0515_h4 = []

x_color_j0515_pg = []
y_color_j0515_pg = []

# The other color
x_color_z_h4 = []
y_color_z_h4 = []

x_color_z_pg = []
y_color_z_pg = []

err_zpVale_h4 = {"e_u": 0.128, "e_j0378": 0.020, "e_j0395": 0.061, "e_j0410": 0.029, "e_j0430": 0.067, "e_g": 0.036, "e_j0515": 0.044, "e_r": 0.042, "e_j0660": 0.043, "e_i": 0.048, "e_j0861": 0.030, "e_z": 0.092}
err_zpVale_pn135 = {"e_u": 0.102, "e_j0378": 0.0, "e_j0395": 0.115, "e_j0410": 0.103, "e_j0430": 0.127, "e_g": 0.073, "e_j0515": 0.073, "e_r": 0.073, "e_j0660": 0.078, "e_i": 0.071, "e_j0861": 0.070, "e_z": 0.100}

#Include the magnitudes from JPLUS images
#HHH4 - 1
pattern1 = "JPLUS-data/H4-1-phot/*6pix.json"
file_list1 = glob.glob(pattern1)
for file_name1 in file_list1:
    with open(file_name1) as f1:
        data1 = json.load(f1)
        j0410 = data1["J0410"]-25+20.971
        g = data1["J0480_gSDSS"]-25+23.297#-1.12
        j0515 = data1["J0515"]-25+21.193
        j0660 = data1["J0660"]-25+20.859
        r = data1["J0625_rSDSS"]-25+23.335
        i = data1["J0766_iSDSS"]-25+23.122
        j0861 = data1["J0861"]-25+21.410
        z_ = data1["J0911_zSDSS"]-25+22.562
        #colors
        ha_r = r - j0660
        r_i = r - i
        x_color_vii_h4.append(r_i)
        y_color_vii_h4.append(ha_r)
        #color
        g_i = g - i
        j410_515 = j0410 - j0660
        # x_color_j0410_h4.append(g_i)
        # y_color_j0410_h4.append(j410_515)
        #color
        z_g = z_ - g
        z_j0660 = z_ - j0660
        x_color_z_h4.append(z_g)
        y_color_z_h4.append(z_j0660)
        #color
        j0515_j0861 = j0515 - j0861
        j0515_j0660 = j0515 - j0660
        x_color_j0515_h4.append(j0515_j0861)
        y_color_j0515_h4.append(j0515_j0660)
        
       
pattern2 = "JPLUS-data/PNG135coadded-phot/*6pix.json"
file_list2 = glob.glob(pattern2)
for file_name2 in file_list2:
    with open(file_name2) as f2:
        data2 = json.load(f2)
        j0410 = data2["J0410"]-25+21.102
        g =  data2["J0480_gSDSS"]-25+23.425#-1.12
        j0515 = data2["J0515"]-25+21.444
        j0660 = data2["J0660"]-25+21.058
        r = data2["J0625_rSDSS"]-25+23.565
        i = data2["J0766_iSDSS"]-25+23.255
        z_ = data2["J0911_zSDSS"]-25+22.535
        j0861 = data2["J0861"]-25+21.534
        ha_r = r - j0660
        r_i = r - i
        x_color_vii_pg.append(r_i)
        y_color_vii_pg.append(ha_r)
        g_i = g - i
        j410_515 = j0410 - j0660
        # x_color_z_pg.append(g_i)
        # y_color_z_pg.append(j410_515)
        #color
        z_g = z_ - g
        z_j0660 = z_ - j0660
        x_color_z_pg.append(z_g)
        y_color_z_pg.append(z_j0660)
        #color
        j0515_j0861 = j0515 - j0861
        j0515_j0660 = j0515 - j0660
        x_color_j0515_pg.append(j0515_j0861)
        y_color_j0515_pg.append(j0515_j0660)

#Progation error with Valera's erros
err_Val_h4x= np.sqrt(err_zpVale_h4["e_r"]**2+err_zpVale_h4['e_i']**2)
err_Val_h4y= np.sqrt(err_zpVale_h4["e_r"]**2+err_zpVale_h4["e_j0660"]**2)
err_Val_pn135x= np.sqrt(err_zpVale_pn135["e_r"]**2+err_zpVale_pn135['e_i']**2)
err_Val_pn135y= np.sqrt(err_zpVale_pn135["e_r"]**2+err_zpVale_pn135["e_j0660"]**2)

err_Val_h4x_z= np.sqrt(err_zpVale_h4["e_z"]**2+err_zpVale_h4['e_g']**2)
err_Val_h4y_z= np.sqrt(err_zpVale_h4["e_z"]**2+err_zpVale_h4["e_j0660"]**2)
err_Val_pn135x_z= np.sqrt(err_zpVale_pn135["e_z"]**2+err_zpVale_pn135['e_g']**2)
err_Val_pn135y_z= np.sqrt(err_zpVale_pn135["e_z"]**2+err_zpVale_pn135["e_j0660"]**2)

err_Val_h4x_j0515= np.sqrt(err_zpVale_h4["e_j0515"]**2+err_zpVale_h4['e_j0861']**2)
err_Val_h4y_j0515= np.sqrt(err_zpVale_h4["e_j0515"]**2+err_zpVale_h4["e_j0660"]**2)
err_Val_pn135x_j0515= np.sqrt(err_zpVale_pn135["e_j0515"]**2+err_zpVale_pn135['e_j0861']**2)
err_Val_pn135y_j0515= np.sqrt(err_zpVale_pn135["e_j0515"]**2+err_zpVale_pn135["e_j0660"]**2)

##############################################################################
##############################################################################
#WD from S-PLUS ##############################################################
##############################################################################
##############################################################################
datadir = "WD_ariel/"
fitsfile = "WD_splus_obs.fits"
hdulist= fits.open(os.path.join(datadir, fitsfile))

def WS_splus(filter_1, filter_2, filter_3):
    band1 = hdulist[1].data[filter_1]
    band2 = hdulist[1].data[filter_2]
    band3 = hdulist[1].data[filter_3]
    return (band1 - band2), (band1 - band3)

##############################################################################
#plots
lgd_kws = {'frameon': True, 'fancybox': True, 'shadow': True}
#sns.set(style="dark", context="talk")
#sns.set_style('ticks')
fig = plt.figure(figsize=(7, 6))
ax1 = fig.add_subplot(111, facecolor="#eeeeee")
ax1.set_xlim(xmin=-3.7,xmax=3.7)
ax1.set_ylim(ymin=-2.8,ymax=2.8)
#ax1.set_xlim(xmin=-2.5,xmax=2.0)
plt.tick_params(axis='x', labelsize=22) 
plt.tick_params(axis='y', labelsize=22)
plt.xlabel(r'$r - i$', fontsize= 22)
plt.ylabel(r'$r - J0660$', fontsize= 22)
#plt.plot( 'x', 'y', data=df, linestyle='', marker='o')
ax1.scatter(y, x, c=z, s=50, alpha=0.5, edgecolor='')
ax1.scatter(x_color_vii_h4, y_color_vii_h4, c=sns.xkcd_rgb['yellow'], alpha=0.9, marker='*', s=490, edgecolor='black', zorder=150.0, label='J-PLUS H4-1')
ax1.errorbar(x_color_vii_h4, y_color_vii_h4, xerr=err_Val_h4x, yerr=err_Val_h4y, marker='.', fmt='k.', elinewidth=1.9, markeredgewidth=1.8, capsize=9)#, elinewidth=1.4, markeredgewidth=1.4, markersize=14,)
ax1.scatter(x_color_vii_pg, y_color_vii_pg,  c=sns.xkcd_rgb['green'], alpha=0.9, marker='*', s=490, zorder=150.0, edgecolor='black', label='J-PLUS PNG135.9+55.9')
ax1.errorbar(x_color_vii_pg, y_color_vii_pg, xerr=err_Val_pn135x, yerr=err_Val_pn135y, marker='.', fmt='k.', elinewidth=1.9, markeredgewidth=1.8, capsize=9)
ax1.scatter(B1[0], A1[0], color= sns.xkcd_rgb["aqua"], s=90, cmap=plt.cm.hot, edgecolor='black', zorder=121.0, label='Obs. hPNe')
#ax1.scatter(B1[19], A1[19], c='y', alpha=0.8, s=40, label='Modeled halo PNe')
(_, caps, _) = ax1.errorbar(B1[0], A1[0], xerr=0.0, yerr=0.0, marker='.', fmt='.', color= sns.xkcd_rgb["aqua"], elinewidth=0.8, markeredgewidth=0.8, markersize=8,)
for cap in caps:
    cap.set_markeredgewidth(1)

ax1.scatter(B1[15], A1[15], color= sns.xkcd_rgb["aqua"], s=90, edgecolor='black',  zorder=200.0, cmap=plt.cm.hot)#, label='Obs. halo PNe')
# ax1.errorbar(B1[15], A1[15], yerr=0.2,  lolims= True,  marker='.', fmt='k.', elinewidth=.8, markeredgewidth=.8, markersize=8,)
# ax1.errorbar(B1[15], A1[15], xerr=0.2,  xuplims= True,  marker='.', fmt='k.', elinewidth=.8, markeredgewidth=.8, markersize=8,)

ax1.scatter(B1[16], A1[16], color= sns.xkcd_rgb["aqua"], s=90, edgecolor='black',  zorder=121.0, cmap=plt.cm.hot)
(_, caps, _) = ax1.errorbar(B1[16], A1[16], xerr=0.0, yerr=0.0, marker='.', fmt='.', color= sns.xkcd_rgb["aqua"], elinewidth=0.8, markeredgewidth=0.8, markersize=8,)
for cap in caps:
    cap.set_markeredgewidth(1)
ax1.scatter(B1[17], A1[17], color= sns.xkcd_rgb["aqua"], s=90, edgecolor='black', zorder=121.0, cmap=plt.cm.hot)
(_, caps, _) = ax1.errorbar(B1[17], A1[17], xerr=0.0, yerr=0.0, marker='.', fmt='.', color= sns.xkcd_rgb["aqua"], elinewidth=0.8, markeredgewidth=0.8, markersize=8,)
for cap in caps:
    cap.set_markeredgewidth(1)
ax1.scatter(B1[1], A1[1], c=sns.xkcd_rgb['pale yellow'], alpha=0.8, s=40, cmap=plt.cm.hot, edgecolor='black',  zorder=10.0, label='SDSS CVs')
ax1.scatter(B1[4], A1[4],  c= "mediumaquamarine" , alpha=0.6, s=40, marker='D', cmap=plt.cm.hot, edgecolor='black', label='SDSS QSOs')
ax1.scatter(B1[5], A1[5],  c= "mediumaquamarine", alpha=0.6, s=40, marker='D', cmap=plt.cm.hot, edgecolor='black')#,  label='SDSS QSOs (2.4<z<2.6)')
ax1.scatter(B1[6], A1[6],  c= "mediumaquamarine", alpha=0.6, s=40, marker='D', cmap=plt.cm.hot, edgecolor='black')#,  label='SDSS QSOs (3.2<z<3.4)')
ax1.scatter(B1[7], A1[7],  c= "goldenrod", alpha=0.8, s=60, marker='^', cmap=plt.cm.hot, edgecolor='black', label='SDSS SFGs ')
ax1.scatter(B1[8], A1[8],  c= "red", alpha=0.6, s=40, marker='s', cmap=plt.cm.hot, edgecolor='black', zorder=120.0, label='Obs. SySt')
#ax1.scatter(B1[72], A1[72],  c= "red", alpha=0.8, marker='D', label='Symbiotics in NGC 55')
ax1.scatter(B1[12], A1[12],  c= "red", alpha=0.6, s=40, marker='s', cmap=plt.cm.hot, edgecolor='black', zorder=120.0)#, label='Obs. SySts in NGC 205')
ax1.scatter(B1[9], A1[9],  c= "red", alpha=0.6, s=60, marker='^', cmap=plt.cm.hot, edgecolor='black', zorder=120.0, label='IPHAS SySt')
ax1.scatter(B1[14], A1[14],  c='red', alpha=0.6, s=40, marker='s', cmap=plt.cm.hot, edgecolor='black', zorder=120.0)#, label='Obs. SySts in IC10 ')
ax1.scatter(B1[13], A1[13],  c= "red", alpha=0.6, s=40, marker='s', cmap=plt.cm.hot, edgecolor='black', zorder=120.0)#, label='Obs. SySts in NGC 185')
#ax1.scatter(B1[73], A1[73],  c= "red", alpha=0.8, marker='o', label='C. Buil Symbiotics')
ax1.scatter(B1[10], A1[10],  c= "gray", alpha=0.6, s=40, marker='D', cmap=plt.cm.hot, edgecolor='black', label='Obs. H II regions in NGC 55')
#ax1.scatter(B1[74], A1[74],  c= "black", alpha=0.8, marker='.', label='SN Remanents')
ax1.scatter(B1[18], A1[18],  c= "lightsalmon", alpha=0.8, s=100, cmap=plt.cm.hot, marker='*',  edgecolor='black', label='Obs. YSOs')
ax1.scatter(B1[19], A1[19],  c=sns.xkcd_rgb['ultramarine blue'], alpha=0.8, s=90, cmap=plt.cm.hot, marker='*',  edgecolor='black', zorder=110, label='Obs. B[e] stars')

redde_vector(-1.2314754077697903, 2.147731023789999, -0.8273818571912539, 2.1826566358487645, 4., 0, -0.6, -0.15) #E=0.7

left, bottom, width, height = [0.20, 0.6, 0.2, 0.2]
ax11 = fig.add_axes([left, bottom, width, height])
axins2 = inset_axes(ax11, width="30%", height="50%")
axins2.set_xlim(xmin=-3.7,xmax=3.7)
axins2.set_ylim(ymin=-2.8,ymax=2.8)
axins2.scatter(B1[20], A1[20],  c=sns.xkcd_rgb['neon purple'], alpha=0.5, s=30, cmap=plt.cm.hot, marker='*', zorder=110, label='Normal stars')

r_660, r_i = WS_splus("r_aper", "F660_aper", "i_aper")
axins2.scatter(r_i, r_660, c=sns.xkcd_rgb['mint green'], alpha=0.8, s=30, cmap=plt.cm.hot, marker='*',  zorder=105, label='WDs from S-PLUS')


#################################################################

for label_, x, y in zip(label, B1[0], A1[0]):
    ax1.annotate(label_, (x, y), alpha=5, size=8,
                   xytext=(-5.0, -10.0), textcoords='offset points', ha='right', va='bottom',)
###################################################################
bbox_props = dict(boxstyle="round", fc="w", ec="0.78", alpha=0.5, pad=0.1)
ax1.annotate("H4-1", (np.array(B1[15]), np.array(A1[15])), alpha=15, size=10.0,
                   xytext=(-7, -10), textcoords='offset points', ha='right', va='bottom', bbox=bbox_props, zorder=100)
ax1.annotate("PNG 135.9+55.9", (np.array(B1[16]), np.array(A1[16])), alpha=15, size=10,
                   xytext=(90, -10), textcoords='offset points', ha='right', va='bottom', bbox=bbox_props, zorder=150)
# ax1.annotate("DdDm-1", (np.array(B1[17]), np.array(A1[17])), alpha=10, size=8,
#                    xytext=(-5, -10), textcoords='offset points', ha='right', va='bottom',)
##################################################################
#Obersevado porJPLUS
#for label_, x, y in zip(label1, d_768_jplus[0], d_644_jplus[0]):
# ax1.annotate("H4-1", (d_768_jplus[0], d_644_jplus[0]), alpha=8, size=8,
#                    xytext=(-5, 3), textcoords='offset points', ha='right', va='bottom', color='blue',)

# ax1.annotate("PNG 135.9+55.9", (d_768_jplus[1], d_644_jplus[1]), alpha=8, size=8,
#                    xytext=(68, -10), textcoords='offset points', ha='right', va='bottom', color='green',)

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
ax1.plot(x_new, y, color='k', zorder=100, linestyle='-')
ax1.plot(x_new2, yy , color='k', zorder=100, linestyle='-')

ax11.plot(x_new, y, color='k', zorder=100, linestyle='-')
ax11.plot(x_new2, yy , color='k', zorder=100, linestyle='-')

#Viironen
# x_new4 = np.linspace(-10.0, 11.1, 200)
# y_v =  0.25*x_new4 + 1.9
# ax1.plot(x_new4, y_v, color='k', linestyle='--')

# Region of the simbiotic stars
result1 = findIntersection(-400.0, +30.4, 0.39, 0.73, 0.0)
x_new_s = np.linspace(-15.5, result1, 200)
x_new2_s = np.linspace(result1, 15.5, 200)
y_s = -400.0*x_new_s + 30.4
yy_s = 0.39*x_new2_s + 0.73
# ax1.plot(x_new_s, y_s, color='r', zorder=100, linestyle='--')
# ax1.plot(x_new2_s, yy_s , color='r', zorder=100, linestyle='--')

plt.text(0.01, 0.94, 'CLOUDY modelled hPNe',
         transform=ax1.transAxes, fontsize="large")

#reddening vector

# arrow_properties = dict(
#     facecolor="black", width=0.4,
#     headwidth=4, shrink=0.1)
# plt.annotate(
#     "", xy=(-0.985+4.0, 2.209),
#     xytext=(-1.098+4.0, 2.197),
#     arrowprops=arrow_properties)

#redde_vector(-1.23147540777, 2.14773102379,  -1.11691297483, 2.16099869712, 4., 0, -0.9, 0.0) #E=0.2
#redde_vector(-1.2314754077697903, 2.147731023789999, -0.8273818571912539, 2.1826566358487645, 4., 0, -0.6, -0.15) #E=0.7
#plt.plot([-1.23147540777+3., -1.11691297483+3.], [2.14773102379, 2.16099869712], 'k-')
#plt.plot(-1.11691297483+3.7, 2.16099869712, '>k', ms=3.7)
#plt.text(-1.11691297483+3.8, 2.16099869712, 'A$_v=0.6$', va='center', fontsize='small')

#ax1.set_title(" ".join([cmd_args.source]))
#ax1.grid(True)
#ax1.annotate('Higher z(3.288)', xy=(0.08749580383300781, 0.181182861328125), xytext=(-0.5, -0.58),
             #arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))
#ax1.annotate('Lower z(3.065)', xy=(0.3957328796386719, 0.1367034912109375), xytext=(0.5, -0.58),
             #arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))
ax1.minorticks_on()
#ax1.grid(which='minor')#, lw=0.3)
ax1.legend(scatterpoints=1, ncol=2, fontsize=11.0, loc='lower right', **lgd_kws)
#ax1.grid()
#lgd = ax1.legend(loc='center right', bbox_to_anchor=(1.27, 0.5), fontsize=7.5, **lgd_kws)
#ax1.grid(which='minor', lw=0.5)
#sns.despine(bottom=True)
plt.tight_layout()
#plt.savefig('luis-JPLUS-Viironen.pdf')#,  bbox_extra_artists=(lgd,), bbox_inches='tight')
pltfile = 'Fig1-JPLUS17-Viironen.pdf'
save_path = '../Dropbox/JPAS/paper-phot/'
file_save = os.path.join(save_path, pltfile)
plt.savefig(file_save)
#plt.savefig('Fig1-JPLUS17-Viironen.pdf')
plt.clf()

##########################################################################################################################################
label = []
label1 = ["H4-1", "PNG 135.9+55.9"]
n = 21
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
ax2 = fig.add_subplot(111, facecolor="#eeeeee")
ax2.set_xlim(xmin=-3.0,xmax=6.4)
ax2.set_ylim(ymin=-5.2,ymax=5.7)
#ax2.set_xlim(xmin=-2.5,xmax=2.0)
plt.tick_params(axis='x', labelsize=22) 
plt.tick_params(axis='y', labelsize=22)
plt.xlabel(r'$J0515 - J0861$', fontsize=22)
plt.ylabel(r'$J0515 - J0660$', fontsize=22)
#plt.plot( 'x', 'y', data=df, linestyle='', marker='o')
ax2.scatter(y, x, c=z, s=50, alpha=0.5, edgecolor='')
ax2.scatter(x_color_j0515_h4, y_color_j0515_h4,  c=sns.xkcd_rgb['yellow'], alpha=0.9, marker='*', s=490, edgecolor='black', zorder=100.0, label='J-PLUS H4-1')
ax2.errorbar(x_color_j0515_h4, y_color_j0515_h4, xerr=err_Val_h4x_j0515, yerr=err_Val_h4y_j0515, marker='.', fmt='k.', elinewidth=1.9, markeredgewidth=1.8, capsize=9)#, elinewidth=1.4, markeredgewidth=1.4, markersize=14,)
ax2.scatter(x_color_j0515_pg, y_color_j0515_pg, c=sns.xkcd_rgb['green'], alpha=0.9, marker='*', s=490, edgecolor='black', zorder=100.0, label='J-PLUS PNG135.9+55.9')
ax2.errorbar(x_color_j0515_pg, y_color_j0515_pg, xerr=err_Val_pn135x_j0515, yerr=err_Val_pn135y_j0515, marker='.', fmt='k.', elinewidth=1.9, markeredgewidth=1.8, capsize=9)
ax2.scatter(B1[0], A1[0], color= sns.xkcd_rgb["aqua"], s=90, edgecolor='black', cmap=plt.cm.hot, zorder=101, label='Obs. hPNe')
(_, caps, _) = ax2.errorbar(B1[0], A1[0], xerr=0.0, yerr=0.0, marker='.', fmt='.',  color= sns.xkcd_rgb["aqua"], elinewidth=0.8, markeredgewidth=0.8, markersize=8,)
for cap in caps:
    cap.set_markeredgewidth(1)
#ax2.scatter(B1[19], A1[19], c='y', alpha=0.8, s=40, label='Modeled halo PNe')
ax2.scatter(B1[15], A1[15],  color= sns.xkcd_rgb["aqua"], edgecolor='black', cmap=plt.cm.hot, s=90, zorder=101)#, label='Obs. halo PNe')
#ax2.errorbar(B1[15], A1[15], yerr=0.3,  lolims= True,  marker='.', fmt='k.', elinewidth=.8, markeredgewidth=.8, markersize=8,)
#ax2.errorbar(B1[15], A1[15], xerr=0.2,  xuplims= True,  marker='.', fmt='k.', elinewidth=.8, markeredgewidth=.8, markersize=8,)

ax2.scatter(B1[16], A1[16],  color= sns.xkcd_rgb["aqua"], edgecolor='black', cmap=plt.cm.hot, s=90,  zorder=101.0)
(_, caps, _) = ax2.errorbar(B1[16], A1[16], xerr=0.0, yerr=0.0, marker='.', fmt='.',  color= sns.xkcd_rgb["aqua"], elinewidth=0.8, markeredgewidth=0.8, markersize=8,)
for cap in caps:
    cap.set_markeredgewidth(1)
ax2.scatter(B1[17], A1[17],  color= sns.xkcd_rgb["aqua"], s=90, edgecolor='black', zorder=101.0, cmap=plt.cm.hot)
(_, caps, _) = ax2.errorbar(B1[17], A1[17], xerr=0.0, yerr=0.0, marker='.', fmt='.',  color= sns.xkcd_rgb["aqua"], elinewidth=0.8, markeredgewidth=0.8, markersize=8,)
for cap in caps:
    cap.set_markeredgewidth(1)

ax2.scatter(B1[1], A1[1], c=sns.xkcd_rgb['pale yellow'], alpha=0.8, s=40, cmap=plt.cm.hot, edgecolor='black', zorder=10.0, label='SDSS CVs')
ax2.scatter(B1[4], A1[4],  c= "mediumaquamarine" , alpha=0.6, s=40, marker='D', cmap=plt.cm.hot, edgecolor='black', label='SDSS QSOs')#,  label='SDSS QSOs (1.3<z<1.4)')
ax2.scatter(B1[5], A1[5],  c= "mediumaquamarine", alpha=0.6, s=40, marker='D', cmap=plt.cm.hot, edgecolor='black',)#,  label='SDSS QSOs (2.4<z<2.6)')
ax2.scatter(B1[6], A1[6],  c= "mediumaquamarine", alpha=0.6, s=40, marker='D',  cmap=plt.cm.hot, edgecolor='black',)#,  label='SDSS QSOs (3.2<z<3.4)')
ax2.scatter(B1[7], A1[7],  c= "goldenrod", alpha=0.8, s=60, marker='^', cmap=plt.cm.hot, edgecolor='black', label='SDSS SFGs ')
ax2.scatter(B1[8], A1[8],  c= "red", alpha=0.6, s=40, marker='s', cmap=plt.cm.hot, edgecolor='black', zorder=120.0, label='Obs. SySt')
#ax2.scatter(B1[72], A1[72],  c= "red", alpha=0.8, marker='D', label='Symbiotics in NGC 55')
ax2.scatter(B1[12], A1[12],  c= "red", alpha=0.6, s=60, marker='s', cmap=plt.cm.hot, edgecolor='black', zorder=120.0)#, label='Obs. SySts in NGC 205')
ax2.scatter(B1[9], A1[9],  c= "red", alpha=0.6, s=60, marker='^', cmap=plt.cm.hot, edgecolor='black', zorder=120.0, label='IPHAS SySt')
ax2.scatter(B1[14], A1[14], c= "red" , alpha=0.6, s=40, marker='s', cmap=plt.cm.hot, edgecolor='black', zorder=120.0)#, label='Obs. SySts in IC10 ')
ax2.scatter(B1[13], A1[13],  c= "red", alpha=0.6, s=40, marker='s', cmap=plt.cm.hot, edgecolor='black', zorder=120.0)#, label='Obs. SySts in NGC 185')
#ax2.scatter(B1[73], A1[73],  c= "red", alpha=0.8, marker='o', label='C. Buil Symbiotics')
ax2.scatter(B1[10], A1[10],  c= "gray", alpha=0.6, s=40, marker='D', cmap=plt.cm.hot, edgecolor='black', label='Obs. H II regions in NGC 55')
ax2.scatter(B1[18], A1[18],  c= "lightsalmon", alpha=0.8, s=100, marker='*', cmap=plt.cm.hot, edgecolor='black', label='Obs. YSOs')
ax2.scatter(B1[19], A1[19],  c=sns.xkcd_rgb['ultramarine blue'], alpha=0.8, s=90, cmap=plt.cm.hot, marker='*',  edgecolor='black', zorder=110, label='Obs. B[e] stars')
ax2.scatter(B1[20], A1[20],  c=sns.xkcd_rgb['neon purple'], alpha=0.8, s=90, cmap=plt.cm.hot, marker='*', edgecolor='black', zorder=110, label='Normal stars')

f515, f515_f861 = WS_splus("F515_aper", "F660_aper", "F861_aper")
ax2.scatter(f515_f861, f515, c=sns.xkcd_rgb['mint green'], alpha=0.3, s=90, cmap=plt.cm.hot, marker='*', edgecolor='black', zorder=105, label='WDs from S-PLUS')

for label_, x, y in zip(label, B1[0], A1[0]):
    ax2.annotate(label_, (x, y), alpha=5, size=8,
                   xytext=(40.0, -10.0), textcoords='offset points', ha='right', va='bottom',)
###################################################################
ax2.annotate("H4-1", (np.array(B1[15]),np.array(A1[15])), alpha=15, size=10,
                   xytext=(25.3, 5), textcoords='offset points', ha='right', va='bottom', bbox=bbox_props,)
ax2.annotate("PNG 135.9+55.9", (np.array(B1[16]), np.array(A1[16])), alpha=15, size=10,
                   xytext=(-5, -10), textcoords='offset points', ha='right', va='bottom', bbox=bbox_props,)
# ax2.annotate("DdDm-1", (np.array(B1[17]), np.array(A1[17])), alpha=10, size=8,
#                    xytext=(-8.5, -8), textcoords='offset points', ha='right', va='bottom',)
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

#Region where are located the PNe
result = findIntersection(2.7, 2.15, 0.0, 0.22058956, 0.0)
result_y = 2.5*result + 2.15

x_new = np.linspace(result, 15.5, 200)
x_new2 = np.linspace(-10.0, result, 200)
x_new3 = np.linspace(-10.0, 10.0, 200)
y = 2.7*x_new + 2.15
yy = 0.0*x_new2 + 0.22058956
#Mask
#mask = y >= result_y - 0.5
ax2.plot(x_new, y, color='k', zorder=100, linestyle='-')
ax2.plot(x_new2, yy , color='k', zorder=100, linestyle='-')

# Region of the simbiotic stars
result1 = findIntersection(5.5, -6.45, 0.98, -0.16, 0.0)
x_new_s = np.linspace(result1, 15.5, 200)
x_new2_s = np.linspace(result1, 15.5, 200)
y_s = 5.5*x_new_s - 6.45
yy_s = 0.98*x_new2_s - 0.16

#redeening vector
#redde_vector(-0.0516484176252, 3.58102946347, 0.322381326655, 3.78236984259, 4.9, -3.6, -0.9, -0.3) #E=0.2
redde_vector(0.05164841762521068, 3.5810294634717708, 1.2541288439073, 4.272881767686182, 4.2, -3.6, -0.2, -0.3) #E=0.7


#plt.arrow(-0.0516484176252+3.7, 3.58102946347-3.6, (0.322381326655+3.7-(-0.0516484176252+3.7)), (3.78236984259-3.6-(3.58102946347-3.6)), fc="k", ec="k",
#head_width=0.05, head_length=0.1 )

#plt.plot([-0.0516484176252+1., 0.322381326655+1.], [3.58102946347, 3.78236984259], '-k')

# ax2.plot(x_new_s, y_s, color='r', zorder=100, linestyle='--')
# ax2.plot(x_new2_s, yy_s , color='r', zorder=100, linestyle='--')

#for label_, x, y in zip(can_alh, d_768_cAlh, d_644_cAlh):
    #ax2.annotate(label_, (x, y), alpha=0.9, size=8,
                   #xytext=(3,-10), textcoords='offset points', ha='left', va='bottom',)
# plt.annotate(
#     '', xy=(B1[2][0],  A1[2][0]+0.35), xycoords='data',                    #
#     xytext=(B1[42][0]+0.4, A1[42][0]+0.4), textcoords='data', fontsize = 7,# vector extinction
#     arrowprops=dict(edgecolor='black',arrowstyle= '<-'))                   #
# plt.annotate(
#     '', xy=(B1[2][0]+0.35,  A1[2][0]+0.35), xycoords='data',
#     xytext=(5, 0), textcoords='offset points', fontsize='x-small')


#for Z, x, y in zip(z, d_768_Qz, d_644_Qz):
    #ax2.annotate("{:.3f}".format(Z), (x, y), fontsize='x-small',
                       #xytext=(5,-5), textcoords='offset points', ha='left', bbox={"boxstyle": "round", "fc": "white", "ec": "none", "alpha": 0.5}, alpha=0.7)
#ax2.set_title(" ".join([cmd_args.source]))
#ax2.grid(True)
#ax2.annotate('Higher z(3.288)', xy=(0.08749580383300781, 0.181182861328125), xytext=(-0.5, -0.58),
             #arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))
#ax2.annotate('Lower z(3.065)', xy=(0.3957328796386719, 0.1367034912109375), xytext=(0.5, -0.58),
             #arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))
ax2.minorticks_on()
#ax2.grid(which='minor')#, lw=0.3)
ax2.legend(scatterpoints=1, ncol=2, fontsize=11.0, loc='lower right', **lgd_kws)
#ax2.grid()
#lgd = ax2.legend(loc='center right', bbox_to_anchor=(1.27, 0.5), fontsize=7.5, **lgd_kws)
#ax2.grid(which='minor', lw=0.5)
#sns.despine(bottom=True)
plt.tight_layout()
plt.text(0.03, 0.96, 'CLOUDY modelled hPNe',
         transform=ax2.transAxes, fontsize="large")
#plt.savefig('luis-JPLUS-Viironen.pdf')#,  bbox_extra_artists=(lgd,), bbox_inches='tight')
pltfile = 'Fig2-SPLUS-J0515-J0660.jpg'
file_save = os.path.join(save_path, pltfile)
plt.savefig(file_save)
#plt.savefig('Fig2-JPLUS17-J0515-J0660.pdf')
plt.clf()


##########################################################################################################################################
label = []
label1 = ["H4-1", "PNG 135.9+55.9"]
n = 21
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
        plot_mag("F911_z_sdss", "F660", "F480_g_sdss")
        
AB = np.vstack([A1[2],B1[2]])
z = gaussian_kde(AB)(AB)
df=pd.DataFrame({'x': np.array(B1[2]), 'y': np.array(A1[2]) })
print(len(A1[2]))

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
ax3 = fig.add_subplot(111, facecolor="#eeeeee")
ax3.set_xlim(xmin=-5.9,xmax=3.9)
ax3.set_ylim(ymin=-7.2,ymax=5.0)
#ax3.set_xlim(xmin=-2.5,xmax=2.0)
plt.tick_params(axis='x', labelsize=22) 
plt.tick_params(axis='y', labelsize=22)
plt.xlabel(r'$z - g$', fontsize=22)
plt.ylabel(r'$z - J0660$', fontsize=22)
#plt.plot( 'x', 'y', data=df, linestyle='', marker='o')
ax3.scatter(y, x, c=z, s=50, alpha=0.5, edgecolor='')
ax3.scatter(x_color_z_h4, y_color_z_h4,  c=sns.xkcd_rgb['yellow'], alpha=0.9, marker='*', s=490, zorder=100.0, edgecolor='black', label='J-PLUS H4-1')
ax3.errorbar(x_color_z_h4, y_color_z_h4, xerr=err_Val_h4x_z, yerr=err_Val_h4y_z, marker='.', fmt='k.', elinewidth=1.9, markeredgewidth=1.8, capsize=9)#, elinewidth=1.4, markeredgewidth=1.4, markersize=14,)
ax3.scatter(x_color_z_pg, y_color_z_pg, c=sns.xkcd_rgb['green'], alpha=0.9, marker='*', s=490, zorder=100.0, edgecolor='black', label='J-PLUS PNG135.9+55.9')
ax3.errorbar(x_color_z_pg, y_color_z_pg, xerr=err_Val_pn135x_z, yerr=err_Val_pn135y_z, marker='.', fmt='k.', elinewidth=1.9, markeredgewidth=1.8, capsize=9)
ax3.scatter(B1[0], A1[0], color= sns.xkcd_rgb["aqua"], s=90, edgecolor='black', cmap=plt.cm.hot, label='Obs. hPNe')
(_, caps, _) = ax3.errorbar(B1[0], A1[0], xerr=0.0, yerr=0.0, marker='.', fmt='.', color= sns.xkcd_rgb["aqua"], elinewidth=0.8, markeredgewidth=0.8, markersize=8,)
for cap in caps:
    cap.set_markeredgewidth(1)
#ax3.scatter(B1[19], A1[19], c='y', alpha=0.8, s=40, label='Modeled halo PNe')
ax3.scatter(B1[15], A1[15], color= sns.xkcd_rgb["aqua"], cmap=plt.cm.hot, s=90, edgecolor='black', zorder=100)#, label='Obs. halo PNe')
# ax3.errorbar(B1[15], A1[15], yerr=0.3,  lolims= True,  marker='.', fmt='k.', elinewidth=.8, markeredgewidth=.8, markersize=8,)
# ax3.errorbar(B1[15], A1[15], xerr=0.3,  xlolims= True,  marker='.', fmt='k.', elinewidth=.8, markeredgewidth=.8, markersize=8,)

ax3.scatter(B1[16], A1[16], color= sns.xkcd_rgb["aqua"], cmap=plt.cm.hot, s=90, edgecolor='black')
(_, caps, _) = ax3.errorbar(B1[16], A1[16], xerr=0.0, yerr=0.0, marker='.', fmt='.', color= sns.xkcd_rgb["aqua"], elinewidth=0.8, markeredgewidth=0.8, markersize=8,)
for cap in caps:
    cap.set_markeredgewidth(1)
ax3.scatter(B1[17], A1[17], color= sns.xkcd_rgb["aqua"], s=90, edgecolor='black', cmap=plt.cm.hot)
(_, caps, _) = ax3.errorbar(B1[17], A1[17], xerr=0.0, yerr=0.0, marker='.', fmt='.', color= sns.xkcd_rgb["aqua"], elinewidth=0.8, markeredgewidth=0.8, markersize=8,)
for cap in caps:
    cap.set_markeredgewidth(1)

ax3.scatter(B1[1], A1[1], c=sns.xkcd_rgb['pale yellow'], alpha=0.8, s=40, cmap=plt.cm.hot, edgecolor='black',  zorder=10.0, label='SDSS CVs')
ax3.scatter(B1[4], A1[4],  c= "mediumaquamarine" , alpha=0.6, s=40, marker='D', cmap=plt.cm.hot, edgecolor='black', label='SDSS QSOs') #label='SDSS QSOs (1.3<z<1.4)')
ax3.scatter(B1[5], A1[5],  c= "mediumaquamarine", alpha=0.6, s=40, cmap=plt.cm.hot, edgecolor='black', marker='D')#,  label='SDSS QSOs (2.4<z<2.6)')
ax3.scatter(B1[6], A1[6],  c= "mediumaquamarine", alpha=0.6, s=40, marker='D', cmap=plt.cm.hot, edgecolor='black')#,  label='SDSS QSOs (3.2<z<3.4)')
ax3.scatter(B1[7], A1[7],  c= "goldenrod", alpha=0.8, s=60, marker='^', cmap=plt.cm.hot, edgecolor='black', label='SDSS SFGs ')
ax3.scatter(B1[8], A1[8],  c= "red", alpha=0.6, s=40, marker='s', cmap=plt.cm.hot, edgecolor='black', zorder=120.0, label='Obs. SySt ')
#ax3.scatter(B1[72], A1[72],  c= "red", alpha=0.8, marker='D', label='Symbiotics in NGC 55')
ax3.scatter(B1[12], A1[12],  c= "red", alpha=0.6, s=40, marker='s', cmap=plt.cm.hot, edgecolor='black', zorder=120.0)#, label='Obs. SySt in NGC 205')
ax3.scatter(B1[9], A1[9],  c= "red", alpha=0.6, s=60, marker='^', cmap=plt.cm.hot, edgecolor='black', zorder=120.0, label='IPHAS SySt')
ax3.scatter(B1[14], A1[14], c= "red" , alpha=0.6, s=40, marker='s', cmap=plt.cm.hot, edgecolor='black', zorder=120.0)#, label='Obs. SySt in IC10 ')
ax3.scatter(B1[13], A1[13],  c= "red", alpha=0.6, s=40, marker='s', cmap=plt.cm.hot, edgecolor='black', zorder=120.0)#, label='Obs. SySt in NGC 185')
#ax3.scatter(B1[73], A1[73],  c= "red", alpha=0.8, marker='o', label='C. Buil Symbiotics')
ax3.scatter(B1[10], A1[10],  c= "gray", alpha=0.6, marker='D', s=40, cmap=plt.cm.hot, edgecolor='black',  zorder=100.0, label='Obs. H II regions in NGC 55')
ax3.scatter(B1[18], A1[18],  c= "lightsalmon", alpha=0.8, s=100, marker='*', cmap=plt.cm.hot, edgecolor='black', label='Obs. YSOs')
ax3.scatter(B1[19], A1[19],  c=sns.xkcd_rgb['ultramarine blue'], alpha=0.8, s=90, cmap=plt.cm.hot, marker='*',  edgecolor='black', zorder=110, label='Obs. B[e] stars')
ax3.scatter(B1[20], A1[20],  c=sns.xkcd_rgb['neon purple'], alpha=0.8, s=90, cmap=plt.cm.hot, marker='*', edgecolor='black', zorder=110, label='Normal stars')

z, z_g = WS_splus("z_aper", "F660_aper", "g_aper")
ax3.scatter(z_g, z, c=sns.xkcd_rgb['mint green'], alpha=0.3, s=90, cmap=plt.cm.hot, marker='*', edgecolor='black', zorder=105, label='WDs from S-PLUS')

for label_, x, y in zip(label, B1[0], A1[0]):
    ax3.annotate(label_, (x, y), alpha=5, size=8,
                   xytext=(-5.0, -3.6), textcoords='offset points', ha='right', va='bottom',)
###################################################################
ax3.annotate("H4-1", (np.array(B1[15]), np.array(A1[15])), alpha=15, size=10,
                   xytext=(22, -17), textcoords='offset points', ha='right', va='bottom', bbox=bbox_props,)
ax3.annotate("PNG 135.9+55.9", (np.array(B1[16]), np.array(A1[16])), alpha=15, size=10,
                   xytext=(78, -14), textcoords='offset points', ha='right', va='bottom', zorder=100, bbox=bbox_props,)
# ax3.annotate("DdDm-1", (np.array(B1[17]), np.array(A1[17])), alpha=10, size=8,
#                    xytext=(-5, -10), textcoords='offset points', ha='right', va='bottom',)
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


# plt.annotate(
#     '', xy=(B1[2][0],  A1[2][0]+0.35), xycoords='data',                    #
#     xytext=(B1[42][0]+0.4, A1[42][0]+0.4), textcoords='data', fontsize = 7,# vector extinction
#     arrowprops=dict(edgecolor='black',arrowstyle= '<-'))                   #
# plt.annotate(
#     '', xy=(B1[2][0]+0.35,  A1[2][0]+0.35), xycoords='data',
#     xytext=(5, 0), textcoords='offset points', fontsize='x-small')

# Region where stay the PNe
result = findIntersection(0.35, 0.82, -0.8, 1.8, 0.0)
result_y = 0.2319*result + 0.85

x_new = np.linspace(result, 15.5, 200)
x_new2 = np.linspace(-10.0, result, 200)

y = 0.35*x_new + 0.82
yy = -0.8*x_new2 +  1.8
#Mask
#mask = y >= result_y - 0.5
ax3.plot(x_new, y, color='k', zorder=100, linestyle='-')
ax3.plot(x_new2, yy , color='k', zorder=100, linestyle='-')

# Region of the simbiotic stars=>
result1 = findIntersection(-1.96, -3.15, 0.2, 0.44, 0.0)
x_new_s = np.linspace(-15.5, result1, 200)
x_new2_s = np.linspace(-15.5, result1, 200)
y_s = -1.96*x_new_s - 3.15
yy_s = 0.2*x_new2_s + 0.44
# ax3.plot(x_new_s, y_s, color='r', zorder=100, linestyle='--')
# ax3.plot(x_new2_s, yy_s , color='r', zorder=100, linestyle='--')

#reddening vector
#redde_vector(0.777202578357, 2.86498835874, 0.269683304204, 2.61962188402, -5., 0, -0.3, 0.3) #E=0.2
redde_vector(0.7772025783566663, 2.8649883587381653, -0.9883877408051549, 1.9952077310511251, -4.5, 0, -0.3, 0.3)

#for Z, x, y in zip(z, d_768_Qz, d_644_Qz):
    #ax3.annotate("{:.3f}".format(Z), (x, y), fontsize='x-small',
                       #xytext=(5,-5), textcoords='offset points', ha='left', bbox={"boxstyle": "round", "fc": "white", "ec": "none", "alpha": 0.5}, alpha=0.7)
#ax3.set_title(" ".join([cmd_args.source]))
#ax3.grid(True)
#ax3.annotate('Higher z(3.288)', xy=(0.08749580383300781, 0.181182861328125), xytext=(-0.5, -0.58),
             #arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))
#ax3.annotate('Lower z(3.065)', xy=(0.3957328796386719, 0.1367034912109375), xytext=(0.5, -0.58),
             #arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))
ax3.minorticks_on()
#ax3.grid(which='minor')#, lw=0.3)
ax3.legend(scatterpoints=1, ncol=2, fontsize=11.0, loc='lower right', **lgd_kws)
#ax3.grid()
#lgd = ax3.legend(loc='center right', bbox_to_anchor=(1.27, 0.5), fontsize=7.5, **lgd_kws)
#ax3.grid(which='minor', lw=0.5)
#sns.despine(bottom=True)
plt.tight_layout()
plt.text(0.35, 0.92, 'CLOUDY modelled hPNe',
         transform=ax3.transAxes, fontsize='large')
# ax3.annotate('CLOUDY modelled halo PNe', xy=(-0.17, 3.1), xycoords='data',
#              xytext=(-2.0, 4.0), textcoords='data'),
              # arrowprops=dict(arrowstyle="->",
              #                 color="0.0",
              #                  shrinkA = 10, shrinkB = 5,
              #                  patchA = None,
              #                  patchB = None,
              #                  connectionstyle=None,
              #                   ),
              # )

#plt.savefig('luis-JPLUS-Viironen.pdf')#,  bbox_extra_artists=(lgd,), bbox_inches='tight')
pltfile = 'Fig3-JPLUS17-z-g.pdf'
file_save = os.path.join(save_path, pltfile)
plt.savefig(file_save)
#plt.savefig('Fig3-JPLUS17-z-g.pdf')
plt.clf()

##########################################################################################################################################
label = []
label1 = ["H4-1", "PNG 135.9+55.9"]
n = 21
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
        plot_mag("F660", "F480_g_sdss", "F625_r_sdss")
        
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
ax4 = fig.add_subplot(111, facecolor="#eeeeee")
ax4.set_xlim(xmin=-2.5,xmax=0.5)
ax4.set_ylim(ymin=-5.0,ymax=1.0)
#ax4.set_xlim(xmin=-2.5,xmax=2.0)
plt.tick_params(axis='x', labelsize=18) 
plt.tick_params(axis='y', labelsize=18)
plt.xlabel(r'$J0660 - r$', fontsize= 18)
plt.ylabel(r'$J0660 - g$', fontsize= 18)
#plt.plot( 'x', 'y', data=df, linestyle='', marker='o')
ax4.scatter(y, x, c=z, s=50, edgecolor='')
ax4.scatter(B1[0], A1[0], color= sns.xkcd_rgb["aqua"], alpha=0.8, s=40, cmap=plt.cm.hot, label='Obs. hPNe')
(_, caps, _) = ax4.errorbar(B1[0], A1[0], xerr=0.0, yerr=0.0, marker='.', fmt='k.', elinewidth=0.8, markeredgewidth=0.8, markersize=8,)
for cap in caps:
    cap.set_markeredgewidth(1)
#ax4.scatter(B1[19], A1[19], c='y', alpha=0.8, s=40, label='Modeled halo PNe')
ax4.scatter(B1[15], A1[15], c='black', alpha=0.8, cmap=plt.cm.hot, s=40)#, label='Obs. halo PNe')
# ax4.errorbar(B1[15], A1[15], yerr=0.2,  lolims= True,  marker='.', fmt='k.', elinewidth=.8, markeredgewidth=.8, markersize=8,)
# ax4.errorbar(B1[15], A1[15], xerr=0.2,  xlolims= True,  marker='.', fmt='k.', elinewidth=.8, markeredgewidth=.8, markersize=8,)
ax4.scatter(B1[16], A1[16], c='black', alpha=0.8, cmap=plt.cm.hot, s=40)
(_, caps, _) = ax4.errorbar(B1[16], A1[16], xerr=0.0, yerr=0.0, marker='.', fmt='k.', elinewidth=0.8, markeredgewidth=0.8, markersize=8,)
for cap in caps:
    cap.set_markeredgewidth(1)
ax4.scatter(B1[17], A1[17], c='black', alpha=0.8, s=40, cmap=plt.cm.hot)
(_, caps, _) = ax4.errorbar(B1[17], A1[17], xerr=0.0, yerr=0.0, marker='.', fmt='k.', elinewidth=0.8, markeredgewidth=0.8, markersize=8,)
for cap in caps:
    cap.set_markeredgewidth(1)

ax4.scatter(B1[1], A1[1], c='purple', alpha=0.6, s=40, cmap=plt.cm.hot, label='SDSS CVs')
ax4.scatter(B1[4], A1[4],  c= "mediumaquamarine" , alpha=0.6, s=40, marker='D', cmap=plt.cm.hot, label='SDSS QSOs') #label='SDSS QSOs (1.3<z<1.4)')
ax4.scatter(B1[5], A1[5],  c= "mediumaquamarine", alpha=0.6, s=40, cmap=plt.cm.hot, marker='D')#,  label='SDSS QSOs (2.4<z<2.6)')
ax4.scatter(B1[6], A1[6],  c= "mediumaquamarine", alpha=0.6, s=40, marker='D', cmap=plt.cm.hot)#,  label='SDSS QSOs (3.2<z<3.4)')
ax4.scatter(B1[7], A1[7],  c= "goldenrod", alpha=0.8, s=60, marker='^', cmap=plt.cm.hot, label='SDSS SFGs ')
ax4.scatter(B1[8], A1[8],  c= "red", alpha=0.6, s=40, marker='s', cmap=plt.cm.hot, label='Obs. SySt ')
#ax4.scatter(B1[72], A1[72],  c= "red", alpha=0.8, marker='D', label='Symbiotics in NGC 55')
ax4.scatter(B1[12], A1[12],  c= "red", alpha=0.6, s=40, marker='D', cmap=plt.cm.hot, label='Obs. SySt in NGC 205')
ax4.scatter(B1[9], A1[9],  c= "red", alpha=0.6, s=40, marker='^', cmap=plt.cm.hot, label='IPHAS SySt')
ax4.scatter(B1[14], A1[14], c= "red" , alpha=0.6, s=40, marker='o', cmap=plt.cm.hot, label='Obs. SySt in IC10 ')
ax4.scatter(B1[13], A1[13],  c= "red", alpha=0.6, s=40, marker='v', cmap=plt.cm.hot, label='Obs. SySt in NGC 185')
#ax4.scatter(B1[73], A1[73],  c= "red", alpha=0.8, marker='o', label='C. Buil Symbiotics')
ax4.scatter(B1[10], A1[10],  c= "gray", alpha=0.6, marker='D', s=40, cmap=plt.cm.hot, zorder=100.0, label='Obs. HII region in NGC 55')
ax4.scatter(B1[18], A1[18],  c= "lightsalmon", alpha=0.8, s=42, marker='*', cmap=plt.cm.hot, label='Obs. YSOs')

for label_, x, y in zip(label, B1[0], A1[0]):
    ax4.annotate(label_, (x, y), alpha=5, size=8,
                   xytext=(-4.0, 3.6), textcoords='offset points', ha='right', va='bottom',)
###################################################################
ax4.annotate("H4-1", (np.array(B1[15]), np.array(A1[15])), alpha=5, size=9,
                   xytext=(-7, -12), textcoords='offset points', ha='right', va='bottom', bbox=bbox_props,)
ax4.annotate("PNG 135.9+55.9", (np.array(B1[16]), np.array(A1[16])), alpha=5, size=9,
                   xytext=(-5, -10), textcoords='offset points', ha='right', va='bottom', bbox=bbox_props,)
# ax4.annotate("DdDm-1", (np.array(B1[17]), np.array(A1[17])), alpha=10, size=8,
#                    xytext=(35, -10), textcoords='offset points', ha='right', va='bottom',)
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


#for label_, x, y in zip(can_alh, d_768_cAlh, d_644_cAlh):
    #ax4.annotate(label_, (x, y), alpha=0.9, size=8,
                   #xytext=(3,-10), textcoords='offset points', ha='left', va='bottom',)
# plt.annotate(
#     '', xy=(B1[2][0],  A1[2][0]+0.35), xycoords='data',                    #
#     xytext=(B1[42][0]+0.4, A1[42][0]+0.4), textcoords='data', fontsize = 7,# vector extinction
#     arrowprops=dict(edgecolor='black',arrowstyle= '<-'))                   #
# plt.annotate(
#     '', xy=(B1[2][0]+0.35,  A1[2][0]+0.35), xycoords='data',
#     xytext=(5, 0), textcoords='offset points', fontsize='x-small')

# Region where stay the PNe
result = findIntersection(1.58, 0.62, 5.8, 2.7, 0.0)
result_y = 1.559*result + 0.58

x_new = np.linspace(-10.0, result, 200)
x_new2 = np.linspace(result, 10.0 , 200)
x_new3 = np.linspace(-10.0, 1.1, 200)
y = 1.58*x_new + 0.62
yy = 5.8*x_new2 + 2.7
#Mask
#mask = y >= result_y - 0.5
ax4.plot(x_new, y, color='k', zorder=100, linestyle='-')
ax4.plot(x_new2, yy, color='k', zorder=100, linestyle='-')

# Region of the simbiotic stars=>
result1 = findIntersection(1.497, -0.12, 2.76, 0.49, 0.0)
x_new_s = np.linspace(-15.5, result1, 200)
x_new2_s = np.linspace(-15.5, result1, 200)
y_s = 1.497*x_new_s - 0.12
yy_s = 2.76*x_new2_s + 0.49
ax4.plot(x_new_s, y_s, color='r', zorder=100, linestyle='--')
ax4.plot(x_new2_s, yy_s , color='r', zorder=100, linestyle='--')


#for Z, x, y in zip(z, d_768_Qz, d_644_Qz):
    #ax4.annotate("{:.3f}".format(Z), (x, y), fontsize='x-small',
                       #xytext=(5,-5), textcoords='offset points', ha='left', bbox={"boxstyle": "round", "fc": "white", "ec": "none", "alpha": 0.5}, alpha=0.7)
#ax4.set_title(" ".join([cmd_args.source]))
#ax4.grid(True)
#ax4.annotate('Higher z(3.288)', xy=(0.08749580383300781, 0.181182861328125), xytext=(-0.5, -0.58),
             #arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))
#ax4.annotate('Lower z(3.065)', xy=(0.3957328796386719, 0.1367034912109375), xytext=(0.5, -0.58),
             #arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))
ax4.minorticks_on()
#ax4.grid(which='minor')#, lw=0.3)
ax4.legend(scatterpoints=1, ncol=1, fontsize=7.0, loc='lower right', **lgd_kws)
#ax4.grid()
#lgd = ax4.legend(loc='center right', bbox_to_anchor=(1.27, 0.5), fontsize=7.5, **lgd_kws)
#ax4.grid(which='minor', lw=0.5)
#sns.despine(bottom=True)
plt.tight_layout()
plt.text(0.05, 0.05, 'CLOUDY modelled hPNe',
         transform=ax4.transAxes, fontsize='x-small')

# fit curve models

def fit(ax, x,y, sort=True):
    z = np.polyfit(x, y, 1)
    fit = np.poly1d(z)
    print(fit)
    ax.set_title("unsorted")
    if sort:
        x = np.sort(x)
        ax.set_title("sorted")
    print('Modelled PNe fit: = {:.2f} colx**{:.2f}'.format(z[1], z[0]))
    ax.plot(x, fit(x), label="fit func", color="k", alpha=1, lw=2.5)  

#fit(ax4, B1[2], A1[2])
# Fit find -0.5606 x - 0.4646 x - 0.5567 lineal 1.459 x + 0.9515

# t = np.linspace(-3.0, 0.5, 200)
# tt = 1.459*t + 0.5
# ax4.plot(t, tt, c="r")

#plt.savefig('luis-JPLUS-Viironen.pdf')#,  bbox_extra_artists=(lgd,), bbox_inches='tight')
pltfile = 'Fig4-JPLUS17-J0660-r.pdf'
file_save = os.path.join(save_path, pltfile)
plt.savefig(file_save)
#plt.savefig('Fig4-JPLUS17-J0660-r.pdf')
plt.clf()

##########################################################################################################################################
label = []
label1 = ["H4-1", "PNG 135.9+55.9"]
n = 21
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
        plot_mag("F348", "F660", "F861")
        
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
ax4 = fig.add_subplot(111, facecolor="#eeeeee")
ax4.set_xlim(xmin=-2.0,xmax=5.5)
ax4.set_ylim(ymin=-2.3,ymax=5.5)
#ax4.set_xlim(xmin=-2.5,xmax=2.0)
plt.tick_params(axis='x', labelsize=18) 
plt.tick_params(axis='y', labelsize=18)
plt.xlabel(r'$uJAVA - J0861$', fontsize= 18)
plt.ylabel(r'$uJAVA - J0660$', fontsize= 18)
#plt.plot( 'x', 'y', data=df, linestyle='', marker='o')
ax4.scatter(y, x, c=z, s=50, edgecolor='')
ax4.scatter(B1[0], A1[0], c='black', alpha=0.8, s=40, cmap=plt.cm.hot, label='Obs. halo PNe')
(_, caps, _) = ax4.errorbar(B1[0], A1[0], xerr=0.0, yerr=0.0, marker='.', fmt='k.', elinewidth=0.8, markeredgewidth=0.8, markersize=8,)
for cap in caps:
    cap.set_markeredgewidth(1)
#ax4.scatter(B1[19], A1[19], c='y', alpha=0.8, s=40, label='Modeled halo PNe')
ax4.scatter(B1[15], A1[15], c='black', alpha=0.8, cmap=plt.cm.hot, s=40)#, label='Obs. halo PNe')
# ax4.errorbar(B1[15], A1[15], yerr=0.2,  lolims= True,  marker='.', fmt='k.', elinewidth=.8, markeredgewidth=.8, markersize=8,)
# ax4.errorbar(B1[15], A1[15], xerr=0.2,  xlolims= True,  marker='.', fmt='k.', elinewidth=.8, markeredgewidth=.8, markersize=8,)

ax4.scatter(B1[16], A1[16], c='black', cmap=plt.cm.hot, s=40)
(_, caps, _) = ax4.errorbar(B1[16], A1[16], xerr=0.0, yerr=0.0, marker='.', fmt='k.', elinewidth=0.8, markeredgewidth=0.8, markersize=8,)
for cap in caps:
    cap.set_markeredgewidth(1)
ax4.scatter(B1[17], A1[17], c='black', alpha=0.8, s=40, cmap=plt.cm.hot)
(_, caps, _) = ax4.errorbar(B1[17], A1[17], xerr=0.0, yerr=0.0, marker='.', fmt='k.', elinewidth=0.8, markeredgewidth=0.8, markersize=8,)
for cap in caps:
    cap.set_markeredgewidth(1)

ax4.scatter(B1[1], A1[1], c=sns.xkcd_rgb['purple'], alpha=0.6, s=40, cmap=plt.cm.hot, label='SDSS CVs')
ax4.scatter(B1[4], A1[4],  c= "mediumaquamarine" , alpha=0.6, s=40, marker='D', cmap=plt.cm.hot, label='SDSS QSOs') #label='SDSS QSOs (1.3<z<1.4)')
ax4.scatter(B1[5], A1[5],  c= "mediumaquamarine", alpha=0.6, s=40, cmap=plt.cm.hot, marker='D')#,  label='SDSS QSOs (2.4<z<2.6)')
ax4.scatter(B1[6], A1[6],  c= "mediumaquamarine", alpha=0.6, s=40, marker='D', cmap=plt.cm.hot)#,  label='SDSS QSOs (3.2<z<3.4)')
ax4.scatter(B1[7], A1[7],  c= "goldenrod", alpha=0.6, s=40, marker='^', cmap=plt.cm.hot, label='SDSS SFGs ')
ax4.scatter(B1[8], A1[8],  c= "red", alpha=0.6, s=40, marker='s', cmap=plt.cm.hot, label='Obs. SySt ')
#ax4.scatter(B1[72], A1[72],  c= "red", alpha=0.8, marker='D', label='Symbiotics in NGC 55')
ax4.scatter(B1[12], A1[12],  c= "red", alpha=0.6, s=40, marker='D', cmap=plt.cm.hot, label='Obs. SySt in NGC 205')
ax4.scatter(B1[9], A1[9],  c= "red", alpha=0.6, s=40, marker='^', cmap=plt.cm.hot, label='IPHAS SySt')
ax4.scatter(B1[14], A1[14], c= "red" , alpha=0.6, s=40, marker='o', cmap=plt.cm.hot, label='Obs. SySt in IC10 ')
ax4.scatter(B1[13], A1[13],  c= "red", alpha=0.6, s=40, marker='v', cmap=plt.cm.hot, zorder=100, label='Obs. SySt in NGC 185')
#ax4.scatter(B1[73], A1[73],  c= "red", alpha=0.8, marker='o', label='C. Buil Symbiotics')
ax4.scatter(B1[10], A1[10],  c= "gray", alpha=0.6, marker='D', s=40, cmap=plt.cm.hot, zorder=100.0, label='Obs. HII region in NGC 55')
ax4.scatter(B1[18], A1[18],  c= "lightsalmon", alpha=0.8, s=42, marker='*', cmap=plt.cm.hot, label='Obs. YSOs')

for label_, x, y in zip(label, B1[0], A1[0]):
    ax4.annotate(label_, (x, y), alpha=5, size=8,
                   xytext=(-4.0, 3.6), textcoords='offset points', ha='right', va='bottom',)
###################################################################
ax4.annotate("H4-1", (np.array(B1[15]), np.array(A1[15])), alpha=5, size=9,
                   xytext=(-5, -10), textcoords='offset points', ha='right', va='bottom', bbox=bbox_props,)
ax4.annotate("PNG 135.9+55.9", (np.array(B1[16]), np.array(A1[16])), alpha=5, size=9,
                   xytext=(-5, -10), textcoords='offset points', ha='right', va='bottom', bbox=bbox_props,)
# ax4.annotate("DdDm-1", (np.array(B1[17]), np.array(A1[17])), alpha=10, size=8,
#                    xytext=(35, -10), textcoords='offset points', ha='right', va='bottom',)
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


#for label_, x, y in zip(can_alh, d_768_cAlh, d_644_cAlh):
    #ax4.annotate(label_, (x, y), alpha=0.9, size=8,
                   #xytext=(3,-10), textcoords='offset points', ha='left', va='bottom',)
# plt.annotate(
#     '', xy=(B1[2][0],  A1[2][0]+0.35), xycoords='data',                    #
#     xytext=(B1[42][0]+0.4, A1[42][0]+0.4), textcoords='data', fontsize = 7,# vector extinction
#     arrowprops=dict(edgecolor='black',arrowstyle= '<-'))                   #
# plt.annotate(
#     '', xy=(B1[2][0]+0.35,  A1[2][0]+0.35), xycoords='data',
#     xytext=(5, 0), textcoords='offset points', fontsize='x-small')

# Region where stay the PNe
result = findIntersection(1.58, 0.62, 5.8, 2.7, 0.0)
result_y = 1.559*result + 0.58

x_new = np.linspace(-10.0, result, 200)
x_new2 = np.linspace(result, 10.0 , 200)
x_new3 = np.linspace(-10.0, 1.1, 200)
y = 1.58*x_new + 0.62
yy = 5.8*x_new2 + 2.7
#Mask
#mask = y >= result_y - 0.5
ax4.plot(x_new, y, color='k', linestyle='-')
ax4.plot(x_new2, yy, color='k', linestyle='-')

# Region of the simbiotic stars=>
result1 = findIntersection(1.497, -0.12, 2.76, 0.49, 0.0)
x_new_s = np.linspace(-15.5, result1, 200)
x_new2_s = np.linspace(-15.5, result1, 200)
y_s = 1.497*x_new_s - 0.12
yy_s = 2.76*x_new2_s + 0.49
ax4.plot(x_new_s, y_s, color='r', linestyle='--')
ax4.plot(x_new2_s, yy_s , color='r', linestyle='--')


#for Z, x, y in zip(z, d_768_Qz, d_644_Qz):
    #ax4.annotate("{:.3f}".format(Z), (x, y), fontsize='x-small',
                       #xytext=(5,-5), textcoords='offset points', ha='left', bbox={"boxstyle": "round", "fc": "white", "ec": "none", "alpha": 0.5}, alpha=0.7)
#ax4.set_title(" ".join([cmd_args.source]))
#ax4.grid(True)
#ax4.annotate('Higher z(3.288)', xy=(0.08749580383300781, 0.181182861328125), xytext=(-0.5, -0.58),
             #arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))
#ax4.annotate('Lower z(3.065)', xy=(0.3957328796386719, 0.1367034912109375), xytext=(0.5, -0.58),
             #arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))
ax4.minorticks_on()
#ax4.grid(which='minor')#, lw=0.3)
ax4.legend(scatterpoints=1, ncol=1, fontsize=7.0, loc='lower right', **lgd_kws)
#ax4.grid()
#lgd = ax4.legend(loc='center right', bbox_to_anchor=(1.27, 0.5), fontsize=7.5, **lgd_kws)
#ax4.grid(which='minor', lw=0.5)
#sns.despine(bottom=True)
plt.tight_layout()
plt.text(0.05, 0.05, 'CLOUDY modelled halo PNe',
         transform=ax4.transAxes, fontsize='x-small')

# fit curve models

def fit(ax, x,y, sort=True):
    z = np.polyfit(x, y, 1)
    fit = np.poly1d(z)
    print(fit)
    ax.set_title("unsorted")
    if sort:
        x = np.sort(x)
        ax.set_title("sorted")
    print('Modelled PNe fit: = {:.2f} colx**{:.2f}'.format(z[1], z[0]))
    ax.plot(x, fit(x), label="fit func", color="k", alpha=1, lw=2.5)  

#fit(ax4, B1[2], A1[2])
# Fit find -0.5606 x - 0.4646 x - 0.5567 lineal 1.459 x + 0.9515

# t = np.linspace(-3.0, 0.5, 200)
# tt = 1.459*t + 0.5
# ax4.plot(t, tt, c="r")

#plt.savefig('luis-JPLUS-Viironen.pdf')#,  bbox_extra_artists=(lgd,), bbox_inches='tight')
pltfile = 'Fig8-JPLUS17-uJAVA-J0660.pdf'
file_save = os.path.join(save_path, pltfile)
plt.savefig(file_save)
#plt.savefig('Fig8-JPLUS17-uJAVA-J0660.pdf')
plt.clf()

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
    x31, y31 = filter_mag("galaxy", "", f1, f2, f3)
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
    for a, b in zip(x31, y31):
        A1[21].append(a)
        B1[21].append(b)
        
label = []
label1 = ["H4-1", "PNG 135.9+55.9"]
n = 22
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
datadir = "WD_ariel-spectros--/"
fitsfile = "WD_splus_obs.fits"
hdulist= fits.open(os.path.join(datadir, fitsfile))

def WS_splus(filter_1, filter_2, filter_3):
    band1 = hdulist[1].data[filter_1]
    band2 = hdulist[1].data[filter_2]
    band3 = hdulist[1].data[filter_3]
    return (band1 - band2), (band1 - band3)

##############################################################################
##############################################################################
#MS from S-PLUS ##############################################################
##############################################################################
##############################################################################
patternn = "MS-G-spectros/*-JPLUS17-magnitude.json"
file_list1 = glob.glob(patternn)


def filter_mag_MS(e, s, f1, f2, f3):
    '''
    Calculate the colors using any of set of filters
    '''
    col, col0 = [], []
    if data1['id'].endswith(e):
        if data1['id'].startswith(str(s)):
            filter1 = data1[f1]
            filter2 = data1[f2]
            filter3 = data1[f3]
            diff = filter1 - filter2
            diff0 = filter1 - filter3
            col.append(diff)
            col0.append(diff0)
    
    return col, col0

def plot_mag_MS(f1, f2, f3):
    x, y = filter_mag_MS("", "g", f1, f2, f3)
    x1, y1 = filter_mag_MS("", "k", f1, f2, f3)
    x2, y2 = filter_mag_MS("", "ukg", f1, f2, f3)
    x3, y3 = filter_mag_MS("", "ukk", f1, f2, f3)
    for a, b in zip(x, y):
        AA1.append(a)
        BB1.append(b)
    for a, b in zip(x1, y1):
        AA1.append(a)
        BB1.append(b)
    for a, b in zip(x2, y2):
        AA1.append(a)
        BB1.append(b)
    for a, b in zip(x3, y3):
        AA1.append(a)
        BB1.append(b)
    
AA1, BB1 = [], []

for file_name1 in file_list1:
    with open(file_name1) as f1:
        data1 = json.load(f1)
        plot_mag_MS("F625_r_sdss", "F660", "F766_i_sdss")

##############################################################################
#plots
lgd_kws = {'frameon': True, 'fancybox': True, 'shadow': True}
#sns.set(style="dark", context="talk")
#sns.set_style('ticks')
fig = plt.figure(figsize=(7, 6))
ax1 = fig.add_subplot(111, facecolor="#eeeeee")
ax1.set_xlim(xmin=-3.7,xmax=3.7)
ax1.set_ylim(ymin=-2.4,ymax=2.8)
#ax1.set_xlim(xmin=-2.5,xmax=2.0)
plt.tick_params(axis='x', labelsize=25) 
plt.tick_params(axis='y', labelsize=25)
plt.xlabel(r'$r - i$', fontsize= 25)
plt.ylabel(r'$r - J0660$', fontsize= 25)
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
ax1.scatter(B1[7], A1[7],  c= "goldenrod", alpha=0.5, s=60, marker='^', cmap=plt.cm.hot, zorder=11.0, edgecolor='black', label='SDSS SFGs ')
ax1.scatter(B1[8], A1[8],  c= "red", alpha=0.6, s=40, marker='s', cmap=plt.cm.hot, edgecolor='black', zorder=120.0, label='Obs. SySt')
#ax1.scatter(B1[72], A1[72],  c= "red", alpha=0.8, marker='D', label='Symbiotics in NGC 55')
ax1.scatter(B1[12], A1[12],  c= "red", alpha=0.6, s=40, marker='s', cmap=plt.cm.hot, edgecolor='black', zorder=120.0)#, label='Obs. SySts in NGC 205')
ax1.scatter(B1[9], A1[9],  c= "red", alpha=0.6, s=60, marker='^', cmap=plt.cm.hot, edgecolor='black', zorder=120.0, label='IPHAS SySt')
ax1.scatter(B1[11], A1[11],  c='red', alpha=0.6, s=40, marker='s', cmap=plt.cm.hot, edgecolor='black', zorder=120.0)
ax1.scatter(B1[14], A1[14],  c='red', alpha=0.6, s=40, marker='s', cmap=plt.cm.hot, edgecolor='black', zorder=120.0)#, label='Obs. SySts in IC10 ')
ax1.scatter(B1[13], A1[13],  c= "red", alpha=0.6, s=40, marker='s', cmap=plt.cm.hot, edgecolor='black', zorder=120.0)#, label='Obs. SySts in NGC 185')
#ax1.scatter(B1[73], A1[73],  c= "red", alpha=0.8, marker='o', label='C. Buil Symbiotics')
ax1.scatter(B1[10], A1[10],  c= "gray", alpha=0.6, s=40, marker='D', cmap=plt.cm.hot, zorder=120.0, edgecolor='black', label='Obs. H II regions in NGC 55')
ax1.scatter(B1[21], A1[21], color= sns.xkcd_rgb["pink"], alpha=0.6, s=40, marker='D', cmap=plt.cm.hot, zorder=120.0, edgecolor='black', label='SDSS BCGs')
#ax1.scatter(B1[74], A1[74],  c= "black", alpha=0.8, marker='.', label='SN Remanents')
ax1.scatter(B1[18], A1[18],  c= "lightsalmon", alpha=0.8, s=100, cmap=plt.cm.hot, marker='*',  edgecolor='black', label='Obs. YSOs')
ax1.scatter(B1[19], A1[19],  c=sns.xkcd_rgb['ultramarine blue'], alpha=0.8, s=90, cmap=plt.cm.hot, marker='*',  edgecolor='black', zorder=110, label='Obs. B[e] stars')

redde_vector(-1.2314754077697903, 2.147731023789999, -0.8273818571912539, 2.1826566358487645, 4., 0, -0.6, -0.15) #E=0.7

left, bottom, width, height = [0.215, 0.61, 0.23, 0.23]
ax11 = fig.add_axes([left, bottom, width, height])
ax11.set_xlim(xmin=-3.7,xmax=3.7)
ax11.set_ylim(ymin=-2.4,ymax=2.8)
ax11.scatter(B1[20], A1[20], c=sns.xkcd_rgb['neon purple'], alpha=0.3, s=20, cmap=plt.cm.hot, marker='*', zorder=110, label='MS stars')
ax11.scatter(BB1, AA1,  c=sns.xkcd_rgb['brown'], s=20, cmap=plt.cm.hot, marker='*', zorder=110, label='Giant stars')
r_660, r_i = WS_splus("r_aper", "F660_aper", "i_aper")
ax11.scatter(r_i, r_660, c=sns.xkcd_rgb['mint green'], alpha=0.8, s=20, cmap=plt.cm.hot, marker='*',  zorder=105, label='S-PLUS WDs')
ax11.text(0.08, 0.68, 'hPNe',
          transform=ax11.transAxes, fontsize=14)
ax11.spines['top'].set_visible(False)
ax11.spines['right'].set_visible(False)
ax11.annotate("MS", xy=(1.28, 0.25), xytext=(1, 2), color='purple', size=14,  zorder= 111, arrowprops=dict(arrowstyle="->", color='purple'))
ax11.annotate("Giant", xy=(0.3, 0.2), xytext=(0.5, -2), color=sns.xkcd_rgb['brown'], size=14, zorder= 111, arrowprops=dict(arrowstyle="->", color=sns.xkcd_rgb['brown']))
ax11.annotate("WD", xy=(-0.5, -0.48), xytext=(-2.5, -2.0), color='green', size=14, zorder= 111, arrowprops=dict(arrowstyle="->",  color='green'))

#ax11.legend(scatterpoints=1, ncol=2, fontsize=6.3, loc='lower right', **lgd_kws)

#################################################################

for label_, x, y in zip(label, B1[0], A1[0]):
    ax1.annotate(label_, (x, y), alpha=5, size=8,
                   xytext=(-5.0, -10.0), textcoords='offset points', ha='right', va='bottom',)
###################################################################
bbox_props = dict(boxstyle="round", fc="w", ec="0.78", alpha=0.5, pad=0.1)
ax1.annotate("H4-1", (np.array(B1[15]), np.array(A1[15])), alpha=15, size=10.0,
                   xytext=(-7, -10), textcoords='offset points', ha='right', va='bottom', bbox=bbox_props, zorder=100)
ax1.annotate("PNG135.9+55.9", (np.array(B1[16]), np.array(A1[16])), alpha=15, size=10,
                   xytext=(-8, -10), textcoords='offset points', ha='right', va='bottom', bbox=bbox_props, zorder=2500)
# ax1.annotate("DdDm-1", (np.array(B1[17]), np.array(A1[17])), alpha=10, size=8,
#                    xytext=(-5, -10), textcoords='offset points', ha='right', va='bottom',)
##################################################################
#Obersevado porJPLUS
#for label_, x, y in zip(label1, d_768_jplus[0], d_644_jplus[0]):
# ax1.annotate("H4-1", (d_768_jplus[0], d_644_jplus[0]), alpha=8, size=8,
#                    xytext=(-5, 3), textcoords='offset points', ha='right', va='bottom', color='blue',)

# ax1.annotate("PNG 135.9+55.9", (d_768_jplus[1], d_644_jplus[1]), alpha=8, size=8,
#                    xytext=(68, -10), textcoords='offset points', ha='right', va='bottom', color='green',)

#Region Halpha Emitters
x_new = np.linspace(-15.0, 1000, 200)
y =  0.25*x_new + 0.5 
#y1 =  0.25*x_new + 0.87

#Mask
#mask = y >= result_y - 0.5
ax1.plot(x_new, y, color='k', zorder=125, linestyle='-.')
ax11.plot(x_new, y, color='k', zorder=125, linestyle='-.')
textbb = {"facecolor": "white", "alpha": 0.7, "edgecolor": "none"}
textpars = {'ha': 'center', 'va': 'center', 'bbox': textbb, 'fontsize': 'small'}
plt.text(0.1, -4.1, 'r - Halpha = 0.25*(r - 1) + 0.5', rotation=np.degrees(np.arctan(0.25)), rotation_mode='anchor', **textpars)

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
         transform=ax1.transAxes, fontsize=13.8)

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
pltfile = 'Fig-JPLUS17-Viironen-HalphaEmitters.pdf'
save_path = '../../Dropbox/JPAS/Tesis/Fig/'
file_save = os.path.join(save_path, pltfile)
plt.savefig(file_save)
#plt.savefig('Fig1-JPLUS17-Viironen.pdf')
plt.clf()















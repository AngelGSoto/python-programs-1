'''
Make color-color diagrams for JPLUS 2017
'''
from __future__ import print_function
import numpy as np
import glob
import json
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import gaussian_kde
import sys
import pandas as pd
from astropy.table import Table
#import StringIO
from scipy.optimize import fsolve
import os
from astropy.io import fits

#Find the point inteception between two lines     
def findIntersection(m, y, m1, y1, x0):
    x = np.linspace(-10.0, 15.5, 200)
    return fsolve(lambda x : (m*x + y) - (m1*x + y1), x0)

pattern = "*-spectros/*-JPLUS17-magnitude.json"
file_list = glob.glob(pattern)

#reddenign vector
def redde_vector(x0, y0, x1, y1, a, b, c, d):
    plt.arrow(x0+a, y0+b, (x1+a)-(x0+a), (y1+b)-(y0+b),  fc="k", ec="k", width=0.01,
              head_width=0.07, head_length=0.15) #head_width=0.05, head_length=0.1)
    plt.text(x0+a+c, y0+b+d, 'A$_\mathrm{V}=2$', va='center', fontsize='x-large')

def filter_mag(e, s, f1, f2, f3, f4):
    '''
    Calculate the colors using any of set of filters
    '''
    col, col0 = [], []
    if data['id'].endswith(e):
        if data['id'].startswith(str(s)):
            filter1 = data[f1]
            filter2 = data[f2]
            filter3 = data[f3]
            filter4 = data[f4]
            diff = filter1 - filter2
            diff0 = filter3 - filter4
            col.append(diff)
            col0.append(diff0)
    
    return col, col0

def plot_mag(f1, f2, f3, f4):
    x, y = filter_mag("HPNe", "", f1, f2, f3, f4)
    x1, y1 = filter_mag("CV", "", f1, f2, f3, f4)
    x2, y2 = filter_mag("E00_300", "", f1, f2, f3, f4)
    x3, y3 = filter_mag("E01_300", "", f1, f2, f3, f4)
    x4, y4 = filter_mag("E02_300", "", f1, f2, f3, f4)
    x5, y5 = filter_mag("E00_600", "", f1, f2, f3, f4)
    x6, y6 = filter_mag("E01_600", "", f1, f2, f3, f4)
    x7, y7 = filter_mag("E02_600", "", f1, f2, f3, f4)
    x8, y8= filter_mag("-DPNe", "", f1, f2, f3, f4)
    x9, y9= filter_mag("QSOs-13", "", f1, f2, f3, f4)
    x10, y10 = filter_mag("QSOs-24", "",  f1, f2, f3, f4)
    x11, y11 = filter_mag("QSOs-32", "", f1, f2, f3, f4)
    x12, y12 = filter_mag("-SFGs", "", f1, f2, f3, f4)
    x13, y13 = filter_mag("-sys", "", f1, f2, f3, f4)
    x14, y14 = filter_mag("-sys-IPHAS", "", f1, f2, f3, f4) 
    x15, y15 = filter_mag("-ExtHII", "", f1, f2, f3, f4)
    x16, y16 = filter_mag("-sys-Ext", '', f1, f2, f3, f4)
    x17, y17 = filter_mag("-survey", '', f1, f2, f3, f4)
    x18, y18 = filter_mag("-SNR", '', f1, f2, f3, f4)
    x19, y19 = filter_mag("extr-SySt", '', f1, f2, f3, f4)
    x20, y20 = filter_mag("ngc185", "", f1, f2, f3, f4)
    x21, y21 = filter_mag("SySt-ic10", "", f1, f2, f3, f4)
    x22, y22 = filter_mag("H41-HPNe-", "", f1, f2, f3, f4)
    x23, y23 = filter_mag("1359559-HPNe-", "", f1, f2, f3, f4)
    x24, y24 = filter_mag("DdDm-1-HPNe-", "", f1, f2, f3, f4)
    x25, y25 = filter_mag("YSOs", "", f1, f2, f3, f4)
    x26, y26 = filter_mag("E00_100", "", f1, f2, f3, f4)
    x27, y27 = filter_mag("E01_100", "", f1, f2, f3, f4)
    x28, y28 = filter_mag("E02_100", "", f1, f2, f3, f4)
    x29, y29 = filter_mag("Be", "", f1, f2, f3, f4)
    x30, y30 = filter_mag("STAR", "", f1, f2, f3, f4)
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
            label.append("NGC 2242")
        elif data['id'].startswith("mwc"):
            label.append("MWC 574")
        plot_mag("F480_g_sdss", "F515", "F660", "F625_r_sdss")

#print(A1[0][1], B1[0][1])        
AB = np.vstack([A1[2],B1[2]])
z = gaussian_kde(AB)(AB)
df=pd.DataFrame({'x': np.array(B1[2]), 'y': np.array(A1[2])})

# Sort the points by density, so that the densest points are plotted last
idx = z.argsort()

x, y, z = np.array(A1[2])[idx], np.array(B1[2])[idx], z[idx]

# Canditade find in the JPLUS data

mag=[100.0, 100.0, 22.0102539, 21.7526703, 22.1947689,  21.7716465, 21.549675, 20.6785908,  19.4841557, 21.4224014, 20.7914772, 21.0010147]

colx = mag[8]-mag[7]
coly = mag[5]-mag[6]

#Candidate for symbiotic star in JPLUS data=>
tab = Table.read("EDR-JPLUS/SySts-allcolour_4.tab", format="ascii.tab")

x1 = tab['J0660'] - tab['rSDSS']
y1 = tab['gSDSS'] - tab['J0515']

x2 = tab['gSDSS'] - tab['iSDSS']
y2 = tab['J0410'] - tab['J0660']
#####################################################################
#####################################################################
#Data science verification===>
#error computing by Valera
x_color_g_ha_h4 = []
y_color_g_ha_h4 = []

x_color_g_ha_pg = []
y_color_g_ha_pg = []

# The other color
x_color_j0410_h4 = []
y_color_j0410_h4 = []

x_color_j0410_pg = []
y_color_j0410_pg = []

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
        #colors
        ha_r = j0660 - r
        g_515 = g - j0515
        x_color_g_ha_h4.append(ha_r)
        y_color_g_ha_h4.append(g_515)
        g_i = g - i
        j410_515 = j0410 - j0660
        x_color_j0410_h4.append(g_i)
        y_color_j0410_h4.append(j410_515)
        
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
        ha_r = j0660 - r
        g_515 = g - j0515
        x_color_g_ha_pg.append(ha_r)
        y_color_g_ha_pg.append(g_515)
        g_i = g - i
        j410_515 = j0410 - j0660
        x_color_j0410_pg.append(g_i)
        y_color_j0410_pg.append(j410_515)

#Progation error with Valera's erros
err_Val_h4x= np.sqrt(err_zpVale_h4["e_j0660"]**2+err_zpVale_h4['e_r']**2)
err_Val_h4y= np.sqrt(err_zpVale_h4["e_g"]**2+err_zpVale_h4["e_j0515"]**2)
err_Val_pn135x= np.sqrt(err_zpVale_pn135["e_j0660"]**2+err_zpVale_pn135['e_r']**2)
err_Val_pn135y= np.sqrt(err_zpVale_pn135["e_g"]**2+err_zpVale_pn135["e_j0515"]**2)

err_Val_h4x_o= np.sqrt(err_zpVale_h4["e_g"]**2+err_zpVale_h4['e_i']**2)
err_Val_h4y_o= np.sqrt(err_zpVale_h4["e_j0410"]**2+err_zpVale_h4["e_j0660"]**2)
err_Val_pn135x_o= np.sqrt(err_zpVale_pn135["e_g"]**2+err_zpVale_pn135['e_i']**2)
err_Val_pn135y_o= np.sqrt(err_zpVale_pn135["e_j0410"]**2+err_zpVale_pn135["e_j0660"]**2)

##############################################################################
##############################################################################
#WD from S-PLUS ##############################################################
##############################################################################
##############################################################################
datadir = "WD_ariel/"
fitsfile = "WD_splus_obs.fits"
hdulist= fits.open(os.path.join(datadir, fitsfile))

def WS_splus(filter_1, filter_2, filter_3, filter_4):
    band1 = hdulist[1].data[filter_1]
    band2 = hdulist[1].data[filter_2]
    band3 = hdulist[1].data[filter_3]
    band4 = hdulist[1].data[filter_4]
    return (band1 - band2), (band3 - band4)

#########################################################################################
##############################################################################
##############################################################################
#MS from S-PLUS ##############################################################
##############################################################################
##############################################################################
patternn = "MS-G-spectros/*-JPLUS17-magnitude.json"
file_list1 = glob.glob(patternn)

def filter_mag_MS(e, s, f1, f2, f3, f4):
    '''
    Calculate the colors using any of set of filters
    '''
    col, col0 = [], []
    if data1['id'].endswith(e):
        if data1['id'].startswith(str(s)):
            filter1 = data1[f1]
            filter2 = data1[f2]
            filter3 = data1[f3]
            filter4 = data1[f4]
            diff = filter1 - filter2
            diff0 = filter3 - filter4
            col.append(diff)
            col0.append(diff0)
    
    return col, col0

def plot_mag_MS(f1, f2, f3, f4):
    x, y = filter_mag_MS("", "g", f1, f2, f3, f4)
    x1, y1 = filter_mag_MS("", "k", f1, f2, f3, f4)
    x2, y2 = filter_mag_MS("", "ukg", f1, f2, f3, f4)
    x3, y3 = filter_mag_MS("", "ukk", f1, f2, f3, f4)
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
        plot_mag_MS("F480_g_sdss", "F515", "F660", "F625_r_sdss")

##############################################################################
#Plotting
lgd_kws = {'frameon': True, 'fancybox': True, 'shadow': True}
#sns.set(style="dark", context="talk")
#sns.set_style('ticks')
fig = plt.figure(figsize=(7, 6))
ax1 = fig.add_subplot(111, facecolor ="#eeeeee")
ax1.set_xlim(-2.7,0.8)
ax1.set_ylim(-3.2,1.8)
#ax1.set_xlim(xmin=-2.5,xmax=2.0)
plt.tick_params(axis='x', labelsize=25) 
plt.tick_params(axis='y', labelsize=25)
plt.xlabel(r'$J0660 - r$', fontsize=25)
plt.ylabel(r'$g - J0515$', fontsize=25)
#plt.plot( 'x', 'y', data=df, linestyle='', marker='o')
ax1.scatter(y, x, c=z, s=50, alpha=0.5, edgecolor='')
ax1.scatter(x_color_g_ha_h4, y_color_g_ha_h4, c=sns.xkcd_rgb['yellow'], alpha=0.9, marker='*', s=490, zorder=100.0, edgecolor='black', label='J-PLUS H4-1')
ax1.errorbar(x_color_g_ha_h4, y_color_g_ha_h4, xerr=err_Val_h4x, yerr=err_Val_h4y, marker='.', fmt='k.', elinewidth=1.9, markeredgewidth=1.8, capsize=9)#, elinewidth=1.4, markeredgewidth=1.4, markersize=14,)
ax1.scatter(x_color_g_ha_pg, y_color_g_ha_pg, c=sns.xkcd_rgb['green'], alpha=0.9, marker='*', s=490, zorder=100.0, edgecolor='black', label='J-PLUS PNG 135')
ax1.errorbar(x_color_g_ha_pg, y_color_g_ha_pg, xerr=err_Val_pn135x, yerr=err_Val_pn135y, marker='.', fmt='k.', elinewidth=1.9, markeredgewidth=1.8, capsize=9)#, elinewidth=1.4, markeredgewidth=1.4, markersize=14,)
ax1.scatter(B1[0], A1[0], color= sns.xkcd_rgb["aqua"], s=90, cmap=plt.cm.hot, zorder=10.0, edgecolor='black', label='Obs. hPNe')
(_, caps, _) = ax1.errorbar(B1[0], A1[0], xerr=0.0, yerr=0.0, marker='.', fmt='.', color= sns.xkcd_rgb["aqua"], elinewidth=0.8, markeredgewidth=0.8, markersize=8,)
for cap in caps:
    cap.set_markeredgewidth(1)
#ax1.scatter(B1[19], A1[19], c='y', alpha=0.8, s=40, label='Modeled halo PNe')
ax1.scatter(B1[15], A1[15], color= sns.xkcd_rgb["aqua"], cmap=plt.cm.hot, s=90, zorder=100.0, edgecolor='black')#, label='Obs. halo PNe')
# ax1.errorbar(B1[15], A1[15], yerr=0.3,  uplims= True,  marker='.', fmt='k.', elinewidth=.8, markeredgewidth=.8, markersize=8,)
# ax1.errorbar(B1[15], A1[15], xerr=0.2,  xuplims= True,  marker='.', fmt='k.', elinewidth=.8, markeredgewidth=.8, markersize=8,)

ax1.scatter(B1[16], A1[16], color= sns.xkcd_rgb["aqua"], cmap=plt.cm.hot, edgecolor='black', s=90)
(_, caps, _) = ax1.errorbar(B1[16], A1[16], xerr=0.0, yerr=0.0, marker='.', fmt='.', color= sns.xkcd_rgb["aqua"], elinewidth=0.8, markeredgewidth=0.8, markersize=8, zorder=3.0)
for cap in caps:
    cap.set_markeredgewidth(1)
ax1.scatter(B1[17], A1[17], color= sns.xkcd_rgb["aqua"], s=90, edgecolor='black', cmap=plt.cm.hot)
(_, caps, _) = ax1.errorbar(B1[17], A1[17], xerr=0.0, yerr=0.0, marker='.', fmt='.', color= sns.xkcd_rgb["aqua"], elinewidth=0.8, markeredgewidth=0.8, markersize=8, zorder=3.0)
for cap in caps:
    cap.set_markeredgewidth(1)

ax1.scatter(B1[1], A1[1], c=sns.xkcd_rgb['pale yellow'], alpha=0.9, s=40, cmap=plt.cm.hot, edgecolor='black', zorder=10.0, label='SDSS CVs')
ax1.scatter(B1[4], A1[4],  c= "mediumaquamarine" , alpha=0.6, s=40, marker='D', cmap=plt.cm.hot, edgecolor='black', label='SDSS QSOs') #label='SDSS QSOs (1.3<z<1.4)')
ax1.scatter(B1[5], A1[5],  c= "mediumaquamarine", alpha=0.6, s=40, cmap=plt.cm.hot, marker='D', edgecolor='black')#,  label='SDSS QSOs (2.4<z<2.6)')
ax1.scatter(B1[6], A1[6],  c= "mediumaquamarine", alpha=0.6, s=40, marker='D', cmap=plt.cm.hot, edgecolor='black')#,  label='SDSS QSOs (3.2<z<3.4)')
ax1.scatter(B1[7], A1[7],  c= "goldenrod", alpha=0.5, s=60, marker='^', cmap=plt.cm.hot, zorder=11, edgecolor='black', label='SDSS SFGs ')
ax1.scatter(B1[8], A1[8],  c= "red", alpha=0.6, s=40, marker='s', cmap=plt.cm.hot, edgecolor='black', zorder=150.0, label='Obs. SySt ')
#ax1.scatter(B1[72], A1[72],  c= "red", alpha=0.8, marker='D', label='Symbiotics in NGC 55')
ax1.scatter(B1[12], A1[12],  c= "red", alpha=0.6, s=40, marker='s', cmap=plt.cm.hot, edgecolor='black', zorder=150)#, label='Obs. SySt in NGC 205')
ax1.scatter(B1[9], A1[9],  c= "red", alpha=0.6, s=60, marker='^', cmap=plt.cm.hot, edgecolor='black', zorder=150.0, label='IPHAS SySt')
ax1.scatter(B1[14], A1[14], c= "red" , alpha=0.6, s=40, marker='s', cmap=plt.cm.hot, edgecolor='black', zorder=150.0)#, label='Obs. SySt in IC10 ')
ax1.scatter(B1[13], A1[13],  c= "red", alpha=0.6, s=40, marker='s', cmap=plt.cm.hot, edgecolor='black', zorder=150.0)#, label='Obs. SySt in NGC 185')
#ax1.scatter(B1[73], A1[73],  c= "red", alpha=0.8, marker='o', label='C. Buil Symbiotics')
ax1.scatter(B1[10], A1[10],  c= "gray", alpha=0.6, marker='D', s=40, cmap=plt.cm.hot, edgecolor='black', zorder=10, label='Obs. H II region in NGC 55')
ax1.scatter(B1[18], A1[18],  c= "lightsalmon", alpha=0.8, s=100, marker='*', cmap=plt.cm.hot, edgecolor='black', label='Obs. YSOs')
ax1.scatter(B1[19], A1[19],  c=sns.xkcd_rgb['ultramarine blue'], alpha=0.8, s=100, cmap=plt.cm.hot, marker='*',  edgecolor='black', zorder=110, label='Obs. B[e] stars')

redde_vector(-2.147731023789999, -1.4932436830902718, -2.1826566358487645, -1.2892862958299025, 0.6, -0.8, 0, -0.1) #E=0.7

left, bottom, width, height = [0.62, 0.22, 0.23, 0.23]
ax11 = fig.add_axes([left, bottom, width, height])
ax11.set_xlim(-2.7,0.8)
ax11.set_ylim(-3.2,1.8)
ax11.scatter(B1[20], A1[20],  c=sns.xkcd_rgb['neon purple'], alpha=0.3, s=20, cmap=plt.cm.hot, marker='*', zorder=110, label='Normal stars')
ax11.scatter(BB1, AA1,  c=sns.xkcd_rgb['brown'], s=20, cmap=plt.cm.hot, marker='*', zorder=110, label='Giant stars')
g_f515, f600_r = WS_splus("g_aper", "F515_aper", "F660_aper", "r_aper")
ax11.scatter(f600_r, g_f515, c=sns.xkcd_rgb['mint green'], alpha=0.8, s=20, cmap=plt.cm.hot, marker='*', zorder=105, label='WDs from S-PLUS')

# ax31.text(0.1, 0.8, 'hPNe',
#          transform=ax31.transAxes, fontsize=14)
ax11.spines['top'].set_visible(False)
ax11.spines['right'].set_visible(False)

# for label_, x, y in zip(label, B1[0], A1[0]):
#     ax1.annotate(label_, (x, y), alpha=5, size=8,
#                    xytext=(-4.0, -10.0), textcoords='offset points', ha='right', va='bottom',)
###################################################################
bbox_props = dict(boxstyle="round", fc="w", ec="0.78", alpha=0.6, pad=0.1)
# t = ax.text(0, 0, "Direction", ha="center", va="center", rotation=45,
#             size=15,
#             bbox=bbox_props)

ax1.annotate("H4-1", (np.array(B1[15]), np.array(A1[15])), alpha=15, size=10.0,
                   xytext=(24, -18), textcoords='offset points', ha='right', va='bottom', bbox=bbox_props,)
ax1.annotate("PNG 135.9+55.9", (np.array(B1[16]), np.array(A1[16])), alpha=15, size=10.0,
                   xytext=(32, -16.0), textcoords='offset points', ha='right', va='bottom', zorder=150, bbox=bbox_props,)
ax1.annotate("MWC 574", (np.array(B1[0][2]), np.array(A1[0][2])), alpha=15, size=10.0,
                   xytext=(46, 5.0), textcoords='offset points', ha='right', va='bottom', bbox=bbox_props, zorder=200.0,)
# ax1.annotate("DdDm-1", (np.array(B1[17]), np.array(A1[17])), alpha=10, size=8,
#                    xytext=(35, -10), textcoords='offset points', ha='right', va='bottom',)
##################################################################

# Region where are located the PNe
result = findIntersection(0.12, -0.01, -1.1, -1.07, 0.0)
result_y = 0.12*result - 0.01

x_new = np.linspace(-15.5, result,  200)
x_new2 = np.linspace(result, 10.0, 200)
x_new3 = np.linspace(-10.0, 1.1, 200)
y = 0.12*x_new - 0.01
yy = -1.1*x_new2 - 1.07
#Mask
#mask = y >= result_y - 0.5
ax1.plot(x_new, y, color='k', zorder=100, linestyle='-')
ax1.plot(x_new2, yy , color='k', zorder=100, linestyle='-')

ax11.plot(x_new, y, color='k', zorder=100, linestyle='-')
ax11.plot(x_new2, yy , color='k', zorder=100, linestyle='-')

# Region of the simbiotic stars
result1 = findIntersection(-0.19, -0.09, -2.9, -2.2, 0.0)
x_new_s = np.linspace(-15.5, result1, 200)
x_new2_s = np.linspace(-15.0, result1, 200)
y_s = -0.19*x_new_s - 0.09
yy_s = -2.9*x_new2_s - 2.2

#vectro reddening
#redde_vector(-2.14773102379, -1.49324368309, -2.16099869712, -1.43243126278, 1.3, -0.8, 0, -0.1) #E=0.2

# ax1.plot(x_new_s, y_s, color='r', zorder=100, linestyle='--')
# ax1.plot(x_new2_s, yy_s , color='r', zorder=100, linestyle='--')

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
#ax1.legend(scatterpoints=1, ncol=2, fontsize=10.0, loc='lower right', **lgd_kws)
#ax1.grid()
#lgd = ax1.legend(loc='center right', bbox_to_anchor=(1.27, 0.5), fontsize=7.5, **lgd_kws)
#ax1.grid(which='minor', lw=0.5)
#sns.despine(bottom=True)
plt.tight_layout()
# plt.text(0.05, 0.03, 'CLOUDY modelled halo PNe',
#          transform=ax1.transAxes, fontsize='small')
#plt.savefig('luis-JPLUS-Viironen.pdf')#,  bbox_extra_artists=(lgd,), bbox_inches='tight')
pltfile = 'Fig5-JPLUS17-J0660-r.pdf'
save_path = '../Dropbox/JPAS/paper-phot/Fig/'
file_save = os.path.join(save_path, pltfile)
plt.savefig(file_save)
#plt.savefig('Fig5-JPLUS17-J0660-r.pdf')
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
        plot_mag("F410", "F660", "F480_g_sdss", "F766_i_sdss") #F480_g_sdss

########################################################################
AA1, BB1 = [], []

for file_name1 in file_list1:
    with open(file_name1) as f1:
        data1 = json.load(f1)
        plot_mag_MS("F410", "F660", "F480_g_sdss", "F766_i_sdss")
##########################################################################

AB = np.vstack([A1[2],B1[2]])
z = gaussian_kde(AB)(AB)
df=pd.DataFrame({'x': np.array(B1[2]), 'y': np.array(A1[2]) })

# Sort the points by density, so that the densest points are plotted last
idx = z.argsort()
x, y, z = np.array(A1[2])[idx], np.array(B1[2])[idx], z[idx]

# Canditade find in the JPLUS data

colx2 = mag[5]-mag[9]
coly2 = mag[3]-mag[8]

lgd_kws = {'frameon': True, 'fancybox': True, 'shadow': True}
#sns.set(style="dark", context="talk")
#sns.set_style('ticks')
fig = plt.figure(figsize=(7, 6))
ax2 = fig.add_subplot(111, facecolor ="#eeeeee")
ax2.set_xlim(-3.0,5.0)
ax2.set_ylim(-2.0,6.0)

#ax2.set_xlim(xmin=-2.5,xmax=2.0)
plt.tick_params(axis='x', labelsize=25) 
plt.tick_params(axis='y', labelsize=25)
plt.xlabel(r'$g - i$', fontsize= 25)
plt.ylabel(r'$J0410 - J0660$', fontsize= 25)
#plt.plot( 'x', 'y', data=df, linestyle='', marker='o')
ax2.scatter(y, x, c=z, s=50, alpha=0.5, edgecolor='')
ax2.scatter(x_color_j0410_h4, y_color_j0410_h4,  c=sns.xkcd_rgb['yellow'], alpha=1.0, marker='*', s=490, zorder=100.0, edgecolor='black', label='J-PLUS H4-1')
ax2.errorbar(x_color_j0410_h4, y_color_j0410_h4, xerr=err_Val_h4x_o, yerr=err_Val_h4y_o, marker='.', fmt='k.', elinewidth=1.9, markeredgewidth=1.8, capsize=9)#, elinewidth=1.4, markeredgewidth=1.4, markersize=14,)
ax2.scatter(x_color_j0410_pg, y_color_j0410_pg,  c= sns.xkcd_rgb['green'], alpha=1.0, marker='*', s=490, zorder=100.0, edgecolor='black', label='J-PLUS PNG 135')
ax2.errorbar(x_color_j0410_pg, y_color_j0410_pg, xerr=err_Val_pn135x_o, yerr=err_Val_pn135y_o, marker='.', fmt='k.', elinewidth=1.9, markeredgewidth=1.8, capsize=9)
ax2.scatter(B1[0], A1[0], color= sns.xkcd_rgb["aqua"], s=90, cmap=plt.cm.hot, edgecolor='black', zorder=150, label='Obs. hPNe')
(_, caps, _) = ax2.errorbar(B1[0], A1[0], xerr=0.0, yerr=0.0, marker='.', fmt='.', color= sns.xkcd_rgb["aqua"], elinewidth=0.8, markeredgewidth=0.8, markersize=8,)
for cap in caps:
    cap.set_markeredgewidth(1)
#ax2.scatter(B1[19], A1[19], c='y', alpha=0.8, s=40, label='Modeled halo PNe')
ax2.scatter(B1[15], A1[15], color= sns.xkcd_rgb["aqua"], cmap=plt.cm.hot, edgecolor='black', s=90, zorder=150)#, label='Obs. halo PNe')
# ax2.errorbar(B1[15], A1[15], yerr=0.3,  lolims= True,  marker='.', fmt='k.', elinewidth=.8, markeredgewidth=.8, markersize=8,)
# ax2.errorbar(B1[15], A1[15], xerr=0.2,  xuplims= True,  marker='.', fmt='k.', elinewidth=.8, markeredgewidth=.8, markersize=8,)

ax2.scatter(B1[16], A1[16], color= sns.xkcd_rgb["aqua"], cmap=plt.cm.hot, s=90, edgecolor='black')
(_, caps, _) = ax2.errorbar(B1[16], A1[16], xerr=0.0, yerr=0.0, marker='.', fmt='.', color= sns.xkcd_rgb["aqua"], elinewidth=0.8, markeredgewidth=0.8, markersize=8,)
for cap in caps:
    cap.set_markeredgewidth(1)
ax2.scatter(B1[17], A1[17], color= sns.xkcd_rgb["aqua"], s=90, cmap=plt.cm.hot, edgecolor='black')
(_, caps, _) = ax2.errorbar(B1[17], A1[17], xerr=0.0, yerr=0.0, marker='.', fmt='.', color= sns.xkcd_rgb["aqua"], elinewidth=0.8, markeredgewidth=0.8, markersize=8,)
for cap in caps:
    cap.set_markeredgewidth(1)

ax2.scatter(B1[1], A1[1], c=sns.xkcd_rgb['pale yellow'], alpha=0.8, s=40, cmap=plt.cm.hot, edgecolor='black', zorder=10.0, label='SDSS CVs')
ax2.scatter(B1[4], A1[4],  c= "mediumaquamarine" , alpha=0.6, s=40, marker='D', cmap=plt.cm.hot, edgecolor='black', label='SDSS QSOs') #label='SDSS QSOs (1.3<z<1.4)')
ax2.scatter(B1[5], A1[5],  c= "mediumaquamarine", alpha=0.6, s=40, cmap=plt.cm.hot, marker='D', edgecolor='black')#,  label='SDSS QSOs (2.4<z<2.6)')
ax2.scatter(B1[6], A1[6],  c= "mediumaquamarine", alpha=0.6, s=40, marker='D', cmap=plt.cm.hot, edgecolor='black')#,  label='SDSS QSOs (3.2<z<3.4)')
ax2.scatter(B1[7], A1[7],  c= "goldenrod", alpha=0.5, s=60, marker='^', zorder=11., cmap=plt.cm.hot, edgecolor='black', label='SDSS SFGs ')
ax2.scatter(B1[8], A1[8],  c= "red", alpha=0.6, s=40, marker='s', cmap=plt.cm.hot, edgecolor='black', zorder=150.0, label='Obs. SySt ')
#ax2.scatter(B1[72], A1[72],  c= "red", alpha=0.8, marker='D', label='Symbiotics in NGC 55')
ax2.scatter(B1[12], A1[12],  c= "red", alpha=0.6, s=40, marker='s', cmap=plt.cm.hot, edgecolor='black', zorder=150.0)#, label='Obs. SySt in NGC 205')
ax2.scatter(B1[9], A1[9],  c= "red", alpha=0.6, s=60, marker='^', cmap=plt.cm.hot, edgecolor='black', zorder=150.0, label='IPHAS SySt')
ax2.scatter(B1[14], A1[14], c= "red" , alpha=0.6, s=40, marker='s', cmap=plt.cm.hot, edgecolor='black', zorder=150.0)#, label='Obs. SySt in IC10 ')
ax2.scatter(B1[13], A1[13],  c= "red", alpha=0.6, s=40, marker='s', cmap=plt.cm.hot, edgecolor='black', zorder=150.0)#, label='Obs. SySt in NGC 185')
#ax2.scatter(B1[73], A1[73],  c= "red", alpha=0.8, marker='o', label='C. Buil Symbiotics')
ax2.scatter(B1[10], A1[10],  c= "gray", alpha=0.6, marker='D', s=40, zorder=10., cmap=plt.cm.hot, edgecolor='black', label='Obs. HII region in NGC 55')
ax2.scatter(B1[18], A1[18],  c= "lightsalmon", alpha=0.8, s=100, marker='*', cmap=plt.cm.hot, edgecolor='black', label='Obs. YSOs')
ax2.scatter(B1[19], A1[19],  c=sns.xkcd_rgb['ultramarine blue'], alpha=0.8, s=90, cmap=plt.cm.hot, marker='*',  edgecolor='black', zorder=110, label='Obs. B[e] stars')

redde_vector(-1.2914206511782904, 3.0366337467574147, -0.026443021183738615, 4.44284915692785, -1.4 , 1.2, -0.2, -0.2) #Ev=0.7

left, bottom, width, height = [0.7, 0.23, 0.23, 0.23]
ax21 = fig.add_axes([left, bottom, width, height])
ax21.set_xlim(-3.0,5.0)
ax21.set_ylim(-2.0,6.0)
ax21.scatter(B1[20], A1[20],  c=sns.xkcd_rgb['neon purple'], alpha=0.3, s=20, cmap=plt.cm.hot, marker='*', zorder=110, label='Normal stars')
ax21.scatter(BB1, AA1,  c=sns.xkcd_rgb['brown'], s=20, cmap=plt.cm.hot, marker='*', zorder=110, label='Giant stars')
f410_f660, g_i = WS_splus("F410_aper", "F660_aper", "g_aper", "i_aper")
ax21.scatter(g_i, f410_f660, c=sns.xkcd_rgb['mint green'], alpha=0.8, s=20, cmap=plt.cm.hot, marker='*', zorder=105, label='WDs from S-PLUS')

ax21.spines['top'].set_visible(False)
ax21.spines['right'].set_visible(False)

# ax31.text(0.1, 0.8, 'hPNe',
#          transform=ax31.transAxes, fontsize=14)
ax21.spines['top'].set_visible(False)
ax21.spines['right'].set_visible(False)

# for label_, x, y in zip(label, B1[0], A1[0]):
#     ax2.annotate(label_, (x, y), alpha=5, size=8,
#                    xytext=(-4.0, -3.6), textcoords='offset points', ha='right', va='bottom',)
###################################################################
ax2.annotate("H4-1", (np.array(B1[15]), np.array(A1[15])), alpha=15, size=10.0,
                   xytext=(25, 10), textcoords='offset points', ha='right', va='bottom', bbox=bbox_props,)
ax2.annotate("PNG 135.9+55.9", (np.array(B1[16]), np.array(A1[16])), alpha=15, size=10.0,
                   xytext=(-5, -10), textcoords='offset points', ha='right', va='bottom', bbox=bbox_props,)
# ax2.annotate("DdDm-1", (np.array(B1[17]), np.array(A1[17])), alpha=10, size=8,
#                    xytext=(-6.0, -8), textcoords='offset points', ha='right', va='bottom',)
##################################################################
#Obersevado porJPLUS
#for label_, x, y in zip(label1, d_768_jplus[0], d_644_jplus[0]):
# ax2.annotate("H4-1", (d_768_jplus[0], d_644_jplus[0]), alpha=8, size=8,
#                    xytext=(-5, 3), textcoords='offset points', ha='right', va='bottom', color='blue',)

# ax2.annotate("PNG 135.9+55.9", (d_768_jplus[1], d_644_jplus[1]), alpha=8, size=8,
#                    xytext=(68, -10), textcoords='offset points', ha='right', va='bottom', color='green',)

# Region where are located the PNe
result = findIntersection(8.0, 4.50, 0.8, 0.55, 0.0)
result_y = 8.0*result + 4.50

x_new = np.linspace(result, 15.5, 200)
x_new2 = np.linspace(-10.0, result, 200)
x_new3 = np.linspace(-10.0, 1.1, 200)
#y =  3.0*x_new + 2.50  #8.0 4.50
y =  8.0*x_new + 4.50
yy = 0.8*x_new2 + 0.55
#Mask
#mask = y >= result_y - 0.5
ax2.plot(x_new, y, color='k', zorder=100, linestyle='-')
ax2.plot(x_new2, yy , color='k', zorder=100, linestyle='-')
ax21.plot(x_new, y, color='k', zorder=100, linestyle='-')
ax21.plot(x_new2, yy , color='k', zorder=100, linestyle='-')

# Region of the simbiotic stars
result1 = findIntersection(-5.2, +10.60, 1.9, -1.43, 0.0)
x_new_s = np.linspace(-15.5, result1, 200)
x_new2_s = np.linspace(result1, 15.5, 200)
y_s = -5.2*x_new_s + 10.60
yy_s = 1.9*x_new2_s - 1.43

# ax2.plot(x_new_s, y_s, color='r', zorder=100, linestyle='--')
# ax2.plot(x_new2_s, yy_s , color='r', zorder=100, linestyle='--')

#reddening vector
#redde_vector(-1.29142065118, 3.03663374676, -0.927973092134, 3.4420227057, 4. , -3.7, -0.2, -0.2) #Ev=0.2

ax2.minorticks_on()
#ax2.grid(which='minor')#, lw=0.3)
#ax2.legend(scatterpoints=1, ncol=1, fontsize=8.0, loc='lower right', **lgd_kws)
#ax2.grid()
#lgd = ax2.legend(loc='center right', bbox_to_anchor=(1.27, 0.5), fontsize=7.5, **lgd_kws)
#ax2.grid(which='minor', lw=0.5)
#sns.despine(bottom=True)
plt.tight_layout()
# plt.text(0.1, 0.85, 'CLOUDY modelled halo PNe',
#          transform=ax2.transAxes, fontsize='large')
#plt.savefig('luis-JPLUS-Viironen.pdf')#,  bbox_extra_artists=(lgd,), bbox_inches='tight')
pltfile = 'Fig6-JPLUS17-g-i.pdf'
file_save = os.path.join(save_path, pltfile)
plt.savefig(file_save)
#plt.savefig('Fig6-JPLUS17-g-i.pdf')
plt.clf()

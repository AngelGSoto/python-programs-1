from __future__ import print_function
import glob

from astropy.io import fits
import os
import json
import numpy as np
import argparse
#import matplotlib
#matplotlib.use("Agg")
import matplotlib.pyplot as plt
import sys, getopt
from collections import OrderedDict
import seaborn as sns
from scipy.optimize import fsolve
from itertools import chain
from collections import defaultdict

def findIntersection(m, y, m1, y1, x0):
    x = np.linspace(-10.0, 15.5, 200)
    return fsolve(lambda x : (m*x + y) - (m1*x + y1), x0)



rSDSS = "*-catalog/*-v1_rSDSS_dual.catalog"
file_list_r = glob.glob(rSDSS)

nsourse0 = 13248
nsourse1 = 22501
nsourse2 = 17412
nsourse3 = 17562

hdu_dt0 = {'rSDSS': np.empty((nsourse0,)), 'err_rSDSS': np.empty((nsourse0,)),
           'iSDSS': np.empty((nsourse0,)), 'err_iSDSS': np.empty((nsourse0,)),
           'J0660': np.empty((nsourse0,)), 'err_J0660': np.empty((nsourse0,)),
           'J0420': np.empty((nsourse0,)), 'err_J0420': np.empty((nsourse0,)),
           'J0840': np.empty((nsourse0,)), 'err_J0840': np.empty((nsourse0,)),
           'J0500': np.empty((nsourse0,)), 'err_J0500': np.empty((nsourse0,))}

hdu_dt1 = {'rSDSS': np.empty((nsourse1,)), 'err_rSDSS': np.empty((nsourse1,)),
           'iSDSS': np.empty((nsourse1,)), 'err_iSDSS': np.empty((nsourse1,)),
           'J0660': np.empty((nsourse1,)), 'err_J0660': np.empty((nsourse1,)),
           'J0420': np.empty((nsourse1,)), 'err_J0420': np.empty((nsourse1,)),
           'J0840': np.empty((nsourse1,)), 'err_J0840': np.empty((nsourse1,)),
           'J0500': np.empty((nsourse1,)), 'err_J0500': np.empty((nsourse1,))}

hdu_dt2 = {'rSDSS': np.empty((nsourse2,)), 'err_rSDSS': np.empty((nsourse2,)),
           'iSDSS': np.empty((nsourse2,)), 'err_iSDSS': np.empty((nsourse2,)),
           'J0660': np.empty((nsourse2,)), 'err_J0660': np.empty((nsourse2,)),
           'J0420': np.empty((nsourse2,)), 'err_J0420': np.empty((nsourse2,)),
           'J0840': np.empty((nsourse2,)), 'err_J0840': np.empty((nsourse2,)),
           'J0500': np.empty((nsourse2,)), 'err_J0500': np.empty((nsourse2,))}

hdu_dt3 = {'rSDSS': np.empty((nsourse3,)), 'err_rSDSS': np.empty((nsourse3,)),
           'iSDSS': np.empty((nsourse3,)), 'err_iSDSS': np.empty((nsourse3,)),
           'J0660': np.empty((nsourse3,)), 'err_J0660': np.empty((nsourse3,)),
           'J0420': np.empty((nsourse3,)), 'err_J0420': np.empty((nsourse3,)),
           'J0840': np.empty((nsourse3,)), 'err_J0840': np.empty((nsourse3,)),
           'J0500': np.empty((nsourse3,)), 'err_J0500': np.empty((nsourse3,))}

for file_name_r in file_list_r:
    r_hdu = fits.open(file_name_r)
    #array_r_hdu = r_hdu[2].data["MAG_AUTO"].reshape(len(r_hdu[2].data["MAG_AUTO"]), 1)
    #print(len(array_r_hdu))
    if len(r_hdu[2].data["MAG_AUTO"]) == 13248:
        for i in range(len(r_hdu[2].data["MAG_AUTO"])):
            hdu_dt0['rSDSS'][i] = np.array(r_hdu[2].data["MAG_AUTO"][i])
            hdu_dt0['err_rSDSS'][i] = np.array(r_hdu[2].data["MAGERR_AUTO"][i])
    elif len(r_hdu[2].data["MAG_AUTO"]) == 22501:
        for i in range(len(r_hdu[2].data["MAG_AUTO"])):
            hdu_dt1['rSDSS'][i] = np.array(r_hdu[2].data["MAG_AUTO"][i])
            hdu_dt1['err_rSDSS'][i] = np.array(r_hdu[2].data["MAGERR_AUTO"][i])
    elif len(r_hdu[2].data["MAG_AUTO"]) == 17412:
        for i in range(len(r_hdu[2].data["MAG_AUTO"])):
            hdu_dt2['rSDSS'][i] = np.array(r_hdu[2].data["MAG_AUTO"][i])
            hdu_dt2['err_rSDSS'][i] = np.array(r_hdu[2].data["MAGERR_AUTO"][i])
    else:
        for i in range(len(r_hdu[2].data["MAG_AUTO"])):
            hdu_dt3['rSDSS'][i] = np.array(r_hdu[2].data["MAG_AUTO"][i])
            hdu_dt3['err_rSDSS'][i] = np.array(r_hdu[2].data["MAGERR_AUTO"][i])

iSDSS = "*-catalog/*-v1_iSDSS_dual.catalog"
file_list_i = glob.glob(iSDSS)
for file_name_i in file_list_i:
    i_hdu = fits.open(file_name_i)
    if len(i_hdu[2].data["MAG_AUTO"]) == 13248:
        for i in range(len(i_hdu[2].data["MAG_AUTO"])):
            hdu_dt0['iSDSS'][i] = np.array(i_hdu[2].data["MAG_AUTO"][i])
            hdu_dt0['err_iSDSS'][i] = np.array(i_hdu[2].data["MAGERR_AUTO"][i])
    elif len(i_hdu[2].data["MAG_AUTO"]) == 22501:
        for i in range(len(i_hdu[2].data["MAG_AUTO"])):
            hdu_dt1['iSDSS'][i] = np.array(i_hdu[2].data["MAG_AUTO"][i])
            hdu_dt1['err_iSDSS'][i] = np.array(i_hdu[2].data["MAGERR_AUTO"][i])
    elif len(i_hdu[2].data["MAG_AUTO"]) == 17412:
        for i in range(len(i_hdu[2].data["MAG_AUTO"])):
            hdu_dt2['iSDSS'][i] = np.array(i_hdu[2].data["MAG_AUTO"][i])
            hdu_dt2['err_iSDSS'][i] = np.array(i_hdu[2].data["MAGERR_AUTO"][i])
    else:
        for i in range(len(i_hdu[2].data["MAG_AUTO"])):
            hdu_dt3['iSDSS'][i] = np.array(i_hdu[2].data["MAG_AUTO"][i])
            hdu_dt3['err_iSDSS'][i] = np.array(i_hdu[2].data["MAGERR_AUTO"][i])
    
J0660 = "*-catalog/*-v1_J0660_dual.catalog"
file_list_J0660 = glob.glob(J0660)
for file_name_J0660 in file_list_J0660:
    J0660_hdu = fits.open(file_name_J0660)
    if len(J0660_hdu[2].data["MAG_AUTO"]) == 13248:
        for i in range(len(J0660_hdu[2].data["MAG_AUTO"])):
            hdu_dt0['J0660'][i] = np.array(J0660_hdu[2].data["MAG_AUTO"][i])
            hdu_dt0['err_J0660'][i] = np.array(J0660_hdu[2].data["MAGERR_AUTO"][i])
    elif len(J0660_hdu[2].data["MAG_AUTO"]) == 22501:
        for i in range(len(J0660_hdu[2].data["MAG_AUTO"])):
            hdu_dt1['J0660'][i] = np.array(J0660_hdu[2].data["MAG_AUTO"][i])
            hdu_dt1['err_J0660'][i] = np.array(J0660_hdu[2].data["MAGERR_AUTO"][i])
    elif len(J0660_hdu[2].data["MAG_AUTO"]) == 17412:
        for i in range(len(J0660_hdu[2].data["MAG_AUTO"])):
            hdu_dt2['J0660'][i] = np.array(J0660_hdu[2].data["MAG_AUTO"][i])
            hdu_dt2['err_J0660'][i] = np.array(J0660_hdu[2].data["MAGERR_AUTO"][i])
    else:
        for i in range(len(J0660_hdu[2].data["MAG_AUTO"])):
            hdu_dt3['J0660'][i] = np.array(J0660_hdu[2].data["MAG_AUTO"][i])
            hdu_dt3['err_J0660'][i] = np.array(J0660_hdu[2].data["MAGERR_AUTO"][i])

##################################################################
# To construct other color
##################################################################
J0420 = "*-catalog/*-v1_J0420_dual.catalog"
file_list_J0420 = glob.glob(J0420)
for file_name_J0420 in file_list_J0420:
    J0420_hdu = fits.open(file_name_J0420)
    if len(J0420_hdu[2].data["MAG_AUTO"]) == 13248:
        for i in range(len(J0420_hdu[2].data["MAG_AUTO"])):
            hdu_dt0['J0420'][i] = np.array(J0420_hdu[2].data["MAG_AUTO"][i])
            hdu_dt0['err_J0420'][i] = np.array(J0420_hdu[2].data["MAGERR_AUTO"][i])
    elif len(J0420_hdu[2].data["MAG_AUTO"]) == 22501:
        for i in range(len(J0420_hdu[2].data["MAG_AUTO"])):
            hdu_dt1['J0420'][i] = np.array(J0420_hdu[2].data["MAG_AUTO"][i])
            hdu_dt1['err_J0420'][i] = np.array(J0420_hdu[2].data["MAGERR_AUTO"][i])
    elif len(J0420_hdu[2].data["MAG_AUTO"]) == 17412:
        for i in range(len(J0420_hdu[2].data["MAG_AUTO"])):
            hdu_dt2['J0420'][i] = np.array(J0420_hdu[2].data["MAG_AUTO"][i])
            hdu_dt2['err_J0420'][i] = np.array(J0420_hdu[2].data["MAGERR_AUTO"][i])
    else:
        for i in range(len(J0420_hdu[2].data["MAG_AUTO"])):
            hdu_dt3['J0420'][i] = np.array(J0420_hdu[2].data["MAG_AUTO"][i])
            hdu_dt3['err_J0420'][i] = np.array(J0420_hdu[2].data["MAGERR_AUTO"][i])

J0840 = "*-catalog/*-v1_J0840_dual.catalog"
file_list_J0840 = glob.glob(J0840)
for file_name_J0840 in file_list_J0840:
    J0840_hdu = fits.open(file_name_J0840)
    if len(J0840_hdu[2].data["MAG_AUTO"]) == 13248:
        for i in range(len(J0840_hdu[2].data["MAG_AUTO"])):
            hdu_dt0['J0840'][i] = np.array(J0840_hdu[2].data["MAG_AUTO"][i])
            hdu_dt0['err_J0840'][i] = np.array(J0840_hdu[2].data["MAGERR_AUTO"][i])
    elif len(J0840_hdu[2].data["MAG_AUTO"]) == 22501:
        for i in range(len(J0840_hdu[2].data["MAG_AUTO"])):
            hdu_dt1['J0840'][i] = np.array(J0840_hdu[2].data["MAG_AUTO"][i])
            hdu_dt1['err_J0840'][i] = np.array(J0840_hdu[2].data["MAGERR_AUTO"][i])
    elif len(J0840_hdu[2].data["MAG_AUTO"]) == 17412:
        for i in range(len(J0840_hdu[2].data["MAG_AUTO"])):
            hdu_dt2['J0840'][i] = np.array(J0840_hdu[2].data["MAG_AUTO"][i])
            hdu_dt2['err_J0840'][i] = np.array(J0840_hdu[2].data["MAGERR_AUTO"][i])
    else:
        for i in range(len(J0840_hdu[2].data["MAG_AUTO"])):
            hdu_dt3['J0840'][i] = np.array(J0840_hdu[2].data["MAG_AUTO"][i])
            hdu_dt3['err_J0840'][i] = np.array(J0840_hdu[2].data["MAGERR_AUTO"][i])

J0500 = "*-catalog/*-v1_J0500_dual.catalog"
file_list_J0500 = glob.glob(J0500)
for file_name_J0500 in file_list_J0500:
    J0500_hdu = fits.open(file_name_J0500)
    if len(J0500_hdu[2].data["MAG_AUTO"]) == 13248:
        for i in range(len(J0500_hdu[2].data["MAG_AUTO"])):
            hdu_dt0['J0500'][i] = np.array(J0500_hdu[2].data["MAG_AUTO"][i])
            hdu_dt0['err_J0500'][i] = np.array(J0500_hdu[2].data["MAGERR_AUTO"][i])
    elif len(J0500_hdu[2].data["MAG_AUTO"]) == 22501:
        for i in range(len(J0500_hdu[2].data["MAG_AUTO"])):
            hdu_dt1['J0500'][i] = np.array(J0500_hdu[2].data["MAG_AUTO"][i])
            hdu_dt1['err_J0500'][i] = np.array(J0500_hdu[2].data["MAGERR_AUTO"][i])
    elif len(J0500_hdu[2].data["MAG_AUTO"]) == 17412:
        for i in range(len(J0500_hdu[2].data["MAG_AUTO"])):
            hdu_dt2['J0500'][i] = np.array(J0500_hdu[2].data["MAG_AUTO"][i])
            hdu_dt2['err_J0500'][i] = np.array(J0500_hdu[2].data["MAGERR_AUTO"][i])
    else:
        for i in range(len(J0500_hdu[2].data["MAG_AUTO"])):
            hdu_dt3['J0500'][i] = np.array(J0500_hdu[2].data["MAG_AUTO"][i])
            hdu_dt3['err_J0500'][i] = np.array(J0500_hdu[2].data["MAGERR_AUTO"][i])

print(len(hdu_dt1['rSDSS']))
# hdu_dt = {}
# hdu_dt.update(hdu_dt0)
# hdu_dt.update(hdu_dt1)
# hdu_dt.update(hdu_dt2)
# print(len(hdu_dt['rSDSS']))
#sys.exit()
# Mask
q0 = hdu_dt0["rSDSS"] <= 20.0
q1 = hdu_dt1["rSDSS"] <= 20.0
q2 = hdu_dt2["rSDSS"] <= 20.0
q3 = hdu_dt3["rSDSS"] <= 20.0

# Mask error
e_r0 = hdu_dt0["err_rSDSS"] <= 0.2
e_i0 = hdu_dt0["err_iSDSS"] <= 0.2
e_J06600 = hdu_dt0["err_J0660"] <= 0.2
e_J04200 = hdu_dt0['err_J0420'] <= 0.2
e_J08400 = hdu_dt0['err_J0840'] <= 0.2

e_r1 = hdu_dt1["err_rSDSS"] <= 0.2
e_i1 = hdu_dt1["err_iSDSS"] <= 0.2
e_J06601 = hdu_dt1["err_J0660"] <= 0.2
e_J04201 = hdu_dt1['err_J0420'] <= 0.2
e_J08401 = hdu_dt1['err_J0840'] <= 0.2

e_r2 = hdu_dt2["err_rSDSS"] <= 0.2
e_i2 = hdu_dt2["err_iSDSS"] <= 0.2
e_J06602 = hdu_dt2["err_J0660"] <= 0.2
e_J04202 = hdu_dt2['err_J0420'] <= 0.2
e_J08402 = hdu_dt2['err_J0840'] <= 0.2

e_r3 = hdu_dt3["err_rSDSS"] <= 0.2
e_i3 = hdu_dt3["err_iSDSS"] <= 0.2
e_J06603 = hdu_dt3["err_J0660"] <= 0.2
e_J04203 = hdu_dt3['err_J0420'] <= 0.2
e_J08403 = hdu_dt3['err_J0840'] <= 0.2


# criteria of selectios

Y_vir0 = -220*(hdu_dt0["rSDSS"] - hdu_dt0["iSDSS"]) + 40.4
Y_vir10 = 0.39*(hdu_dt0["rSDSS"] - hdu_dt0["iSDSS"]) + 0.73

Y_vir1 = -220*(hdu_dt1["rSDSS"] - hdu_dt1["iSDSS"]) + 40.4
Y_vir11 = 0.39*(hdu_dt1["rSDSS"] - hdu_dt1["iSDSS"]) + 0.73

Y_vir2 = -220*(hdu_dt2["rSDSS"] - hdu_dt2["iSDSS"]) + 40.4
Y_vir12 = 0.39*(hdu_dt2["rSDSS"] - hdu_dt2["iSDSS"]) + 0.73

Y_vir3 = -220*(hdu_dt3["rSDSS"] - hdu_dt3["iSDSS"]) + 40.4
Y_vir13 = 0.39*(hdu_dt3["rSDSS"] - hdu_dt3["iSDSS"]) + 0.73

m0 = (hdu_dt0["rSDSS"] - hdu_dt0["J0660"]) >= Y_vir0
m10 = (hdu_dt0["rSDSS"] - hdu_dt0["J0660"]) >= Y_vir10
m_r_h0 = (hdu_dt0["rSDSS"] - hdu_dt0["J0660"]) >= 0.9

m1 = (hdu_dt1["rSDSS"] - hdu_dt1["J0660"]) >= Y_vir1
m11 = (hdu_dt1["rSDSS"] - hdu_dt1["J0660"]) >= Y_vir11
m_r_h1 = (hdu_dt1["rSDSS"] - hdu_dt1["J0660"]) >= 0.9

m2 = (hdu_dt2["rSDSS"] - hdu_dt2["J0660"]) >= Y_vir2
m12 = (hdu_dt2["rSDSS"] - hdu_dt2["J0660"]) >= Y_vir12
m_r_h2 = (hdu_dt2["rSDSS"] - hdu_dt2["J0660"]) >= 0.9

m3 = (hdu_dt3["rSDSS"] - hdu_dt3["J0660"]) >= Y_vir3
m13 = (hdu_dt3["rSDSS"] - hdu_dt3["J0660"]) >= Y_vir13
m_r_h3 = (hdu_dt3["rSDSS"] - hdu_dt3["J0660"]) >= 0.9

# Other color-color diagram
# y =  26.41*x_new - 23.41
# yy = 0.66*x_new2 + 0.38
s_Y_vir0 = 26.41*(hdu_dt0["J0420"] - hdu_dt0["J0840"]) - 23.41
s_Y_vir10 = 0.66*(hdu_dt0["J0420"] - hdu_dt0["J0840"]) + 0.38

s_Y_vir1 = 26.41*(hdu_dt1["J0420"] - hdu_dt1["J0840"]) - 23.41
s_Y_vir11 = 0.66*(hdu_dt1["J0420"] - hdu_dt1["J0840"]) + 0.38

s_Y_vir2 = 26.41*(hdu_dt2["J0420"] - hdu_dt2["J0840"]) - 23.41
s_Y_vir12 = 0.66*(hdu_dt2["J0420"] - hdu_dt2["J0840"]) + 0.38

s_Y_vir3 = 26.41*(hdu_dt3["J0420"] - hdu_dt3["J0840"]) - 23.41
s_Y_vir13 = 0.66*(hdu_dt3["J0420"] - hdu_dt3["J0840"]) + 0.38

#applyging mask or criteri
s_m0 = (hdu_dt0["J0420"] - hdu_dt0["J0500"]) >= s_Y_vir0
s_m10 = (hdu_dt0["J0420"] - hdu_dt0["J0500"]) >= s_Y_vir10

s_m1 = (hdu_dt1["J0420"] - hdu_dt1["J0500"]) >= s_Y_vir1
s_m11 = (hdu_dt1["J0420"] - hdu_dt1["J0500"]) >= s_Y_vir11

s_m2 = (hdu_dt2["J0420"] - hdu_dt2["J0500"]) >= s_Y_vir2
s_m12 = (hdu_dt2["J0420"] - hdu_dt2["J0500"]) >= s_Y_vir12

s_m3 = (hdu_dt3["J0420"] - hdu_dt3["J0500"]) >= s_Y_vir3
s_m13 = (hdu_dt3["J0420"] - hdu_dt3["J0500"]) >= s_Y_vir13


mask0 = q0 

mask1 = q1  

mask2 = q2 

mask3 =  q3 

# mask0 = q0 & e_r0 & e_i0 & e_J06600 & e_J04200 & e_J08400 & m0 & m10 & s_m0 & s_m10

# mask1 = q1 & e_r1 & e_i1 & e_J06601 & e_J04201 & e_J08401 & m1 & m11 & s_m1 & s_m11

# mask2 = q2 & e_r2 & e_i2 & e_J06602 & e_J04202 & e_J08402 & m2 & m12 & s_m2 & s_m12

# mask3 = q3 & e_r3 & e_i3 & e_J06603 & e_J04203 & e_J08403 & m3 & m13 & s_m3 & s_m13

#Colours and Aplying the criteria
xc_vir0 = hdu_dt0["rSDSS"][mask0] - hdu_dt0["iSDSS"][mask0]
yc_vir0 = hdu_dt0["rSDSS"][mask0] - hdu_dt0["J0660"][mask0]

xc_vir1 = hdu_dt1["rSDSS"][mask1] - hdu_dt1["iSDSS"][mask1]
yc_vir1 = hdu_dt1["rSDSS"][mask1] - hdu_dt1["J0660"][mask1]

xc_vir2 = hdu_dt2["rSDSS"][mask2] - hdu_dt2["iSDSS"][mask2]
yc_vir2 = hdu_dt2["rSDSS"][mask2] - hdu_dt2["J0660"][mask2]

xc_vir3 = hdu_dt3["rSDSS"][mask3] - hdu_dt3["iSDSS"][mask3]
yc_vir3 = hdu_dt3["rSDSS"][mask3] - hdu_dt3["J0660"][mask3]

# xc_vir0 = hdu_dt0["rSDSS"][m_r_h0] - hdu_dt0["iSDSS"][m_r_h0]
# yc_vir0 = hdu_dt0["rSDSS"][m_r_h0] - hdu_dt0["J0660"][m_r_h0]

# xc_vir1 = hdu_dt1["rSDSS"][m_r_h1] - hdu_dt1["iSDSS"][m_r_h1]
# yc_vir1 = hdu_dt1["rSDSS"][m_r_h1] - hdu_dt1["J0660"][m_r_h1]

# xc_vir2 = hdu_dt2["rSDSS"][m_r_h2] - hdu_dt2["iSDSS"][m_r_h2]
# yc_vir2 = hdu_dt2["rSDSS"][m_r_h2] - hdu_dt2["J0660"][m_r_h2]

# xc_vir3 = hdu_dt3["rSDSS"][m_r_h3] - hdu_dt3["iSDSS"][m_r_h3]
# yc_vir3 = hdu_dt3["rSDSS"][m_r_h3] - hdu_dt3["J0660"][m_r_h3]

# color using [O III]
s_xc_vir0 = hdu_dt0["J0420"][mask0] - hdu_dt0["J0840"][mask0]
s_yc_vir0 = hdu_dt0["J0420"][mask0] - hdu_dt0["J0500"][mask0]

s_xc_vir1 = hdu_dt1["J0420"][mask1] - hdu_dt1["J0840"][mask1]
s_yc_vir1 = hdu_dt1["J0420"][mask1] - hdu_dt1["J0500"][mask1]

s_xc_vir2 = hdu_dt2["J0420"][mask2] - hdu_dt2["J0840"][mask2]
s_yc_vir2 = hdu_dt2["J0420"][mask2] - hdu_dt2["J0500"][mask2]

s_xc_vir3 = hdu_dt3["J0420"][mask3] - hdu_dt3["J0840"][mask3]
s_yc_vir3 = hdu_dt3["J0420"][mask3] - hdu_dt3["J0500"][mask3]

print(len(yc_vir0))

lgd_kws = {'frameon': True, 'fancybox': True, 'shadow': True}
#sns.set(style="dark")#, context="talk")
sns.set_style('ticks')       
fig = plt.figure(figsize=(7, 6))
ax1 = fig.add_subplot(111)
ax1.set_ylim(ymin=-1.7,ymax=2.5)
ax1.set_xlim(xmin=-2.9,xmax=3.5)
plt.tick_params(axis='x', labelsize=20)
plt.tick_params(axis='y', labelsize=20)
plt.xlabel('$r - i$', size = 20)
plt.ylabel('$r - J0660$', size = 20)
#ax4.scatter(r_i00, r_ha00, c='green', alpha=0.8, marker ='.',  s=35, label='All sources')
ax1.scatter(xc_vir0, yc_vir0, c='blue', alpha=0.8, marker ='D', s=70)
ax1.scatter(xc_vir1, yc_vir1, c='blue', alpha=0.8, marker ='D', s=70)
ax1.scatter(xc_vir2, yc_vir2, c='blue', alpha=0.8, marker ='D', s=70)
ax1.scatter(xc_vir3, yc_vir3, c='blue', alpha=0.8, marker ='D', s=70, label='J-PAS PN candidates')

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
#ax1.plot(x_new4, y_v, color='k', linestyle='--')

# Region of the simbiotic stars
result1 = findIntersection(-220, +40.4, 0.39, 0.73, 0.0)
x_new_s = np.linspace(-15.5, result1, 200)
x_new2_s = np.linspace(result1, 15.5, 200)
y_s = -220*x_new_s + 40.4
yy_s = 0.39*x_new2_s + 0.73

ax1.plot(x_new_s, y_s, color='r', linestyle='--')
ax1.plot(x_new2_s, yy_s , color='r', linestyle='--')


# for label_, x, y in zip(tab["Number"][total_m], x1, y1):
#     ax1.annotate(label_, (x, y), alpha=0.9, size=8,
#                    xytext=(-20, 5), textcoords='offset points', ha='left', va='bottom',)

plt.text(0.05, 0.90, 'Zone HPNe',
         transform=ax1.transAxes, fontsize=12.0)
ax1.minorticks_on()
#ax1.grid(which='minor')#, lw=0.3)
ax1.legend(scatterpoints=1, **lgd_kws)
ax1.grid()
#sns.despine(bottom=True)
plt.tight_layout()
plt.savefig('Fig1-SySt-aegi-viironen.pdf')
plt.clf()

##################################################################################
# [O III] #######################################################################
#################################################################################

fig = plt.figure(figsize=(7, 6))
ax2 = fig.add_subplot(111)
ax2.set_ylim(ymin=-1.7,ymax=6.6)
ax2.set_xlim(xmin=-2.0,xmax=6.5)
plt.tick_params(axis='x', labelsize=20)
plt.tick_params(axis='y', labelsize=20)
plt.xlabel('$r - i$', size = 20)
plt.ylabel('$r - J0660$', size = 20)
#ax4.scatter(r_i00, r_ha00, c='green', alpha=0.8, marker ='.',  s=35, label='All sources')
ax2.scatter(s_xc_vir0, s_yc_vir0, c='blue', alpha=0.8, marker ='D', s=70)
ax2.scatter(s_xc_vir1, s_yc_vir1, c='blue', alpha=0.8, marker ='D', s=70)
ax2.scatter(s_xc_vir2, s_yc_vir2, c='blue', alpha=0.8, marker ='D', s=70)
ax2.scatter(s_xc_vir3, s_yc_vir3, c='blue', alpha=0.8, marker ='D', s=70, label='J-PAS PN candidates')

# Region where are located the PNe
result = findIntersection(26.41, -23.41, 0.66, 0.38, 0.0)
result_y = 8.0*result + 4.50

x_new = np.linspace(15.0, result, 200)
x_new2 = np.linspace(-15.0, result, 200)
#x_new3 = np.linspace(-10.0, 1.1, 200)
y =  26.41*x_new - 23.41
yy = 0.66*x_new2 + 0.38

#Mask
#mask = y >= result_y - 0.5
ax2.plot(x_new, y, color='k', linestyle='-')
ax2.plot(x_new2, yy , color='k', linestyle='-')

#Viironen
x_new4 = np.linspace(-10.0, 11.1, 200)
y_v =  0.25*x_new4 + 1.9
#ax2.plot(x_new4, y_v, color='k', linestyle='--')

# Region of the simbiotic stars
result1 = findIntersection(0.35, -0.09, -8.75, 23.5, 0.0)
x_new_s = np.linspace(15.5, result1, 200)
x_new2_s = np.linspace(result1, -15.5, 200)
y_s = 0.35*x_new_s - 0.09
yy_s = -8.75*x_new2_s + 23.5

ax2.plot(x_new_s, y_s, color='r', linestyle='--')
ax2.plot(x_new2_s, yy_s , color='r', linestyle='--')

# for label_, x, y in zip(tab["Number"][total_m], x2, y1):
#     ax2.annotate(label_, (x, y), alpha=0.9, size=8,
#                    xytext=(-20, 5), textcoords='offset points', ha='left', va='bottom',)

plt.text(0.05, 0.90, 'Zone HPNe',
         transform=ax2.transAxes, fontsize=12.0)
ax2.minorticks_on()
#ax2.grid(which='minor')#, lw=0.3)
ax2.legend(scatterpoints=1, **lgd_kws)
ax2.grid()
#sns.despine(bottom=True)
plt.tight_layout()
#plt.savefig('Fig2-aegi-oiii.pdf')
plt.clf()


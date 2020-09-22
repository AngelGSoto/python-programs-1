'''
Getting objects that like alpha emitter but were not selected with my criteria in S-PLUS catalog (DR1)
'''
from __future__ import print_function
import numpy as np
import glob
import json
import os
import matplotlib.pyplot as plt
#import seaborn as sns
import sys
from astropy.table import Table
import argparse
import seaborn as sns
import sys
from scipy.optimize import fsolve

#The equation the represent the criteria
def findIntersection(m, y, m1, y1, x0):
    x = np.linspace(-10.0, 15.5, 200)
    return fsolve(lambda x : (m*x + y) - (m1*x + y1), x0)

n=18
magnitude = [[] for _ in range(n)]

dt = np.dtype([('Field', 'S13'), ('ID', 'f8'), ('RA', 'f8'), ('Dec', 'f8'),('X', 'f8'),('Y', 'f8'),('Aperture', 'f8'),('s2nDet', 'f4'),('PhotoFlag', 'f4'),('FWHM', 'f4'),('MUMAX', 'f4'),('A', 'f4'),('B', 'f4'),('THETA', 'f4'),('FlRadDet', 'f4'),('KrRadDet', 'f4'),('U_auto', 'f8'),('dU_auto', 'f4'), ('s2n_U_auto', 'f4'), ('U_petro', 'f4'), ('dU_petro', 'f4'), ('s2n_U_petro ', 'f4'), ('U_aper', 'f4'), ('DU_aper', 'f4'), ('S2n_U_aper', 'f4'), ('F0378_auto', 'f8'),('dF0378_auto', 'f4'),('s2n_F0378_auto', 'f4'),('F0378_petro', 'f4'),('dF0378_petro', 'f4'),('s2n_F0378_petro', 'f4'),('F0378_aper', 'f4'),('dF0378_aper', 'f4'),('s2n_F0378_aper', 'f4'),('F0395_auto', 'f8'),('dF0395_auto', 'f4'),('s2n_F0395_auto', 'f4'),('F0395_petro', 'f4'),('dF0395_petro', 'f4'),('s2n_F0395_petro', 'f4'),('F0395_aper', 'f4'),('dF0395_aper', 'f4'),('s2n_F0395_aper', 'f4'),('F0410_auto', 'f8'),('dF0410_auto', 'f4'),('s2n_F0410_auto', 'f4'),('F0410_petro', 'f4'),('dF0410_petro', 'f4'),('s2n_F0410_petro', 'f4'),('F0410_aper', 'f4'),('dF0410_aper', 'f4'),('s2n_F0410_aper', 'f4'),('F0430_auto', 'f8'),('dF0430_auto', 'f4'),('s2n_F0430_auto', 'f4'),('F0430_petro', 'f4'),('dF0430_petro', 'f4'),('s2n_F0430_petro', 'f4'),('F0430_aper', 'f4'),('dF0430_aper', 'f4'),('s2n_F0430_aper', 'f4'),('G_auto', 'f8'),('dG_auto', 'f4'),('s2n_G_auto', 'f4'),('G_petro', 'f4'),('dG_petro', 'f4'),('s2n_G_petro', 'f4'),('G_aper', 'f4'),('dG_aper', 'f4'),('s2n_G_aper', 'f4'),('F0515_auto', 'f8'),('dF0515_auto', 'f4'),('s2n_F0515_auto', 'f4'),('F0515_petro', 'f4'),('dF0515_petro', 'f4'),('s2n_F0515_petro', 'f4'),('F0515_aper', 'f4'),('dF0515_aper', 'f4'),(' s2n_F0515_aper', 'f4'),('R_auto', 'f8'),('dR_auto', 'f4'),('s2n_R_auto', 'f4'),('R_petro', 'f4'),('dR_petro', 'f4'),('s2n_R_petro', 'f4'),('R_aper', 'f4'),('dR_aper', 'f4'),('s2n_R_aper', 'f4'),('F0660_auto', 'f8'),('dF0660_auto', 'f4'),('s2n_F0660_auto', 'f4'),('F0660_petro', 'f4'),('dF0660_petro', 'f4'),('s2n_F0660_petro', 'f4'),('F0660_aper', 'f4'),('dF0660_aper', 'f4'),('s2n_F0660_aper', 'f4'),('I_auto', 'f8'),('dI_auto', 'f4'),('s2n_I_auto', 'f4'),('I_petro', 'f4'),('dI_petro', 'f4'),('s2n_I_petro', 'f4'),('I_aper', 'f4'),('dI_aper', 'f4'),('s2n_I_aper', 'f4'),('F0861_auto', 'f8'),('dF0861_auto', 'f4'),('s2n_F0861_auto', 'f4'),('F0861_petro', 'f4'),('dF0861_petro', 'f4'),('s2n_F0861_petro', 'f4'),('F0861_aper', 'f4'),('dF0861_aper', 'f4'),('s2n_F0861_aper', 'f4'),('Z_auto', 'f8'),('dZ_auto', 'f4'),('s2n_Z_auto', 'f4'),('Z_petro', 'f4'),('dZ_petro', 'f4'),('s2n_Z_petro', 'f4'),('Z_aper', 'f4'),('dZ_aper', 'f4'),('s2n_Z_aper', 'f4'),('zb', 'f4'), ('zb_Min', 'f4'),('zb_Max', 'f4'), ('Tb', 'f4'),('Odds', 'f4'),('Chi2', 'f4'),('M_B', 'f4'),('Stell_Mass', 'f4'),('CLASS', 'f4'), ('PROB_GAL', 'f8'),('PROB_STAR', 'f8'), ('RA_1', 'f4'),('DEC_1', 'f4'), ('Sep', 'f8')])

data = np.loadtxt("halpha-emitter-galaxy-STRIPE82.txt", dtype=dt)
data1 = np.loadtxt("HII-region-emitter-galaxy-STRIPE82-2.txt", dtype=dt)

Id = data['ID']
Field = data['Field']

#Color
x1 = data['F0515_auto'] - data['F0861_auto']
y1 = data['F0515_auto'] - data['F0660_auto']

x11 = data['F0515_petro'] - data['F0861_petro']
y11 = data['F0515_petro'] - data['F0660_petro']

x111 = data['F0515_aper'] - data['F0861_aper']
y111 = data['F0515_aper'] - data['F0660_aper']
    
#Color
x2 = data['Z_auto'] - data['G_auto']
y2 = data['Z_auto'] - data['F0660_auto']

x22 = data['Z_petro'] - data['G_petro']
y22 = data['Z_petro'] - data['F0660_petro']

x222 = data['Z_aper'] - data['G_aper']
y222 = data['Z_aper'] - data['F0660_aper']

#Color
x3 = data['F0660_auto'] - data['R_auto']
y3 = data['F0660_auto'] - data['G_auto']

x33 = data['F0660_petro'] - data['R_petro']
y33 = data['F0660_petro'] - data['G_petro']

x333 = data['F0660_aper'] - data['R_aper']
y333 = data['F0660_aper'] - data['G_aper']

#Color
x4 = data['F0660_auto'] - data['R_auto']
y4 = data['G_auto'] - data['F0515_auto']

x44 = data['F0660_petro'] - data['R_petro']
y44 = data['G_petro'] - data['F0515_petro']

x444 = data['F0660_aper'] - data['R_aper']
y444 = data['G_aper'] - data['F0515_aper']
    
#Color
x5 = data['G_auto'] - data['I_auto']
y5 = data['F0410_auto'] - data['F0660_auto']

x55 = data['G_petro'] - data['I_petro']
y55 = data['F0410_petro'] - data['F0660_petro']

x555 = data['G_aper'] - data['I_aper']
y555 = data['F0410_aper'] - data['F0660_aper']

#Color Vironen
x6 = data['R_auto'] - data['I_auto']
y6 = data['R_auto'] - data['F0660_auto']

x66 = data['R_petro'] - data['I_petro']
y66 = data['R_petro'] - data['F0660_petro']

x666 = data['R_aper'] - data['I_aper']
y666 = data['R_aper'] - data['F0660_aper']

######################################################
# color H II of the galaxy
######################################################

Idd = data1['ID']
Fieldd = data1['Field']

#Color
xx1 = data1['F0515_auto'] - data1['F0861_auto']
yy1 = data1['F0515_auto'] - data1['F0660_auto']

xx11 = data1['F0515_petro'] - data1['F0861_petro']
yy11 = data1['F0515_petro'] - data1['F0660_petro']

xx111 = data1['F0515_aper'] - data1['F0861_aper']
yy111 = data1['F0515_aper'] - data1['F0660_aper']
    
#Color
xx2 = data1['Z_auto'] - data1['G_auto']
yy2 = data1['Z_auto'] - data1['F0660_auto']

xx22 = data1['Z_petro'] - data1['G_petro']
yy22 = data1['Z_petro'] - data1['F0660_petro']

xx222 = data1['Z_aper'] - data1['G_aper']
yy222 = data1['Z_aper'] - data1['F0660_aper']

#Color
xx3 = data1['F0660_auto'] - data1['R_auto']
yy3 = data1['F0660_auto'] - data1['G_auto']

xx33 = data1['F0660_petro'] - data1['R_petro']
yy33 = data1['F0660_petro'] - data1['G_petro']

xx333 = data1['F0660_aper'] - data1['R_aper']
yy333 = data1['F0660_aper'] - data1['G_aper']

#Color
xx4 = data1['F0660_auto'] - data1['R_auto']
yy4 = data1['G_auto'] - data1['F0515_auto']

xx44 = data1['F0660_petro'] - data1['R_petro']
yy44 = data1['G_petro'] - data1['F0515_petro']

xx444 = data1['F0660_aper'] - data1['R_aper']
yy444 = data1['G_aper'] - data1['F0515_aper']
    
#Color
xx5 = data1['G_auto'] - data1['I_auto']
yy5 = data1['F0410_auto'] - data1['F0660_auto']

xx55 = data1['G_petro'] - data1['I_petro']
yy55 = data1['F0410_petro'] - data1['F0660_petro']

xx555 = data1['G_aper'] - data1['I_aper']
yy555 = data1['F0410_aper'] - data1['F0660_aper']

#Color Vironen
xx6 = data1['R_auto'] - data1['I_auto']
yy6 = data1['R_auto'] - data1['F0660_auto']

xx66 = data1['R_petro'] - data1['I_petro']
yy66 = data1['R_petro'] - data1['F0660_petro']

xx666 = data1['R_aper'] - data1['I_aper']
yy666 = data1['R_aper'] - data1['F0660_aper']

############################################################################### AUTO
############################################################################### AUTO
lgd_kws = {'frameon': True, 'fancybox': True, 'shadow': True}
#sns.set(style="dark")#, context="ta1lk")
sns.set_style('ticks')       
fig = plt.figure(figsize=(7, 6))
ax1 = fig.add_subplot(111)
ax1.set_xlim(xmin=-2.5,xmax=5.5)
ax1.set_ylim(ymin=-2.0,ymax=5.0)
plt.tick_params(axis='x', labelsize=20)
plt.tick_params(axis='y', labelsize=20)
plt.xlabel('$J0515 - J0861$', size = 20)
plt.ylabel('$J0515 - J0660$', size = 20)
#ax4.scatter(r_i00, r_ha00, c='green', alpha=0.8, marker ='.',  s=35, label='All sources')
ax1.scatter(x1, y1, c='magenta', alpha=0.8, marker ='D', s=70, label="Halpha emitters")
ax1.scatter(xx1, yy1, c='red', alpha=0.8, marker ='D', s=70, label="H II regions")

# Region where are located the PNe
result = findIntersection(2.7, 2.15, 0.0, 0.22058956, 0.0)
result_y = 2.7*result + 2.15

x_new = np.linspace(result, 15.5, 200)
x_new2 = np.linspace(-10.0, result, 200)
x_new3 = np.linspace(-10.0, result, 200)
y = 2.7*x_new + 2.15
yy = 0.0*x_new2 + 0.22058956

#Mask
#mask = y >= result_y - 0.5
ax1.plot(x_new, y, color='k', linestyle='-')
ax1.plot(x_new2, yy , color='k', linestyle='-')

# ax1.fill_between(x_new2, y, yy)
# ax1.fill(y, yy)

# for label_, x, y in zip(Id, x1, y1):
#     ax1.annotate(label_, (x, y), alpha=0.9, size=8,
#                    xytext=(3, 5), textcoords='offset points', ha='left', va='bottom',)

plt.text(0.05, 0.90, 'Zone HPNe',
         transform=ax1.transAxes, fontsize='small')
ax1.minorticks_on()
#ax1.grid(which='minor')#, lw=0.3)
ax1.legend(scatterpoints=1, **lgd_kws)
ax1.grid()
#sns.despine(bottom=True)
plt.tight_layout()
plt.savefig('Fig1-EDR-SPLUS-J0515-J0861-marz18_auto.pdf')
plt.clf()
#############################################################################
#z - J0660 v z - g ##########################################################
###############################################################################

lgd_kws = {'frameon': True, 'fancybox': True, 'shadow': True}
#sns.set(style="dark")#, context="talk")
sns.set_style('ticks')       
fig = plt.figure(figsize=(7, 6))
ax2 = fig.add_subplot(111)
ax2.set_xlim(xmin=-5.8,xmax=2.5)
ax2.set_ylim(ymin=-3.0,ymax=5.0)
plt.tick_params(axis='x', labelsize=20)
plt.tick_params(axis='y', labelsize=20)
plt.xlabel('$zSDSS - gSDSS$', size =20)
plt.ylabel('$zSDSS - J0660$', size =20)
#ax4.scatter(r_i00, r_ha00, c='green', alpha=0.8, marker ='.',  s=35, label='All sources')
ax2.scatter(x2, y2, c='magenta', alpha=0.8, marker ='D', s=70, label='Halpha emitters')#,  s=55, label='Halpha emitters')
ax2.scatter(xx2, yy2, c='red', alpha=0.8, marker ='D', s=70, label='H II regions')

# Region where stay the PNe
result = findIntersection(0.2319, 0.85, -1.3, 1.7, 0.0)
result_y = 0.2319*result + 0.85

x_new = np.linspace(result, 15.5, 200)
x_new2 = np.linspace(-10.0, result, 200)

y = 0.2319*x_new + 0.85
yy = -1.3*x_new2 +  1.7
#Mask
#mask = y >= result_y - 0.5
ax2.plot(x_new, y, color='k', linestyle='-')
ax2.plot(x_new2, yy , color='k', linestyle='-')

# ax2.plot(X, 0.2319*X + 0.85, color='k', linestyle='-')
# ax2.plot(X, -1.3*X + 1.7, color='k', linestyle='-')
# for label_, x, y in zip(Id, x2, y2):
#     ax2.annotate(label_, (x, y), alpha=0.9, size=8,
#                    xytext=(3, 5), textcoords='offset points', ha='left', va='bottom',)

plt.text(0.8, 0.9, 'Zone HPNe',
         transform=ax2.transAxes, fontsize='small')

ax2.minorticks_on()
#ax1.grid(which='minor')#, lw=0.3)
ax2.legend(scatterpoints=1, loc="upper left", **lgd_kws)
ax2.grid()
#sns.despine(bottom=True)
plt.tight_layout()
plt.savefig('Fig2-EDR-SPLUS-zSDSS-gSDSS-marz18_auto.pdf')
plt.clf()
###################################################################################
#J0660 - rSDSS vs J0660 - gSDSS ###################################################
###################################################################################
lgd_kws = {'frameon': True, 'fancybox': True, 'shadow': True}
#sns.set(style="dark")#, context="talk")
sns.set_style('ticks')       
fig = plt.figure(figsize=(7, 6))
ax4 = fig.add_subplot(111)
ax4.set_xlim(xmin=-2.5,xmax=0.5)
ax4.set_ylim(ymin=-5.0,ymax=1.5)
plt.tick_params(axis='x', labelsize=20)
plt.tick_params(axis='y', labelsize=20)
plt.xlabel('$J0660 - rSDSS$', size =20)
plt.ylabel('$J0660 - gSDSS$', size =20)
#ax4.scatter(r_i00, r_ha00, c='green', alpha=0.8, marker ='.',  s=35, label='All sources')
ax4.scatter(x3, y3, c='magenta', alpha=0.8, marker ='D', s=70, label='Halpha emitters')#, label='Halpha emitters')
ax4.scatter(x3, y3, c='magenta', alpha=0.8, marker ='D', s=70, label='Halpha emitters')
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

# ax4.plot(X, 1.559*X + 0.58, color='k', linestyle='-')
# ax4.axvline(x=-0.5, color='k', linestyle='-')
# for label_, x, y in zip(Id, x3, y3):
#     ax4.annotate(label_, (x, y), alpha=0.9, size=8,
#                    xytext=(3, 5), textcoords='offset points', ha='left', va='bottom',)

plt.text(0.05, 0.90, 'Zone HPNe',
         transform=ax4.transAxes, fontsize='small')

ax4.minorticks_on()
#ax1.grid(which='minor')#, lw=0.3)
ax4.legend(scatterpoints=1, **lgd_kws)
ax4.grid()
#sns.despine(bottom=True)
plt.tight_layout()
plt.savefig('Fig3-EDR-SPLUS-J0660-rSDSS-marz18_auto.pdf')
plt.clf()

###################################################################################
#gSDSS - J0515 vs J0660 - rSDSS ###################################################
###################################################################################
lgd_kws = {'frameon': True, 'fancybox': True, 'shadow': True}
#sns.set(style="dark")#, context="talk")
sns.set_style('ticks')       
fig = plt.figure(figsize=(7, 6))
ax5 = fig.add_subplot(111)
ax5.set_xlim(xmin=-2.5,xmax=0.8)
ax5.set_ylim(ymin=-2.0,ymax=1.5)
plt.tick_params(axis='x', labelsize=20)
plt.tick_params(axis='y', labelsize=20)
plt.xlabel('$J0660 - rSDSS$', size =20)
plt.ylabel('$gSDSS - J0515$', size =20)
#ax4.scatter(r_i00, r_ha00, c='green', alpha=0.8, marker ='.',  s=35, label='All sources')
ax5.scatter(x4, y4, c='magenta', alpha=0.8, marker ='D', s=70, label='Halpha emitters')
ax5.scatter(xx4, yy4, c='red', alpha=0.8, marker ='D', s=70, label='H II regions')

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
ax5.plot(x_new, y, color='k', linestyle='-')
ax5.plot(x_new2, yy , color='k', linestyle='-')

# ax5.plot(X, 0.12*X - 0.01, color='k', linestyle='-' )
# ax5.plot(X, -1.1*X - 1.07, color='k', linestyle='-' )

# for label_, x, y in zip(Id, x4, y4):
#     ax5.annotate(label_, (x, y), alpha=0.9, size=8,
#                    xytext=(3, 5), textcoords='offset points', ha='left', va='bottom',)

plt.text(0.05, 0.4, 'Zone HPNe',
         transform=ax5.transAxes, fontsize='small')
ax5.minorticks_on()
#ax1.grid(which='minor')#, lw=0.3)
ax5.legend(scatterpoints=1, **lgd_kws)
ax5.grid()
#sns.despine(bottom=True)
plt.tight_layout()
plt.savefig('Fig4-EDR-JPLUS-J0660-rSDSS-marz18_magenta.pdf')
plt.clf()

###################################################################################
#J0410 vs J0660 - J0660 ###################################################
###################################################################################
lgd_kws = {'frameon': True, 'fancybox': True, 'shadow': True}
#sns.set(style="dark")#, context="talk")
sns.set_style('ticks')       
fig = plt.figure(figsize=(7, 6))
ax6 = fig.add_subplot(111)
ax6.set_xlim(xmin=-3.0,xmax=5.0)
ax6.set_ylim(ymin=-2.0,ymax=6.0)
plt.tick_params(axis='x', labelsize=20)
plt.tick_params(axis='y', labelsize=20)
plt.xlabel('$gSDSS - iSDSS$', size =20)
plt.ylabel('$J0410 - J0660$', size =20)
#ax4.scatter(r_i00, r_ha00, c='green', alpha=0.8, marker ='.',  s=35, label='All sources')
ax6.scatter(x5, y5, c='magenta', alpha=0.8, marker ='D', s=70, label="Halpha emitters")
ax6.scatter(xx5, yy5, c='red', alpha=0.8, marker ='D', s=70, label="H II regions")

# Region where are located the PNe
result = findIntersection(8.0, 4.50, 0.8, 0.55, 0.0)
result_y = 8.0*result + 4.50

x_new = np.linspace(result, 15.5, 200)
x_new2 = np.linspace(-10.0, result, 200)
x_new3 = np.linspace(-10.0, 1.1, 200)
y =  8.0*x_new + 4.50
yy = 0.8*x_new2 + 0.55
#Mask
#mask = y >= result_y - 0.5
ax6.plot(x_new, y, color='k', linestyle='-')
ax6.plot(x_new2, yy , color='k', linestyle='-')

# ax6.plot(X, 8.0*X + 4.50, color='k', linestyle='-')
# ax6.plot(X, 0.8*X + 0.55, color='k', linestyle='-')

# for label_, x, y in zip(Id, x5, y5):
#     ax6.annotate(label_, (x, y), alpha=0.9, size=8,
#                    xytext=(3, 5), textcoords='offset points', ha='left', va='bottom',)

plt.text(0.05, 0.90, 'Zone HPNe',
         transform=ax6.transAxes, fontsize='small')
ax6.minorticks_on()
#ax1.grid(which='minor')#, lw=0.3)
ax6.legend(scatterpoints=1, **lgd_kws)
ax6.grid()
#sns.despine(bottom=True)
plt.tight_layout()
plt.savefig('Fig5-EDR-JPLUS-gSDSS-iSDSS-marz18_auto.pdf')
plt.clf()

#############################################################################################################
#Vironen
############################################################################################################
lgd_kws = {'frameon': True, 'fancybox': True, 'shadow': True}
#sns.set(style="dark")#, context="talk")
sns.set_style('ticks')       
fig = plt.figure(figsize=(7, 6))
ax7 = fig.add_subplot(111)
ax7.set_xlim(xmin=-3.0,xmax=3.0)
ax7.set_ylim(ymin=-1.0,ymax=3.0)
plt.tick_params(axis='x', labelsize=20)
plt.tick_params(axis='y', labelsize=20)
plt.xlabel('$rSDSS - iSDSS$', size =20)
plt.ylabel('$rSDSS - J0660$', size =20)
#ax4.scatter(r_i00, r_ha00, c='green', alpha=0.8, marker ='.',  s=35, label='All sources')
ax7.scatter(x6, y6, c='magenta', alpha=0.8, marker ='D', s=70, label="Halpha emitters")
ax7.scatter(xx6, yy6, c='red', alpha=0.8, marker ='D', s=70, label="H II regions")

# Region where are located the PNe
result = findIntersection(0.43, 0.65, 7.0, 3.0, 0.0)
result_y = 8.0*result + 4.50

x_new = np.linspace(-15.0, result, 200)
x_new2 = np.linspace(result, 15.0, 200)
x_new3 = np.linspace(-10.0, 1.1, 200)
y =  0.43*x_new + 0.65
yy = 7.0*x_new2 + 3.0
#Mask
#mask = y >= result_y - 0.5
ax7.plot(x_new, y, color='k', linestyle='-')
ax7.plot(x_new2, yy , color='k', linestyle='-')

# Region of the simbiotic stars
result1 = findIntersection(-220, +40.4, 0.39, 0.73, 0.0)
x_new_s = np.linspace(-15.5, result1, 200)
x_new2_s = np.linspace(result1, 15.5, 200)
y_s = -220*x_new_s + 40.4
yy_s = 0.39*x_new2_s + 0.73

ax7.plot(x_new_s, y_s, color='r', linestyle='--')
ax7.plot(x_new2_s, yy_s , color='r', linestyle='--')


# ax6.plot(X, 8.0*X + 4.50, color='k', linestyle='-')
# ax6.plot(X, 0.8*X + 0.55, color='k', linestyle='-')

# for label_, x, y in zip(Id, x6, y6):
#     ax7.annotate(label_, (x, y), alpha=0.9, size=8,
#                    xytext=(-20.0, 5), textcoords='offset points', ha='left', va='bottom',)


plt.text(0.05, 0.90, 'Zone HPNe',
         transform=ax6.transAxes, fontsize='small')
ax7.minorticks_on()
#ax1.grid(which='minor')#, lw=0.3)
ax7.legend(scatterpoints=1, **lgd_kws)
ax7.grid()
#sns.despine(bottom=True)
plt.tight_layout()
plt.savefig('Fig6-EDR-SPLUS-vironen-marz18_auto.pdf')
plt.clf()

###########################################################################
###########################################################################
#Petro
###########################################################################
###########################################################################
lgd_kws = {'frameon': True, 'fancybox': True, 'shadow': True}
#sns.set(style="dark")#, context="ta1lk")
sns.set_style('ticks')       
fig = plt.figure(figsize=(7, 6))
ax1 = fig.add_subplot(111)
ax1.set_xlim(xmin=-2.5,xmax=5.5)
ax1.set_ylim(ymin=-2.0,ymax=5.0)
plt.tick_params(axis='x', labelsize=20)
plt.tick_params(axis='y', labelsize=20)
plt.xlabel('$J0515 - J0861$', size = 20)
plt.ylabel('$J0515 - J0660$', size = 20)
#ax4.scatter(r_i00, r_ha00, c='green', alpha=0.8, marker ='.',  s=35, label='All sources')
ax1.scatter(x11, y11, c='magenta', alpha=0.8, marker ='D', s=70, label="Halpha emitters")
ax1.scatter(xx11, yy11, c='red', alpha=0.8, marker ='D', s=70, label="H II regions")

# Region where are located the PNe
result = findIntersection(2.7, 2.15, 0.0, 0.22058956, 0.0)
result_y = 2.7*result + 2.15

x_new = np.linspace(result, 15.5, 200)
x_new2 = np.linspace(-10.0, result, 200)
x_new3 = np.linspace(-10.0, result, 200)
y = 2.7*x_new + 2.15
yy = 0.0*x_new2 + 0.22058956

#Mask
#mask = y >= result_y - 0.5
ax1.plot(x_new, y, color='k', linestyle='-')
ax1.plot(x_new2, yy , color='k', linestyle='-')

# ax1.fill_between(x_new2, y, yy)
# ax1.fill(y, yy)

# for label_, x, y in zip(Id, x1, y1):
#     ax1.annotate(label_, (x, y), alpha=0.9, size=8,
#                    xytext=(3, 5), textcoords='offset points', ha='left', va='bottom',)

plt.text(0.05, 0.90, 'Zone HPNe',
         transform=ax1.transAxes, fontsize='small')
ax1.minorticks_on()
#ax1.grid(which='minor')#, lw=0.3)
ax1.legend(scatterpoints=1, **lgd_kws)
ax1.grid()
#sns.despine(bottom=True)
plt.tight_layout()
plt.savefig('Fig1-EDR-SPLUS-J0515-J0861-marz18_petro.pdf')
plt.clf()
#############################################################################
#z - J0660 v z - g ##########################################################
###############################################################################

lgd_kws = {'frameon': True, 'fancybox': True, 'shadow': True}
#sns.set(style="dark")#, context="talk")
sns.set_style('ticks')       
fig = plt.figure(figsize=(7, 6))
ax2 = fig.add_subplot(111)
ax2.set_xlim(xmin=-5.8,xmax=2.5)
ax2.set_ylim(ymin=-3.0,ymax=5.0)
plt.tick_params(axis='x', labelsize=20)
plt.tick_params(axis='y', labelsize=20)
plt.xlabel('$zSDSS - gSDSS$', size =20)
plt.ylabel('$zSDSS - J0660$', size =20)
#ax4.scatter(r_i00, r_ha00, c='green', alpha=0.8, marker ='.',  s=35, label='All sources')
ax2.scatter(x22, y22, c='magenta', alpha=0.8, marker ='D', s=70, label='Halpha emitters')#,  s=55, label='Halpha emitters')
ax2.scatter(xx22, yy22, c='red', alpha=0.8, marker ='D', s=70, label='H II regions')

# Region where stay the PNe
result = findIntersection(0.2319, 0.85, -1.3, 1.7, 0.0)
result_y = 0.2319*result + 0.85

x_new = np.linspace(result, 15.5, 200)
x_new2 = np.linspace(-10.0, result, 200)

y = 0.2319*x_new + 0.85
yy = -1.3*x_new2 +  1.7
#Mask
#mask = y >= result_y - 0.5
ax2.plot(x_new, y, color='k', linestyle='-')
ax2.plot(x_new2, yy , color='k', linestyle='-')

# ax2.plot(X, 0.2319*X + 0.85, color='k', linestyle='-')
# ax2.plot(X, -1.3*X + 1.7, color='k', linestyle='-')
# for label_, x, y in zip(Id, x2, y2):
#     ax2.annotate(label_, (x, y), alpha=0.9, size=8,
#                    xytext=(3, 5), textcoords='offset points', ha='left', va='bottom',)

plt.text(0.8, 0.9, 'Zone HPNe',
         transform=ax2.transAxes, fontsize='small')

ax2.minorticks_on()
#ax1.grid(which='minor')#, lw=0.3)
ax2.legend(scatterpoints=1, loc="upper left", **lgd_kws)
ax2.grid()
#sns.despine(bottom=True)
plt.tight_layout()
plt.savefig('Fig2-EDR-SPLUS-zSDSS-gSDSS-marz18_petro.pdf')
plt.clf()
###################################################################################
#J0660 - rSDSS vs J0660 - gSDSS ###################################################
###################################################################################
lgd_kws = {'frameon': True, 'fancybox': True, 'shadow': True}
#sns.set(style="dark")#, context="talk")
sns.set_style('ticks')       
fig = plt.figure(figsize=(7, 6))
ax4 = fig.add_subplot(111)
ax4.set_xlim(xmin=-2.5,xmax=0.5)
ax4.set_ylim(ymin=-5.0,ymax=1.5)
plt.tick_params(axis='x', labelsize=20)
plt.tick_params(axis='y', labelsize=20)
plt.xlabel('$J0660 - rSDSS$', size =20)
plt.ylabel('$J0660 - gSDSS$', size =20)
#ax4.scatter(r_i00, r_ha00, c='green', alpha=0.8, marker ='.',  s=35, label='All sources')
ax4.scatter(x33, y33, c='magenta', alpha=0.8, marker ='D', s=70, label='Halpha emitters')#, label='Halpha emitters')
ax4.scatter(xx33, yy33, c='magenta', alpha=0.8, marker ='D', s=70, label='Halpha emitters')
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

# ax4.plot(X, 1.559*X + 0.58, color='k', linestyle='-')
# ax4.axvline(x=-0.5, color='k', linestyle='-')
# for label_, x, y in zip(Id, x3, y3):
#     ax4.annotate(label_, (x, y), alpha=0.9, size=8,
#                    xytext=(3, 5), textcoords='offset points', ha='left', va='bottom',)

plt.text(0.05, 0.90, 'Zone HPNe',
         transform=ax4.transAxes, fontsize='small')

ax4.minorticks_on()
#ax1.grid(which='minor')#, lw=0.3)
ax4.legend(scatterpoints=1, **lgd_kws)
ax4.grid()
#sns.despine(bottom=True)
plt.tight_layout()
plt.savefig('Fig3-EDR-SPLUS-J0660-rSDSS-marz18_petro.pdf')
plt.clf()

###################################################################################
#gSDSS - J0515 vs J0660 - rSDSS ###################################################
###################################################################################
lgd_kws = {'frameon': True, 'fancybox': True, 'shadow': True}
#sns.set(style="dark")#, context="talk")
sns.set_style('ticks')       
fig = plt.figure(figsize=(7, 6))
ax5 = fig.add_subplot(111)
ax5.set_xlim(xmin=-2.5,xmax=0.8)
ax5.set_ylim(ymin=-2.0,ymax=1.5)
plt.tick_params(axis='x', labelsize=20)
plt.tick_params(axis='y', labelsize=20)
plt.xlabel('$J0660 - rSDSS$', size =20)
plt.ylabel('$gSDSS - J0515$', size =20)
#ax4.scatter(r_i00, r_ha00, c='green', alpha=0.8, marker ='.',  s=35, label='All sources')
ax5.scatter(x44, y44, c='magenta', alpha=0.8, marker ='D', s=70, label='Halpha emitters')
ax5.scatter(xx44, yy44, c='red', alpha=0.8, marker ='D', s=70, label='H II regions')

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
ax5.plot(x_new, y, color='k', linestyle='-')
ax5.plot(x_new2, yy , color='k', linestyle='-')

# ax5.plot(X, 0.12*X - 0.01, color='k', linestyle='-' )
# ax5.plot(X, -1.1*X - 1.07, color='k', linestyle='-' )

# for label_, x, y in zip(Id, x4, y4):
#     ax5.annotate(label_, (x, y), alpha=0.9, size=8,
#                    xytext=(3, 5), textcoords='offset points', ha='left', va='bottom',)

plt.text(0.05, 0.4, 'Zone HPNe',
         transform=ax5.transAxes, fontsize='small')
ax5.minorticks_on()
#ax1.grid(which='minor')#, lw=0.3)
ax5.legend(scatterpoints=1, **lgd_kws)
ax5.grid()
#sns.despine(bottom=True)
plt.tight_layout()
plt.savefig('Fig4-EDR-JPLUS-J0660-rSDSS-marz18_petro.pdf')
plt.clf()

###################################################################################
#J0410 vs J0660 - J0660 ###################################################
###################################################################################
lgd_kws = {'frameon': True, 'fancybox': True, 'shadow': True}
#sns.set(style="dark")#, context="talk")
sns.set_style('ticks')       
fig = plt.figure(figsize=(7, 6))
ax6 = fig.add_subplot(111)
ax6.set_xlim(xmin=-3.0,xmax=5.0)
ax6.set_ylim(ymin=-2.0,ymax=6.0)
plt.tick_params(axis='x', labelsize=20)
plt.tick_params(axis='y', labelsize=20)
plt.xlabel('$gSDSS - iSDSS$', size =20)
plt.ylabel('$J0410 - J0660$', size =20)
#ax4.scatter(r_i00, r_ha00, c='green', alpha=0.8, marker ='.',  s=35, label='All sources')
ax6.scatter(x55, y55, c='magenta', alpha=0.8, marker ='D', s=70, label="Halpha emitters")
ax6.scatter(xx55, yy55, c='red', alpha=0.8, marker ='D', s=70, label="H II regions")

# Region where are located the PNe
result = findIntersection(8.0, 4.50, 0.8, 0.55, 0.0)
result_y = 8.0*result + 4.50

x_new = np.linspace(result, 15.5, 200)
x_new2 = np.linspace(-10.0, result, 200)
x_new3 = np.linspace(-10.0, 1.1, 200)
y =  8.0*x_new + 4.50
yy = 0.8*x_new2 + 0.55
#Mask
#mask = y >= result_y - 0.5
ax6.plot(x_new, y, color='k', linestyle='-')
ax6.plot(x_new2, yy , color='k', linestyle='-')

# ax6.plot(X, 8.0*X + 4.50, color='k', linestyle='-')
# ax6.plot(X, 0.8*X + 0.55, color='k', linestyle='-')

# for label_, x, y in zip(Id, x5, y5):
#     ax6.annotate(label_, (x, y), alpha=0.9, size=8,
#                    xytext=(3, 5), textcoords='offset points', ha='left', va='bottom',)

plt.text(0.05, 0.90, 'Zone HPNe',
         transform=ax6.transAxes, fontsize='small')
ax6.minorticks_on()
#ax1.grid(which='minor')#, lw=0.3)
ax6.legend(scatterpoints=1, **lgd_kws)
ax6.grid()
#sns.despine(bottom=True)
plt.tight_layout()
plt.savefig('Fig5-EDR-JPLUS-gSDSS-iSDSS-marz18_petro.pdf')
plt.clf()

#############################################################################################################
#Vironen
############################################################################################################
lgd_kws = {'frameon': True, 'fancybox': True, 'shadow': True}
#sns.set(style="dark")#, context="talk")
sns.set_style('ticks')       
fig = plt.figure(figsize=(7, 6))
ax7 = fig.add_subplot(111)
ax7.set_xlim(xmin=-3.0,xmax=3.0)
ax7.set_ylim(ymin=-1.0,ymax=3.0)
plt.tick_params(axis='x', labelsize=20)
plt.tick_params(axis='y', labelsize=20)
plt.xlabel('$rSDSS - iSDSS$', size =20)
plt.ylabel('$rSDSS - J0660$', size =20)
#ax4.scatter(r_i00, r_ha00, c='green', alpha=0.8, marker ='.',  s=35, label='All sources')
ax7.scatter(x66, y66, c='magenta', alpha=0.8, marker ='D', s=70, label="Halpha emitters")
ax7.scatter(xx66, yy66, c='red', alpha=0.8, marker ='D', s=70, label="H II regions")

# Region where are located the PNe
result = findIntersection(0.43, 0.65, 7.0, 3.0, 0.0)
result_y = 8.0*result + 4.50

x_new = np.linspace(-15.0, result, 200)
x_new2 = np.linspace(result, 15.0, 200)
x_new3 = np.linspace(-10.0, 1.1, 200)
y =  0.43*x_new + 0.65
yy = 7.0*x_new2 + 3.0
#Mask
#mask = y >= result_y - 0.5
ax7.plot(x_new, y, color='k', linestyle='-')
ax7.plot(x_new2, yy , color='k', linestyle='-')

# Region of the simbiotic stars
result1 = findIntersection(-220, +40.4, 0.39, 0.73, 0.0)
x_new_s = np.linspace(-15.5, result1, 200)
x_new2_s = np.linspace(result1, 15.5, 200)
y_s = -220*x_new_s + 40.4
yy_s = 0.39*x_new2_s + 0.73

ax7.plot(x_new_s, y_s, color='r', linestyle='--')
ax7.plot(x_new2_s, yy_s , color='r', linestyle='--')


# ax6.plot(X, 8.0*X + 4.50, color='k', linestyle='-')
# ax6.plot(X, 0.8*X + 0.55, color='k', linestyle='-')

# for label_, x, y in zip(Id, x6, y6):
#     ax7.annotate(label_, (x, y), alpha=0.9, size=8,
#                    xytext=(-20.0, 5), textcoords='offset points', ha='left', va='bottom',)


plt.text(0.05, 0.90, 'Zone HPNe',
         transform=ax6.transAxes, fontsize='small')
ax7.minorticks_on()
#ax1.grid(which='minor')#, lw=0.3)
ax7.legend(scatterpoints=1, **lgd_kws)
ax7.grid()
#sns.despine(bottom=True)
plt.tight_layout()
plt.savefig('Fig6-EDR-SPLUS-vironen-marz18_petro.pdf')
plt.clf()

###########################################################################
#Aper 3''
###########################################################################

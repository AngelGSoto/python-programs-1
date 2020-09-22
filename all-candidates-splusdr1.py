'''
Read the table from SPLUS EDR table to make the colour-colour diagrams
'''
from __future__ import print_function
import numpy as np
from astropy.io import fits
import os
import glob
import json
import matplotlib.pyplot as plt
import pandas as pd
import StringIO
from astropy.table import Table
import seaborn as sns
import sys
from scipy.optimize import fsolve

def findIntersection(m, y, m1, y1, x0):
    x = np.linspace(-10.0, 15.5, 200)
    return fsolve(lambda x : (m*x + y) - (m1*x + y1), x0)

tab_np = Table.read("PNe-candidates-splus_dr1-marz18.tab", format="ascii.tab")
tab_sym = Table.read("SyTs-candidates-splus_dr1.tab", format="ascii.tab")

#Field and number of the objects
number_np = tab_np['Id']
Field_np = tab_np['Field']

number_sym = tab_sym['Id']
Field_sym = tab_sym['Field']

#####################################################################
# Aperture ###########################################################
######################################################################
#Color
x1_np_aper = tab_np['F0515_aper'] - tab_np['F0861_aper']
y1_np_aper = tab_np['F0515_aper'] - tab_np['F0660_aper']

x1_sym_aper = tab_sym['F0515_aper'] - tab_sym['F0861_aper']
y1_sym_aper = tab_sym['F0515_aper'] - tab_sym['F0660_aper']
    
#Color
x2_np_aper = tab_np['Z_aper'] - tab_np['G_aper']
y2_np_aper = tab_np['Z_aper'] - tab_np['F0660_aper']

x2_sym_aper = tab_sym['Z_aper'] - tab_sym['G_aper']
y2_sym_aper = tab_sym['Z_aper'] - tab_sym['F0660_aper']

#Color
x3_np_aper = tab_np['F0660_aper'] - tab_np['R_aper']
y3_np_aper = tab_np['F0660_aper'] - tab_np['G_aper']

x3_sym_aper = tab_sym['F0660_aper'] - tab_sym['R_aper']
y3_sym_aper = tab_sym['F0660_aper'] - tab_sym['G_aper']

#Color
x4_np_aper = tab_np['F0660_aper'] - tab_np['R_aper']
y4_np_aper = tab_np['G_aper'] - tab_np['F0515_aper']

x4_sym_aper = tab_sym['F0660_aper'] - tab_sym['R_aper']
y4_sym_aper = tab_sym['G_aper'] - tab_sym['F0515_aper']
    
#Color
x5_np_aper = tab_np['G_aper'] - tab_np['I_aper']
y5_np_aper = tab_np['F0410_aper'] - tab_np['F0660_aper']

x5_sym_aper = tab_sym['G_aper'] - tab_sym['I_aper']
y5_sym_aper = tab_sym['F0410_aper'] - tab_sym['F0660_aper']

#Color
x6_np_aper = tab_np['R_aper'] - tab_np['I_aper']
y6_np_aper = tab_np['R_aper'] - tab_np['F0660_aper']

x6_sym_aper = tab_sym['R_aper'] - tab_sym['I_aper']
y6_sym_aper = tab_sym['R_aper'] - tab_sym['F0660_aper']

################################################################################################
# Petro         ################################################################################
################################################################################################
#Color
x1_np_petro = tab_np['F0515_petro'] - tab_np['F0861_petro']
y1_np_petro = tab_np['F0515_petro'] - tab_np['F0660_petro']

x1_sym_petro = tab_sym['F0515_petro'] - tab_sym['F0861_petro']
y1_sym_petro = tab_sym['F0515_petro'] - tab_sym['F0660_petro']
    
#Color
x2_np_petro = tab_np['Z_petro'] - tab_np['G_petro']
y2_np_petro = tab_np['Z_petro'] - tab_np['F0660_petro']

x2_sym_petro = tab_sym['Z_petro'] - tab_sym['G_petro']
y2_sym_petro = tab_sym['Z_petro'] - tab_sym['F0660_petro']

#Color
x3_np_petro = tab_np['F0660_petro'] - tab_np['R_petro']
y3_np_petro = tab_np['F0660_petro'] - tab_np['G_petro']

x3_sym_petro = tab_sym['F0660_petro'] - tab_sym['R_petro']
y3_sym_petro = tab_sym['F0660_petro'] - tab_sym['G_petro']

#Color
x4_np_petro = tab_np['F0660_petro'] - tab_np['R_petro']
y4_np_petro = tab_np['G_petro'] - tab_np['F0515_petro']

x4_sym_petro = tab_sym['F0660_petro'] - tab_sym['R_petro']
y4_sym_petro = tab_sym['G_petro'] - tab_sym['F0515_petro']
    
#Color
x5_np_petro = tab_np['G_petro'] - tab_np['I_petro']
y5_np_petro = tab_np['F0410_petro'] - tab_np['F0660_petro']

x5_sym_petro = tab_sym['G_petro'] - tab_sym['I_petro']
y5_sym_petro = tab_sym['F0410_petro'] - tab_sym['F0660_petro']

#Color
x6_np_petro = tab_np['R_petro'] - tab_np['I_petro']
y6_np_petro = tab_np['R_petro'] - tab_np['F0660_petro']

x6_sym_petro = tab_sym['R_petro'] - tab_sym['I_petro']
y6_sym_petro = tab_sym['R_petro'] - tab_sym['F0660_petro']

####################################################################################3
#     Auto       #################################################################
#######################################################################################
#Color
x1_np_auto = tab_np['F0515_auto'] - tab_np['F0861_auto']
y1_np_auto = tab_np['F0515_auto'] - tab_np['F0660_auto']

x1_sym_auto = tab_sym['F0515_auto'] - tab_sym['F0861_auto']
y1_sym_auto = tab_sym['F0515_auto'] - tab_sym['F0660_auto']
    
#Color
x2_np_auto = tab_np['Z_auto'] - tab_np['G_auto']
y2_np_auto = tab_np['Z_auto'] - tab_np['F0660_auto']

x2_sym_auto = tab_sym['Z_auto'] - tab_sym['G_auto']
y2_sym_auto = tab_sym['Z_auto'] - tab_sym['F0660_auto']

#Color
x3_np_auto = tab_np['F0660_auto'] - tab_np['R_auto']
y3_np_auto = tab_np['F0660_auto'] - tab_np['G_auto']

x3_sym_auto = tab_sym['F0660_auto'] - tab_sym['R_auto']
y3_sym_auto = tab_sym['F0660_auto'] - tab_sym['G_auto']

#Color
x4_np_auto = tab_np['F0660_auto'] - tab_np['R_auto']
y4_np_auto = tab_np['G_auto'] - tab_np['F0515_auto']

x4_sym_auto = tab_sym['F0660_auto'] - tab_sym['R_auto']
y4_sym_auto = tab_sym['G_auto'] - tab_sym['F0515_auto']
    
#Color
x5_np_auto = tab_np['G_auto'] - tab_np['I_auto']
y5_np_auto = tab_np['F0410_auto'] - tab_np['F0660_auto']

x5_sym_auto = tab_sym['G_auto'] - tab_sym['I_auto']
y5_sym_auto = tab_sym['F0410_auto'] - tab_sym['F0660_auto']

#Color
x6_np_auto = tab_np['R_auto'] - tab_np['I_auto']
y6_np_auto = tab_np['R_auto'] - tab_np['F0660_auto']

x6_sym_auto = tab_sym['R_auto'] - tab_sym['I_auto']
y6_sym_auto = tab_sym['R_auto'] - tab_sym['F0660_auto']

##################################################################################################################################333
lgd_kws = {'frameon': True, 'fancybox': True, 'shadow': True}
#sns.set(style="dark")#, context="talk")
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
ax1.scatter(x1_np, y1_np, c='blue', alpha=0.8, marker ='o', s=70, label='S-PLUS PN1')
ax1.scatter(x1_sym, y1_sym, c='r', alpha=0.8, marker ='s', s=70, label='S-PLUS SySt')

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

# Region of the simbiotic stars
result1 = findIntersection(5.5, -6.45, 0.98, -0.16, 0.0)
x_new_s = np.linspace(result1, 15.5, 200)
x_new2_s = np.linspace(result1, 15.5, 200)
y_s = 5.5*x_new_s - 6.45
yy_s = 0.98*x_new2_s - 0.16

ax1.plot(x_new_s, y_s, color='r', linestyle='--')
ax1.plot(x_new2_s, yy_s , color='r', linestyle='--')

# ax1.fill_between(x_new2, y, yy)
# ax1.fill(y, yy)

for label_, x, y in zip(number_np, x1_np, y1_np):
    ax1.annotate(label_, (x, y), alpha=0.9, size=8,
                   xytext=(3, 5), textcoords='offset points', ha='left', va='bottom',)
for label_, x, y in zip(Field_np, x1_np, y1_np):
    ax1.annotate(label_, (x, y), alpha=0.9, size=8,
                 xytext=(-18, -15), textcoords='offset points', ha='left', va='bottom',)
plt.text(0.05, 0.90, 'Zone HPNe',
         transform=ax1.transAxes, fontsize='small')
#Symbiotics
for label_, x, y in zip(number_np, x1_np, y1_np):
    ax1.annotate(label_, (x, y), alpha=0.9, size=8,
                   xytext=(3, 5), textcoords='offset points', ha='left', va='bottom',)
for label_, x, y in zip(Field_np, x1_np, y1_np):
    ax1.annotate(label_, (x, y), alpha=0.9, size=8,
                 xytext=(-18, -15), textcoords='offset points', ha='left', va='bottom',)
plt.text(0.05, 0.90, 'Zone HPNe',
         transform=ax1.transAxes, fontsize='small')

ax1.minorticks_on()
#ax1.grid(which='minor')#, lw=0.3)
ax1.legend(scatterpoints=1, **lgd_kws)
ax1.grid()
#sns.despine(bottom=True)
plt.tight_layout()
plt.savefig('Fig1-EDR-SPLUS-J0515-J0861-all.pdf')
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
ax2.scatter(x2_np, y2_np, c='blue', alpha=0.8, marker ='o', s=70, label='S-PLUS PN1')#,  s=55, label='Halpha emitters')
ax2.scatter(x2_sym, y2_sym, c='r', alpha=0.8, marker ='s', s=70, label='S-PLUS SySt')
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

# Region of the simbiotic stars=>
result1 = findIntersection(-1.96, -3.15, 0.2, 0.44, 0.0)
x_new_s = np.linspace(-15.5, result1, 200)
x_new2_s = np.linspace(-15.5, result1, 200)
y_s = -1.96*x_new_s - 3.15
yy_s = 0.2*x_new2_s + 0.44
ax2.plot(x_new_s, y_s, color='r', linestyle='--')
ax2.plot(x_new2_s, yy_s , color='r', linestyle='--')

# ax2.plot(X, 0.2319*X + 0.85, color='k', linestyle='-')
# ax2.plot(X, -1.3*X + 1.7, color='k', linestyle='-')
for label_, x, y in zip(number_np, x2_np, y2_np):
    ax2.annotate(label_, (x, y), alpha=0.9, size=8,
                   xytext=(3, 5), textcoords='offset points', ha='left', va='bottom',)
for label_, x, y in zip(Field_np, x2_np, y2_np):
    ax2.annotate(label_, (x, y), alpha=0.9, size=8,
                 xytext=(-18, -15), textcoords='offset points', ha='left', va='bottom',)

plt.text(0.8, 0.9, 'Zone HPNe',
         transform=ax2.transAxes, fontsize='small')

ax2.minorticks_on()
#ax1.grid(which='minor')#, lw=0.3)
ax2.legend(scatterpoints=1, loc="upper left", **lgd_kws)
ax2.grid()
#sns.despine(bottom=True)
plt.tight_layout()
plt.savefig('Fig2-EDR-SPLUS-zSDSS-gSDSS-all.pdf')
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
ax4.scatter(x3_np, y3_np, c='blue', alpha=0.8, marker ='o', s=70, label='S-PLUS PN1')#, label='Halpha emitters')
ax4.scatter(x3_sym, y3_sym, c='r', alpha=0.8, marker ='s', s=70, label='S-PLUS SySt')
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
for label_, x, y in zip(number_np, x3_np, y3_np):
    ax4.annotate(label_, (x, y), alpha=0.9, size=8,
                   xytext=(3, 5), textcoords='offset points', ha='left', va='bottom',)
for label_, x, y in zip(Field_np, x3_np, y3_np):
    ax4.annotate(label_, (x, y), alpha=0.9, size=8,
                 xytext=(-18, -15), textcoords='offset points', ha='left', va='bottom',)
plt.text(0.05, 0.90, 'Zone HPNe',
         transform=ax4.transAxes, fontsize='small')

ax4.minorticks_on()
#ax1.grid(which='minor')#, lw=0.3)
ax4.legend(scatterpoints=1, **lgd_kws)
ax4.grid()
#sns.despine(bottom=True)
plt.tight_layout()
plt.savefig('Fig3-EDR-SPLUS-J0660-rSDSS-all.pdf')
plt.clf()

###################################################################################
#gSDSS - J0515 vs J0660 - rSDSS ###################################################
###################################################################################
lgd_kws = {'frameon': True, 'fancybox': True, 'shadow': True}
#sns.set(style="dark")#, context="talk")
sns.set_style('ticks')       
fig = plt.figure(figsize=(7, 6))
ax5 = fig.add_subplot(111)
ax5.set_xlim(xmin=-2.7,xmax=0.8)
ax5.set_ylim(ymin=-2.0,ymax=1.5)
plt.tick_params(axis='x', labelsize=20)
plt.tick_params(axis='y', labelsize=20)
plt.xlabel('$J0660 - rSDSS$', size =20)
plt.ylabel('$gSDSS - J0515$', size =20)
#ax4.scatter(r_i00, r_ha00, c='green', alpha=0.8, marker ='.',  s=35, label='All sources')
ax5.scatter(x4_np, y4_np, c='blue', alpha=0.8, marker ='o', s=70, label='S-PLUS PN1')#, label='Halpha emitters')
ax5.scatter(x4_sym, y4_sym, c='red', alpha=0.8, marker ='s', s=70, label='S-PLUS SySt')
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

# Region of the simbiotic stars
result1 = findIntersection(-0.19, -0.05, -2.66, -2.2, 0.0)
x_new_s = np.linspace(-15.5, result1, 200)
x_new2_s = np.linspace(-15.0, result1, 200)
y_s = -0.19*x_new_s - 0.05
yy_s = -2.66*x_new2_s - 2.2

ax5.plot(x_new_s, y_s, color='r', linestyle='--')
ax5.plot(x_new2_s, yy_s , color='r', linestyle='--')


# ax5.plot(X, 0.12*X - 0.01, color='k', linestyle='-' )
# ax5.plot(X, -1.1*X - 1.07, color='k', linestyle='-' )

for label_, x, y in zip(number_np, x4_np, y4_np):
    ax5.annotate(label_, (x, y), alpha=0.9, size=8,
                   xytext=(3, 5), textcoords='offset points', ha='left', va='bottom',)
for label_, x, y in zip(Field_np, x4_np, y4_np):
    ax5.annotate(label_, (x, y), alpha=0.9, size=8,
                 xytext=(-18, -15), textcoords='offset points', ha='left', va='bottom',)

# for label_, x, y in zip(number_sym, x4_sym, y4_sym):
#     ax5.annotate(label_, (x, y), alpha=0.9, size=8,
#                    xytext=(3, 5), textcoords='offset points', ha='left', va='bottom',)
# for label_, x, y in zip(Field_sym, x4_np, y4_sym):
#     ax5.annotate(label_, (x, y), alpha=0.9, size=8,
#                  xytext=(-18, -15), textcoords='offset points', ha='left', va='bottom',)

plt.text(0.05, 0.4, 'Zone HPNe',
         transform=ax5.transAxes, fontsize='small')
ax5.minorticks_on()
#ax1.grid(which='minor')#, lw=0.3)
ax5.legend(scatterpoints=1, **lgd_kws)
ax5.grid()
#sns.despine(bottom=True)
plt.tight_layout()
plt.savefig('Fig4-EDR-SPLUS-J0660-rSDSS-all.pdf')
plt.clf()

###################################################################################
#J0410 vs J0660 - J0660 ###########################################################
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
ax6.scatter(x5_np, y5_np, c='blue', alpha=0.8, marker ='o', s=70, label='S-PLUS PN1')
ax6.scatter(x5_sym, y5_sym, c='r', alpha=0.8, marker ='s', s=70, label='S-PLUS S-PLUS SySt')

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

# Region of the simbiotic stars
result1 = findIntersection(-4.7, +10.60, 1.39, -0.04, 0.0)
x_new_s = np.linspace(-15.5, result1, 200)
x_new2_s = np.linspace(result1, 15.5, 200)
y_s = -4.7*x_new_s + 10.60
yy_s = 2.13*x_new2_s - 1.43

ax6.plot(x_new_s, y_s, color='r', linestyle='--')
ax6.plot(x_new2_s, yy_s , color='r', linestyle='--')


# ax6.plot(X, 8.0*X + 4.50, color='k', linestyle='-')
# ax6.plot(X, 0.8*X + 0.55, color='k', linestyle='-')

for label_, x, y in zip(number_np, x5_np, y5_np):
    ax6.annotate(label_, (x, y), alpha=0.9, size=8,
                   xytext=(3, 5), textcoords='offset points', ha='left', va='bottom',)
for label_, x, y in zip(Field_np, x5_np, y5_np):
    ax6.annotate(label_, (x, y), alpha=0.9, size=8,
                 xytext=(-18, -15), textcoords='offset points', ha='left', va='bottom',)

plt.text(0.05, 0.90, 'Zone HPNe',
         transform=ax6.transAxes, fontsize='small')
ax6.minorticks_on()
#ax1.grid(which='minor')#, lw=0.3)
ax6.legend(scatterpoints=1, **lgd_kws)
ax6.grid()
#sns.despine(bottom=True)
plt.tight_layout()
plt.savefig('Fig5-EDR-SPLUS-gSDSS-iSDSS-all.pdf')
plt.clf()

#############################################################################################################
#Vironen                       ##############################################################################
#############################################################################################################
lgd_kws = {'frameon': True, 'fancybox': True, 'shadow': True}
#sns.set(style="dark")#, context="talk")
sns.set_style('ticks')       
fig = plt.figure(figsize=(7, 6))
ax7 = fig.add_subplot(111)
ax7.set_xlim(xmin=-3.0,xmax=5.0)
ax7.set_ylim(ymin=-2.0,ymax=6.0)
plt.tick_params(axis='x', labelsize=20)
plt.tick_params(axis='y', labelsize=20)
plt.xlabel('$gSDSS - iSDSS$', size =20)
plt.ylabel('$J0410 - J0660$', size =20)
#ax4.scatter(r_i00, r_ha00, c='green', alpha=0.8, marker ='.',  s=35, label='All sources')
ax7.scatter(x6_np, y6_np, c='blue', alpha=0.8, marker ='o', s=70, label='S-PLUS PN1')
ax7.scatter(x6_sym, y6_sym, c='red', alpha=0.8, marker ='s', s=70, label='S-PLUS SySt')

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
ax7.plot(x_new, y, color='k', linestyle='-')
ax7.plot(x_new2, yy , color='k', linestyle='-')

#Viironen
x_new4 = np.linspace(-10.0, 11.1, 200)
y_v =  0.25*x_new4 + 1.9
ax7.plot(x_new4, y_v, color='k', linestyle='--')

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

for label_, x, y in zip(number_np, x6_np, y6_np):
    ax7.annotate(label_, (x, y), alpha=0.9, size=8,
                   xytext=(3, 5), textcoords='offset points', ha='left', va='bottom',)
for label_, x, y in zip(Field_np, x6_np, y6_np):
    ax7.annotate(label_, (x, y), alpha=0.9, size=8,
                 xytext=(-18, -15), textcoords='offset points', ha='left', va='bottom',)

plt.text(0.05, 0.90, 'Zone HPNe',
         transform=ax7.transAxes, fontsize='small')
ax7.minorticks_on()
#ax1.grid(which='minor')#, lw=0.3)
ax7.legend(scatterpoints=1, **lgd_kws)
ax7.grid()
#sns.despine(bottom=True)
plt.tight_layout()
plt.savefig('Fig6-EDR-SPLUS-vironen-all.pdf')
plt.clf()

###########################################################################################################################
lgd_kws = {'frameon': True, 'fancybox': True, 'shadow': True}
#sns.set(style="dark")#, context="talk")
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
ax1.scatter(x1_np, y1_np, c='blue', alpha=0.8, marker ='o', s=70, label='S-PLUS PN1')
ax1.scatter(x1_sym, y1_sym, c='r', alpha=0.8, marker ='s', s=70, label='S-PLUS SySt')

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

# Region of the simbiotic stars
result1 = findIntersection(5.5, -6.45, 0.98, -0.16, 0.0)
x_new_s = np.linspace(result1, 15.5, 200)
x_new2_s = np.linspace(result1, 15.5, 200)
y_s = 5.5*x_new_s - 6.45
yy_s = 0.98*x_new2_s - 0.16

ax1.plot(x_new_s, y_s, color='r', linestyle='--')
ax1.plot(x_new2_s, yy_s , color='r', linestyle='--')

# ax1.fill_between(x_new2, y, yy)
# ax1.fill(y, yy)

for label_, x, y in zip(number_np, x1_np, y1_np):
    ax1.annotate(label_, (x, y), alpha=0.9, size=8,
                   xytext=(3, 5), textcoords='offset points', ha='left', va='bottom',)
for label_, x, y in zip(Field_np, x1_np, y1_np):
    ax1.annotate(label_, (x, y), alpha=0.9, size=8,
                 xytext=(-18, -15), textcoords='offset points', ha='left', va='bottom',)
plt.text(0.05, 0.90, 'Zone HPNe',
         transform=ax1.transAxes, fontsize='small')
#Symbiotics
for label_, x, y in zip(number_np, x1_np, y1_np):
    ax1.annotate(label_, (x, y), alpha=0.9, size=8,
                   xytext=(3, 5), textcoords='offset points', ha='left', va='bottom',)
for label_, x, y in zip(Field_np, x1_np, y1_np):
    ax1.annotate(label_, (x, y), alpha=0.9, size=8,
                 xytext=(-18, -15), textcoords='offset points', ha='left', va='bottom',)
plt.text(0.05, 0.90, 'Zone HPNe',
         transform=ax1.transAxes, fontsize='small')

ax1.minorticks_on()
#ax1.grid(which='minor')#, lw=0.3)
ax1.legend(scatterpoints=1, **lgd_kws)
ax1.grid()
#sns.despine(bottom=True)
plt.tight_layout()
plt.savefig('Fig1-EDR-SPLUS-J0515-J0861-all.pdf')
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
ax2.scatter(x2_np, y2_np, c='blue', alpha=0.8, marker ='o', s=70, label='S-PLUS PN1')#,  s=55, label='Halpha emitters')
ax2.scatter(x2_sym, y2_sym, c='r', alpha=0.8, marker ='s', s=70, label='S-PLUS SySt')
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

# Region of the simbiotic stars=>
result1 = findIntersection(-1.96, -3.15, 0.2, 0.44, 0.0)
x_new_s = np.linspace(-15.5, result1, 200)
x_new2_s = np.linspace(-15.5, result1, 200)
y_s = -1.96*x_new_s - 3.15
yy_s = 0.2*x_new2_s + 0.44
ax2.plot(x_new_s, y_s, color='r', linestyle='--')
ax2.plot(x_new2_s, yy_s , color='r', linestyle='--')

# ax2.plot(X, 0.2319*X + 0.85, color='k', linestyle='-')
# ax2.plot(X, -1.3*X + 1.7, color='k', linestyle='-')
for label_, x, y in zip(number_np, x2_np, y2_np):
    ax2.annotate(label_, (x, y), alpha=0.9, size=8,
                   xytext=(3, 5), textcoords='offset points', ha='left', va='bottom',)
for label_, x, y in zip(Field_np, x2_np, y2_np):
    ax2.annotate(label_, (x, y), alpha=0.9, size=8,
                 xytext=(-18, -15), textcoords='offset points', ha='left', va='bottom',)

plt.text(0.8, 0.9, 'Zone HPNe',
         transform=ax2.transAxes, fontsize='small')

ax2.minorticks_on()
#ax1.grid(which='minor')#, lw=0.3)
ax2.legend(scatterpoints=1, loc="upper left", **lgd_kws)
ax2.grid()
#sns.despine(bottom=True)
plt.tight_layout()
plt.savefig('Fig2-EDR-SPLUS-zSDSS-gSDSS-all.pdf')
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
ax4.scatter(x3_np, y3_np, c='blue', alpha=0.8, marker ='o', s=70, label='S-PLUS PN1')#, label='Halpha emitters')
ax4.scatter(x3_sym, y3_sym, c='r', alpha=0.8, marker ='s', s=70, label='S-PLUS SySt')
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
for label_, x, y in zip(number_np, x3_np, y3_np):
    ax4.annotate(label_, (x, y), alpha=0.9, size=8,
                   xytext=(3, 5), textcoords='offset points', ha='left', va='bottom',)
for label_, x, y in zip(Field_np, x3_np, y3_np):
    ax4.annotate(label_, (x, y), alpha=0.9, size=8,
                 xytext=(-18, -15), textcoords='offset points', ha='left', va='bottom',)
plt.text(0.05, 0.90, 'Zone HPNe',
         transform=ax4.transAxes, fontsize='small')

ax4.minorticks_on()
#ax1.grid(which='minor')#, lw=0.3)
ax4.legend(scatterpoints=1, **lgd_kws)
ax4.grid()
#sns.despine(bottom=True)
plt.tight_layout()
plt.savefig('Fig3-EDR-SPLUS-J0660-rSDSS-all.pdf')
plt.clf()

###################################################################################
#gSDSS - J0515 vs J0660 - rSDSS ###################################################
###################################################################################
lgd_kws = {'frameon': True, 'fancybox': True, 'shadow': True}
#sns.set(style="dark")#, context="talk")
sns.set_style('ticks')       
fig = plt.figure(figsize=(7, 6))
ax5 = fig.add_subplot(111)
ax5.set_xlim(xmin=-2.7,xmax=0.8)
ax5.set_ylim(ymin=-2.0,ymax=1.5)
plt.tick_params(axis='x', labelsize=20)
plt.tick_params(axis='y', labelsize=20)
plt.xlabel('$J0660 - rSDSS$', size =20)
plt.ylabel('$gSDSS - J0515$', size =20)
#ax4.scatter(r_i00, r_ha00, c='green', alpha=0.8, marker ='.',  s=35, label='All sources')
ax5.scatter(x4_np, y4_np, c='blue', alpha=0.8, marker ='o', s=70, label='S-PLUS PN1')#, label='Halpha emitters')
ax5.scatter(x4_sym, y4_sym, c='red', alpha=0.8, marker ='s', s=70, label='S-PLUS SySt')
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

# Region of the simbiotic stars
result1 = findIntersection(-0.19, -0.05, -2.66, -2.2, 0.0)
x_new_s = np.linspace(-15.5, result1, 200)
x_new2_s = np.linspace(-15.0, result1, 200)
y_s = -0.19*x_new_s - 0.05
yy_s = -2.66*x_new2_s - 2.2

ax5.plot(x_new_s, y_s, color='r', linestyle='--')
ax5.plot(x_new2_s, yy_s , color='r', linestyle='--')


# ax5.plot(X, 0.12*X - 0.01, color='k', linestyle='-' )
# ax5.plot(X, -1.1*X - 1.07, color='k', linestyle='-' )

for label_, x, y in zip(number_np, x4_np, y4_np):
    ax5.annotate(label_, (x, y), alpha=0.9, size=8,
                   xytext=(3, 5), textcoords='offset points', ha='left', va='bottom',)
for label_, x, y in zip(Field_np, x4_np, y4_np):
    ax5.annotate(label_, (x, y), alpha=0.9, size=8,
                 xytext=(-18, -15), textcoords='offset points', ha='left', va='bottom',)

# for label_, x, y in zip(number_sym, x4_sym, y4_sym):
#     ax5.annotate(label_, (x, y), alpha=0.9, size=8,
#                    xytext=(3, 5), textcoords='offset points', ha='left', va='bottom',)
# for label_, x, y in zip(Field_sym, x4_np, y4_sym):
#     ax5.annotate(label_, (x, y), alpha=0.9, size=8,
#                  xytext=(-18, -15), textcoords='offset points', ha='left', va='bottom',)

plt.text(0.05, 0.4, 'Zone HPNe',
         transform=ax5.transAxes, fontsize='small')
ax5.minorticks_on()
#ax1.grid(which='minor')#, lw=0.3)
ax5.legend(scatterpoints=1, **lgd_kws)
ax5.grid()
#sns.despine(bottom=True)
plt.tight_layout()
plt.savefig('Fig4-EDR-SPLUS-J0660-rSDSS-all.pdf')
plt.clf()

###################################################################################
#J0410 vs J0660 - J0660 ###########################################################
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
ax6.scatter(x5_np, y5_np, c='blue', alpha=0.8, marker ='o', s=70, label='S-PLUS PN1')
ax6.scatter(x5_sym, y5_sym, c='r', alpha=0.8, marker ='s', s=70, label='S-PLUS S-PLUS SySt')

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

# Region of the simbiotic stars
result1 = findIntersection(-4.7, +10.60, 1.39, -0.04, 0.0)
x_new_s = np.linspace(-15.5, result1, 200)
x_new2_s = np.linspace(result1, 15.5, 200)
y_s = -4.7*x_new_s + 10.60
yy_s = 2.13*x_new2_s - 1.43

ax6.plot(x_new_s, y_s, color='r', linestyle='--')
ax6.plot(x_new2_s, yy_s , color='r', linestyle='--')


# ax6.plot(X, 8.0*X + 4.50, color='k', linestyle='-')
# ax6.plot(X, 0.8*X + 0.55, color='k', linestyle='-')

for label_, x, y in zip(number_np, x5_np, y5_np):
    ax6.annotate(label_, (x, y), alpha=0.9, size=8,
                   xytext=(3, 5), textcoords='offset points', ha='left', va='bottom',)
for label_, x, y in zip(Field_np, x5_np, y5_np):
    ax6.annotate(label_, (x, y), alpha=0.9, size=8,
                 xytext=(-18, -15), textcoords='offset points', ha='left', va='bottom',)

plt.text(0.05, 0.90, 'Zone HPNe',
         transform=ax6.transAxes, fontsize='small')
ax6.minorticks_on()
#ax1.grid(which='minor')#, lw=0.3)
ax6.legend(scatterpoints=1, **lgd_kws)
ax6.grid()
#sns.despine(bottom=True)
plt.tight_layout()
plt.savefig('Fig5-EDR-SPLUS-gSDSS-iSDSS-all.pdf')
plt.clf()

#############################################################################################################
#Vironen                       ##############################################################################
#############################################################################################################
lgd_kws = {'frameon': True, 'fancybox': True, 'shadow': True}
#sns.set(style="dark")#, context="talk")
sns.set_style('ticks')       
fig = plt.figure(figsize=(7, 6))
ax7 = fig.add_subplot(111)
ax7.set_xlim(xmin=-3.0,xmax=5.0)
ax7.set_ylim(ymin=-2.0,ymax=6.0)
plt.tick_params(axis='x', labelsize=20)
plt.tick_params(axis='y', labelsize=20)
plt.xlabel('$gSDSS - iSDSS$', size =20)
plt.ylabel('$J0410 - J0660$', size =20)
#ax4.scatter(r_i00, r_ha00, c='green', alpha=0.8, marker ='.',  s=35, label='All sources')
ax7.scatter(x6_np, y6_np, c='blue', alpha=0.8, marker ='o', s=70, label='S-PLUS PN1')
ax7.scatter(x6_sym, y6_sym, c='red', alpha=0.8, marker ='s', s=70, label='S-PLUS SySt')

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
ax7.plot(x_new, y, color='k', linestyle='-')
ax7.plot(x_new2, yy , color='k', linestyle='-')

#Viironen
x_new4 = np.linspace(-10.0, 11.1, 200)
y_v =  0.25*x_new4 + 1.9
ax7.plot(x_new4, y_v, color='k', linestyle='--')

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

for label_, x, y in zip(number_np, x6_np, y6_np):
    ax7.annotate(label_, (x, y), alpha=0.9, size=8,
                   xytext=(3, 5), textcoords='offset points', ha='left', va='bottom',)
for label_, x, y in zip(Field_np, x6_np, y6_np):
    ax7.annotate(label_, (x, y), alpha=0.9, size=8,
                 xytext=(-18, -15), textcoords='offset points', ha='left', va='bottom',)

plt.text(0.05, 0.90, 'Zone HPNe',
         transform=ax7.transAxes, fontsize='small')
ax7.minorticks_on()
#ax1.grid(which='minor')#, lw=0.3)
ax7.legend(scatterpoints=1, **lgd_kws)
ax7.grid()
#sns.despine(bottom=True)
plt.tight_layout()
plt.savefig('Fig6-EDR-SPLUS-vironen-all.pdf')
plt.clf()

###############################################################################################################################3
lgd_kws = {'frameon': True, 'fancybox': True, 'shadow': True}
#sns.set(style="dark")#, context="talk")
sns.set_style('ticks')       
fig = plt.figure(figsize=(7, 6))
ax8 = fig.add_subplot(111)
ax8.set_xlim(xmin=-2.5,xmax=5.5)
ax8.set_ylim(ymin=-2.0,ymax=5.0)
plt.tick_params(axis='x', labelsize=20)
plt.tick_params(axis='y', labelsize=20)
plt.xlabel('$J0515 - J0861$', size = 20)
plt.ylabel('$J0515 - J0660$', size = 20)
#ax4.scatter(r_i00, r_ha00, c='green', alpha=0.8, marker ='.',  s=35, label='All sources')
ax8.scatter(x1_np, y1_np, c='blue', alpha=0.8, marker ='o', s=70, label='S-PLUS PN1')
ax8.scatter(x1_sym, y1_sym, c='r', alpha=0.8, marker ='s', s=70, label='S-PLUS SySt')

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
ax8.plot(x_new, y, color='k', linestyle='-')
ax8.plot(x_new2, yy , color='k', linestyle='-')

# Region of the simbiotic stars
result1 = findIntersection(5.5, -6.45, 0.98, -0.16, 0.0)
x_new_s = np.linspace(result1, 15.5, 200)
x_new2_s = np.linspace(result1, 15.5, 200)
y_s = 5.5*x_new_s - 6.45
yy_s = 0.98*x_new2_s - 0.16

ax8.plot(x_new_s, y_s, color='r', linestyle='--')
ax8.plot(x_new2_s, yy_s , color='r', linestyle='--')

# ax1.fill_between(x_new2, y, yy)
# ax1.fill(y, yy)

for label_, x, y in zip(number_np, x1_np, y1_np):
    ax8.annotate(label_, (x, y), alpha=0.9, size=8,
                   xytext=(3, 5), textcoords='offset points', ha='left', va='bottom',)
for label_, x, y in zip(Field_np, x1_np, y1_np):
    ax8.annotate(label_, (x, y), alpha=0.9, size=8,
                 xytext=(-18, -15), textcoords='offset points', ha='left', va='bottom',)
plt.text(0.05, 0.90, 'Zone HPNe',
         transform=ax1.transAxes, fontsize='small')
#Symbiotics
for label_, x, y in zip(number_np, x1_np, y1_np):
    ax8.annotate(label_, (x, y), alpha=0.9, size=8,
                   xytext=(3, 5), textcoords='offset points', ha='left', va='bottom',)
for label_, x, y in zip(Field_np, x1_np, y1_np):
    ax8.annotate(label_, (x, y), alpha=0.9, size=8,
                 xytext=(-18, -15), textcoords='offset points', ha='left', va='bottom',)
plt.text(0.05, 0.90, 'Zone HPNe',
         transform=ax1.transAxes, fontsize='small')

ax8.minorticks_on()
#ax1.grid(which='minor')#, lw=0.3)
ax8.legend(scatterpoints=1, **lgd_kws)
ax8.grid()
#sns.despine(bottom=True)
plt.tight_layout()
plt.savefig('Fig1-EDR-SPLUS-J0515-J0861-all.pdf')
plt.clf()
#############################################################################
#z - J0660 v z - g ##########################################################
###############################################################################

lgd_kws = {'frameon': True, 'fancybox': True, 'shadow': True}
#sns.set(style="dark")#, context="talk")
sns.set_style('ticks')       
fig = plt.figure(figsize=(7, 6))
ax9 = fig.add_subplot(111)
ax9.set_xlim(xmin=-5.8,xmax=2.5)
ax9.set_ylim(ymin=-3.0,ymax=5.0)
plt.tick_params(axis='x', labelsize=20)
plt.tick_params(axis='y', labelsize=20)
plt.xlabel('$zSDSS - gSDSS$', size =20)
plt.ylabel('$zSDSS - J0660$', size =20)
#ax4.scatter(r_i00, r_ha00, c='green', alpha=0.8, marker ='.',  s=35, label='All sources')
ax9.scatter(x9_np, y2_np, c='blue', alpha=0.8, marker ='o', s=70, label='S-PLUS PN1')#,  s=55, label='Halpha emitters')
ax9.scatter(x9_sym, y2_sym, c='r', alpha=0.8, marker ='s', s=70, label='S-PLUS SySt')
# Region where stay the PNe
result = findIntersection(0.2319, 0.85, -1.3, 1.7, 0.0)
result_y = 0.2319*result + 0.85

x_new = np.linspace(result, 15.5, 200)
x_new2 = np.linspace(-10.0, result, 200)

y = 0.2319*x_new + 0.85
yy = -1.3*x_new2 +  1.7
#Mask
#mask = y >= result_y - 0.5
ax9.plot(x_new, y, color='k', linestyle='-')
ax9.plot(x_new2, yy , color='k', linestyle='-')

# Region of the simbiotic stars=>
result1 = findIntersection(-1.96, -3.15, 0.2, 0.44, 0.0)
x_new_s = np.linspace(-15.5, result1, 200)
x_new2_s = np.linspace(-15.5, result1, 200)
y_s = -1.96*x_new_s - 3.15
yy_s = 0.2*x_new2_s + 0.44
ax9.plot(x_new_s, y_s, color='r', linestyle='--')
ax9.plot(x_new2_s, yy_s , color='r', linestyle='--')

# ax9.plot(X, 0.2319*X + 0.85, color='k', linestyle='-')
# ax9.plot(X, -1.3*X + 1.7, color='k', linestyle='-')
for label_, x, y in zip(number_np, x9_np, y2_np):
    ax9.annotate(label_, (x, y), alpha=0.9, size=8,
                   xytext=(3, 5), textcoords='offset points', ha='left', va='bottom',)
for label_, x, y in zip(Field_np, x9_np, y2_np):
    ax9.annotate(label_, (x, y), alpha=0.9, size=8,
                 xytext=(-18, -15), textcoords='offset points', ha='left', va='bottom',)

plt.text(0.8, 0.9, 'Zone HPNe',
         transform=ax9.transAxes, fontsize='small')

ax9.minorticks_on()
#ax1.grid(which='minor')#, lw=0.3)
ax9.legend(scatterpoints=1, loc="upper left", **lgd_kws)
ax9.grid()
#sns.despine(bottom=True)
plt.tight_layout()
plt.savefig('Fig2-EDR-SPLUS-zSDSS-gSDSS-all.pdf')
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
ax4.scatter(x3_np, y3_np, c='blue', alpha=0.8, marker ='o', s=70, label='S-PLUS PN1')#, label='Halpha emitters')
ax4.scatter(x3_sym, y3_sym, c='r', alpha=0.8, marker ='s', s=70, label='S-PLUS SySt')
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
for label_, x, y in zip(number_np, x3_np, y3_np):
    ax4.annotate(label_, (x, y), alpha=0.9, size=8,
                   xytext=(3, 5), textcoords='offset points', ha='left', va='bottom',)
for label_, x, y in zip(Field_np, x3_np, y3_np):
    ax4.annotate(label_, (x, y), alpha=0.9, size=8,
                 xytext=(-18, -15), textcoords='offset points', ha='left', va='bottom',)
plt.text(0.05, 0.90, 'Zone HPNe',
         transform=ax4.transAxes, fontsize='small')

ax4.minorticks_on()
#ax1.grid(which='minor')#, lw=0.3)
ax4.legend(scatterpoints=1, **lgd_kws)
ax4.grid()
#sns.despine(bottom=True)
plt.tight_layout()
plt.savefig('Fig3-EDR-SPLUS-J0660-rSDSS-all.pdf')
plt.clf()

###################################################################################
#gSDSS - J0515 vs J0660 - rSDSS ###################################################
###################################################################################
lgd_kws = {'frameon': True, 'fancybox': True, 'shadow': True}
#sns.set(style="dark")#, context="talk")
sns.set_style('ticks')       
fig = plt.figure(figsize=(7, 6))
ax5 = fig.add_subplot(111)
ax5.set_xlim(xmin=-2.7,xmax=0.8)
ax5.set_ylim(ymin=-2.0,ymax=1.5)
plt.tick_params(axis='x', labelsize=20)
plt.tick_params(axis='y', labelsize=20)
plt.xlabel('$J0660 - rSDSS$', size =20)
plt.ylabel('$gSDSS - J0515$', size =20)
#ax4.scatter(r_i00, r_ha00, c='green', alpha=0.8, marker ='.',  s=35, label='All sources')
ax5.scatter(x4_np, y4_np, c='blue', alpha=0.8, marker ='o', s=70, label='S-PLUS PN1')#, label='Halpha emitters')
ax5.scatter(x4_sym, y4_sym, c='red', alpha=0.8, marker ='s', s=70, label='S-PLUS SySt')
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

# Region of the simbiotic stars
result1 = findIntersection(-0.19, -0.05, -2.66, -2.2, 0.0)
x_new_s = np.linspace(-15.5, result1, 200)
x_new2_s = np.linspace(-15.0, result1, 200)
y_s = -0.19*x_new_s - 0.05
yy_s = -2.66*x_new2_s - 2.2

ax5.plot(x_new_s, y_s, color='r', linestyle='--')
ax5.plot(x_new2_s, yy_s , color='r', linestyle='--')


# ax5.plot(X, 0.12*X - 0.01, color='k', linestyle='-' )
# ax5.plot(X, -1.1*X - 1.07, color='k', linestyle='-' )

for label_, x, y in zip(number_np, x4_np, y4_np):
    ax5.annotate(label_, (x, y), alpha=0.9, size=8,
                   xytext=(3, 5), textcoords='offset points', ha='left', va='bottom',)
for label_, x, y in zip(Field_np, x4_np, y4_np):
    ax5.annotate(label_, (x, y), alpha=0.9, size=8,
                 xytext=(-18, -15), textcoords='offset points', ha='left', va='bottom',)

# for label_, x, y in zip(number_sym, x4_sym, y4_sym):
#     ax5.annotate(label_, (x, y), alpha=0.9, size=8,
#                    xytext=(3, 5), textcoords='offset points', ha='left', va='bottom',)
# for label_, x, y in zip(Field_sym, x4_np, y4_sym):
#     ax5.annotate(label_, (x, y), alpha=0.9, size=8,
#                  xytext=(-18, -15), textcoords='offset points', ha='left', va='bottom',)

plt.text(0.05, 0.4, 'Zone HPNe',
         transform=ax5.transAxes, fontsize='small')
ax5.minorticks_on()
#ax1.grid(which='minor')#, lw=0.3)
ax5.legend(scatterpoints=1, **lgd_kws)
ax5.grid()
#sns.despine(bottom=True)
plt.tight_layout()
plt.savefig('Fig4-EDR-SPLUS-J0660-rSDSS-all.pdf')
plt.clf()

###################################################################################
#J0410 vs J0660 - J0660 ###########################################################
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
ax6.scatter(x5_np, y5_np, c='blue', alpha=0.8, marker ='o', s=70, label='S-PLUS PN1')
ax6.scatter(x5_sym, y5_sym, c='r', alpha=0.8, marker ='s', s=70, label='S-PLUS S-PLUS SySt')

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

# Region of the simbiotic stars
result1 = findIntersection(-4.7, +10.60, 1.39, -0.04, 0.0)
x_new_s = np.linspace(-15.5, result1, 200)
x_new2_s = np.linspace(result1, 15.5, 200)
y_s = -4.7*x_new_s + 10.60
yy_s = 2.13*x_new2_s - 1.43

ax6.plot(x_new_s, y_s, color='r', linestyle='--')
ax6.plot(x_new2_s, yy_s , color='r', linestyle='--')


# ax6.plot(X, 8.0*X + 4.50, color='k', linestyle='-')
# ax6.plot(X, 0.8*X + 0.55, color='k', linestyle='-')

for label_, x, y in zip(number_np, x5_np, y5_np):
    ax6.annotate(label_, (x, y), alpha=0.9, size=8,
                   xytext=(3, 5), textcoords='offset points', ha='left', va='bottom',)
for label_, x, y in zip(Field_np, x5_np, y5_np):
    ax6.annotate(label_, (x, y), alpha=0.9, size=8,
                 xytext=(-18, -15), textcoords='offset points', ha='left', va='bottom',)

plt.text(0.05, 0.90, 'Zone HPNe',
         transform=ax6.transAxes, fontsize='small')
ax6.minorticks_on()
#ax1.grid(which='minor')#, lw=0.3)
ax6.legend(scatterpoints=1, **lgd_kws)
ax6.grid()
#sns.despine(bottom=True)
plt.tight_layout()
plt.savefig('Fig5-EDR-SPLUS-gSDSS-iSDSS-all.pdf')
plt.clf()

#############################################################################################################
#Vironen                       ##############################################################################
#############################################################################################################
lgd_kws = {'frameon': True, 'fancybox': True, 'shadow': True}
#sns.set(style="dark")#, context="talk")
sns.set_style('ticks')       
fig = plt.figure(figsize=(7, 6))
ax7 = fig.add_subplot(111)
ax7.set_xlim(xmin=-3.0,xmax=5.0)
ax7.set_ylim(ymin=-2.0,ymax=6.0)
plt.tick_params(axis='x', labelsize=20)
plt.tick_params(axis='y', labelsize=20)
plt.xlabel('$gSDSS - iSDSS$', size =20)
plt.ylabel('$J0410 - J0660$', size =20)
#ax4.scatter(r_i00, r_ha00, c='green', alpha=0.8, marker ='.',  s=35, label='All sources')
ax7.scatter(x6_np, y6_np, c='blue', alpha=0.8, marker ='o', s=70, label='S-PLUS PN1')
ax7.scatter(x6_sym, y6_sym, c='red', alpha=0.8, marker ='s', s=70, label='S-PLUS SySt')

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
ax7.plot(x_new, y, color='k', linestyle='-')
ax7.plot(x_new2, yy , color='k', linestyle='-')

#Viironen
x_new4 = np.linspace(-10.0, 11.1, 200)
y_v =  0.25*x_new4 + 1.9
ax7.plot(x_new4, y_v, color='k', linestyle='--')

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

for label_, x, y in zip(number_np, x6_np, y6_np):
    ax7.annotate(label_, (x, y), alpha=0.9, size=8,
                   xytext=(3, 5), textcoords='offset points', ha='left', va='bottom',)
for label_, x, y in zip(Field_np, x6_np, y6_np):
    ax7.annotate(label_, (x, y), alpha=0.9, size=8,
                 xytext=(-18, -15), textcoords='offset points', ha='left', va='bottom',)

plt.text(0.05, 0.90, 'Zone HPNe',
         transform=ax7.transAxes, fontsize='small')
ax7.minorticks_on()
#ax1.grid(which='minor')#, lw=0.3)
ax7.legend(scatterpoints=1, **lgd_kws)
ax7.grid()
#sns.despine(bottom=True)
plt.tight_layout()
plt.savefig('Fig6-EDR-SPLUS-vironen-all.pdf')
plt.clf()


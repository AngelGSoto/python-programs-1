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


tab = Table.read("SPLUS_STRIPE82-catalogue_edr_march2018.tab", format="ascii.tab")

shape = (len(tab['Id']), )
x = np.linspace(-10.0, 15.5, len(tab['Id']))
X = np.array(x).reshape(shape)

#filer deep splus mask
f = tab['uJAVA'] <= 21.6
f1 = tab['J0378'] <= 21.5
f2 = tab['J0395'] < 21.4
f3 = tab['J0410'] <= 21.5
f4 = tab['J0430'] < 21.4
f5 = tab['gSDSS'] <= 22.2
f6 = tab['J0515'] <= 21.4
f7 = tab['rSDSS'] <= 21.9
f8 = tab['J0660'] <= 21.3
f9 = tab['iSDSS'] <= 20.8
f10 = tab['J0861'] <= 20.8
f11 = tab['zSDSS'] <= 20.5

mask =  f3 & f5 & f6 & f7 & f8 & f9 & f10 & f11

# # #Mask 1
q = (tab['J0515'] - tab['J0660']) <= 5.0
q1 = (tab['J0515'] - tab['J0861']) >= -3.0
q2 = (tab['rSDSS'] - tab['J0660']) <= 4.0
q3 = (tab['rSDSS'] - tab['iSDSS']) >= -4.0
q4 = (tab['gSDSS'] - tab['J0515']) >= -3.2
q5 = (tab['gSDSS'] - tab['iSDSS']) >= -3.0
q6 = (tab['J0410'] - tab['J0660']) <= 6.0
q7 = (tab['zSDSS'] - tab['gSDSS']) <= 4.0

mask1 = q & q1 & q2 & q3 & q4 & q5 & q6 & q7 
#Mask
Y = 5.5*(tab['J0515'] - tab['J0861']) - 6.45
Y1 = 0.98*(tab['J0515'] - tab['J0861']) - 0.16
Y2 = -1.96*(tab['zSDSS'] - tab['gSDSS']) - 3.15
Y3 = 0.2*(tab['zSDSS'] - tab['gSDSS']) + 0.44 
Y4 = -220*(tab['rSDSS'] - tab['iSDSS']) + 40.4
Y44 = 0.39*(tab['rSDSS'] - tab['iSDSS']) + 0.73
Y5 = -4.7*(tab['gSDSS'] - tab['iSDSS']) + 10.60
Y6 = 2.13*(tab['gSDSS'] - tab['iSDSS']) - 1.43
Y7 = -0.19*(tab['J0660'] - tab['rSDSS']) - 0.05
Y8 = -2.66*(tab['J0660'] - tab['rSDSS']) - 2.2

#m = tab['Class star'] < 0.6 
m1 = tab['J0515'] - tab['J0660']<= Y
m2 = tab['J0515'] - tab['J0660']>= Y1
m3 = tab['zSDSS'] - tab['J0660']<= Y2
m4 = tab['zSDSS'] - tab['J0660']>= Y3
m5 = tab['rSDSS'] - tab['J0660']>= Y4
m6 = tab['rSDSS'] - tab['J0660']>= Y44
m7 = tab['J0410'] - tab['J0660']>= Y5
m8 = tab['J0410'] - tab['J0660']>= Y6
m9 = tab['gSDSS'] - tab['J0515']>= Y7
m10 = tab['gSDSS'] - tab['J0515']<= Y8
total_m = m1 & m2 & m3 & m4 & m5 & m6 & m7 & m8 & m9 & m10 & mask & mask1
#Field and number of the objects
number = tab['Id'][total_m]
Field = tab['Field'][total_m]

#Color
x1 = tab['J0515'][total_m] - tab['J0861'][total_m]
y1 = tab['J0515'][total_m] - tab['J0660'][total_m]
    
#Color
x2 = tab['zSDSS'][total_m] - tab['gSDSS'][total_m]
y2 = tab['zSDSS'][total_m] - tab['J0660'][total_m]

#Color
x3 = tab['J0660'][total_m] - tab['rSDSS'][total_m]
y3 = tab['J0660'][total_m] - tab['gSDSS'][total_m]

#Color
x4 = tab['J0660'][total_m] - tab['rSDSS'][total_m]
y4 = tab['gSDSS'][total_m] - tab['J0515'][total_m]
    
#Color
x5 = tab['gSDSS'][total_m] - tab['iSDSS'][total_m]
y5 = tab['J0410'][total_m] - tab['J0660'][total_m]

#Color Vironen
x6 = tab['rSDSS'][total_m] - tab['iSDSS'][total_m]
y6 = tab['rSDSS'][total_m] - tab['J0660'][total_m]
    

#Crearting the table
         
table = Table([tab["Field"][total_m], tab["Id"][total_m], tab["RA"][total_m], tab["Dec"][total_m], tab["uJAVA"][total_m], tab["J0378"][total_m], tab["J0395"][total_m], tab["J0410"][total_m], tab["J0430"][total_m], tab["gSDSS"][total_m], tab["J0515"][total_m], tab["rSDSS"][total_m], tab["J0660"][total_m], tab["iSDSS"][total_m], tab["J0861"][total_m], tab["zSDSS"][total_m], tab['Class star'][total_m]], names=("Field", "Id", "RA", "Dec", "uJAVA", "J0378", "J0395", "J0410", "J0430", "gSDSS", "J0515", "rSDSS", "J0660", "iSDSS", "J0861", "zSDSS", "Class Star"), meta={'name': 'first table'})  

#Saving resultated table

asciifile = "SySt-candidates-splus_dr1-marz18.tab"
table.write(asciifile, format="ascii.tab")

print(x1, y1)
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
ax1.scatter(x1, y1, c='blue', alpha=0.8, marker ='D', s=70, label='S-PLUS PN1')

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

for label_, x, y in zip(number, x1, y1):
    ax1.annotate(label_, (x, y), alpha=0.9, size=8,
                   xytext=(3, 5), textcoords='offset points', ha='left', va='bottom',)
for label_, x, y in zip(Field, x1, y1):
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
plt.savefig('Fig1-EDR-SPLUS-J0515-J0861-syst.pdf')
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
ax2.scatter(x2, y2, c='blue', alpha=0.8, marker ='D', s=70, label='S-PLUS PN1')#,  s=55, label='Halpha emitters')

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
for label_, x, y in zip(number, x2, y2):
    ax2.annotate(label_, (x, y), alpha=0.9, size=8,
                   xytext=(3, 5), textcoords='offset points', ha='left', va='bottom',)
for label_, x, y in zip(Field, x2, y2):
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
plt.savefig('Fig2-EDR-SPLUS-zSDSS-gSDSS-syst.pdf')
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
ax4.scatter(x3, y3, c='blue', alpha=0.8, marker ='D', s=70, label='S-PLUS PN1')#, label='Halpha emitters')

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
for label_, x, y in zip(number, x3, y3):
    ax4.annotate(label_, (x, y), alpha=0.9, size=8,
                   xytext=(3, 5), textcoords='offset points', ha='left', va='bottom',)
for label_, x, y in zip(Field, x3, y3):
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
plt.savefig('Fig3-EDR-SPLUS-J0660-rSDSS-syst.pdf')
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
ax5.scatter(x4, y4, c='blue', alpha=0.8, marker ='D', s=70, label='S-PLUS PN1')#, label='Halpha emitters')

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

for label_, x, y in zip(number, x4, y4):
    ax5.annotate(label_, (x, y), alpha=0.9, size=8,
                   xytext=(3, 5), textcoords='offset points', ha='left', va='bottom',)
for label_, x, y in zip(Field, x4, y4):
    ax5.annotate(label_, (x, y), alpha=0.9, size=8,
                 xytext=(-18, -15), textcoords='offset points', ha='left', va='bottom',)

plt.text(0.05, 0.4, 'Zone HPNe',
         transform=ax5.transAxes, fontsize='small')
ax5.minorticks_on()
#ax1.grid(which='minor')#, lw=0.3)
ax5.legend(scatterpoints=1, **lgd_kws)
ax5.grid()
#sns.despine(bottom=True)
plt.tight_layout()
plt.savefig('Fig4-EDR-SPLUS-J0660-rSDSS-syts.pdf')
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
ax6.scatter(x5, y5, c='blue', alpha=0.8, marker ='D', s=70, label='S-PLUS PN1')

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

for label_, x, y in zip(number, x5, y5):
    ax6.annotate(label_, (x, y), alpha=0.9, size=8,
                   xytext=(3, 5), textcoords='offset points', ha='left', va='bottom',)
for label_, x, y in zip(Field, x5, y5):
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
plt.savefig('Fig5-EDR-SPLUS-gSDSS-iSDSS-systs.pdf')
plt.clf()

#############################################################################################################
#Vironen
############################################################################################################
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
ax7.scatter(x6, y6, c='blue', alpha=0.8, marker ='D', s=70, label='S-PLUS PN1')

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

for label_, x, y in zip(number, x5, y5):
    ax6.annotate(label_, (x, y), alpha=0.9, size=8,
                   xytext=(3, 5), textcoords='offset points', ha='left', va='bottom',)
for label_, x, y in zip(Field, x5, y5):
    ax6.annotate(label_, (x, y), alpha=0.9, size=8,
                 xytext=(-18, -15), textcoords='offset points', ha='left', va='bottom',)

plt.text(0.05, 0.90, 'Zone HPNe',
         transform=ax6.transAxes, fontsize='small')
ax7.minorticks_on()
#ax1.grid(which='minor')#, lw=0.3)
ax7.legend(scatterpoints=1, **lgd_kws)
ax7.grid()
#sns.despine(bottom=True)
plt.tight_layout()
plt.savefig('Fig6-EDR-SPLUS-vironen-systs.pdf')
plt.clf()

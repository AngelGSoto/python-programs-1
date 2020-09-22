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

#Definition to make of plots
def plot_viironen(x, y, figfile):
    lgd_kws = {'frameon': True, 'fancybox': True, 'shadow': True}
    sns.set_style('ticks')       
    fig = plt.figure(figsize=(7, 6))
    ax = fig.add_subplot(111)
    ax.set_xlim(xmin=-3.0,xmax=3.0)
    ax.set_ylim(ymin=-0.8,ymax=2.5)
    plt.tick_params(axis='x', labelsize=20)
    plt.tick_params(axis='y', labelsize=20)
    plt.xlabel('$rSDSS - iSDSS$', size =20)
    plt.ylabel('$rSDSS - J0660$', size =20)
    ax.scatter(x, y, c='green', alpha=0.8, marker ='o', s=70, label='J-PLUS known nebulae')
    result = findIntersection(0.43, 0.65, -6.8, -1.3, 0.0)
    result_y = 8.0*result + 4.50

    x_new = np.linspace(-15.0, result, 200)
    x_new2 = np.linspace(-15.0, result, 200)
    y0 =  0.43*x_new + 0.65
    yy = -6.8*x_new2 - 1.3
    ax.plot(x_new, y0, color='k', linestyle='-')
    ax.plot(x_new2, yy , color='k', linestyle='-')

    # Region of the simbiotic stars
    result1 = findIntersection(-220, +40.4, 0.39, 0.73, 0.0)
    x_new_s = np.linspace(-15.5, result1, 200)
    x_new2_s = np.linspace(result1, 15.5, 200)
    y_s = -220*x_new_s + 40.4
    yy_s = 0.39*x_new2_s + 0.73

    ax.plot(x_new_s, y_s, color='r', linestyle='--')
    ax.plot(x_new2_s, yy_s , color='r', linestyle='--')
    for label_, x_e, y_e in zip(number, x, y):
        ax.annotate(label_, (x_e, y_e), alpha=0.9, size=8,
                   xytext=(3, 5), textcoords='offset points', ha='left', va='bottom', color='blue',)
    print(y)
    plt.text(0.05, 0.90, 'Zone HPNe',
         transform=ax.transAxes, fontsize='small')
    ax.minorticks_on()
    #ax1.grid(which='minor')#, lw=0.3)
    ax.legend(scatterpoints=1, loc="lower right", **lgd_kws)
    ax.grid()
    #sns.despine(bottom=True)
    plt.tight_layout()

    return plt.savefig(figfile)
    
    
################
############### Data
################

tab = Table.read("macht-jplusdr1_HASH-PNe.tab", format="ascii.tab")
#number
number = tab['Number']
 ################   
# colors       #
#Color vironen #
################
x_auto = tab['rSDSS_auto'] - tab['iSDSS_auto']
y_auto = tab['rSDSS_auto'] - tab['J0660_auto']

x_petro = tab['rSDSS_petro'] - tab['iSDSS_petro']
y_petro = tab['rSDSS_petro'] - tab['J0660_petro']

x_60 = tab['rSDSS_60'] - tab['iSDSS_60']
y_60 = tab['rSDSS_60'] - tab['J0660_60']

x_WORSTPSF = tab['rSDSS_WORSTPSF'] - tab['iSDSS_WORSTPSF']
y_WORSTPSF = tab['rSDSS_WORSTPSF'] - tab['J0660_WORSTPSF']

#plotting
plot_viironen(x_auto, y_auto, "Fig1-IDR-JPLUS-vironen_auto.pdf")
plot_viironen(x_petro, y_petro, "Fig1-IDR-JPLUS-vironen_petro.pdf")
plot_viironen(x_60, y_60, "Fig1-IDR-JPLUS-vironen_60.pdf")
plot_viironen(x_WORSTPSF, y_WORSTPSF, "Fig1-IDR-JPLUS-vironen_WORSTPSF.pdf")

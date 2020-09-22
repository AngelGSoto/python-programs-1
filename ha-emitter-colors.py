'''
Read the file from J-PLUS IDR table to make the colour-colour diagrams
'''
from __future__ import print_function
import numpy as np
from astropy.io import fits
import os
import glob
import json
import matplotlib.pyplot as plt
import pandas as pd
#import StringIO
from astropy.table import Table
import seaborn as sns
import sys
from scipy.optimize import fsolve

def findIntersection(m, y, m1, y1, x0):
    x = np.linspace(-10.0, 15.5, 200)
    return fsolve(lambda x : (m*x + y) - (m1*x + y1), x0)

#The equation the represent the criteria
def findIntersection(m, y, m1, y1, x0):
    x = np.linspace(-10.0, 15.5, 200)
    return fsolve(lambda x : (m*x + y) - (m1*x + y1), x0)

#Definition to make of plots
def plot_viironen(x_np, y_np, figfile):
    ''' 
    Viironen
    '''
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
    ax.scatter(x_np, y_np, c='blue', alpha=0.8, marker ='o', s=70, label='J-PLUS PN candidate')
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
    for label_, x_e, y_e in zip(number_np, x_np, y_np):
        ax.annotate(label_, (x_e, y_e), alpha=0.9, size=8,
                   xytext=(3, 5), textcoords='offset points', ha='left', va='bottom', color='blue',)

    # for label_, x, y in zip(tab_np_known['Number'], x_np_known, y_np_known):
    #     ax.annotate(label_, (x, y), alpha=0.9, size=8,
    #                  xytext=(-18, -15), textcoords='offset points', ha='left', va='bottom', color='green',)
    # for label_, x, y in zip(tab_hii_known['Number'], x_hii_known, y_hii_known):
    #     ax.annotate(label_, (x, y), alpha=0.9, size=8,
    #                  xytext=(-18, -15), textcoords='offset points', ha='left', va='bottom', color='gray',)
    # for label_, x, y in zip(tab_syst['Number'], x_syst, y_syst):
    #     ax.annotate(label_, (x, y), alpha=0.9, size=8,
    #              xytext=(-18, 5), textcoords='offset points', ha='left', va='bottom', color='red',)

    
    plt.text(0.05, 0.90, 'Zone HPNe',
         transform=ax.transAxes, fontsize='small')
    ax.minorticks_on()
    #ax1.grid(which='minor')#, lw=0.3)
    ax.legend(scatterpoints=1, loc="lower right", **lgd_kws)
    ax.grid()
    #sns.despine(bottom=True)
    plt.tight_layout()

    return plt.savefig(figfile)

def plot_J0515(x_np, y_np, figfile):
    '''
    J0515 - J0861 vs J0515 - J0660
    '''
    lgd_kws = {'frameon': True, 'fancybox': True, 'shadow': True}
    sns.set_style('ticks')       
    fig = plt.figure(figsize=(7, 6))
    ax1 = fig.add_subplot(111)
    ax1.set_xlim(xmin=-2.5,xmax=5.0)
    ax1.set_ylim(ymin=-1.5,ymax=5.5)
    plt.tick_params(axis='x', labelsize=20)
    plt.tick_params(axis='y', labelsize=20)
    plt.xlabel('$J0515 - J0861$', size = 20)
    plt.ylabel('$J0515 - J0660$', size = 20)
    ax1.scatter(x_np, y_np, c='blue', alpha=0.8, marker ='o', s=70, label='J-PLUS PN candidate')
    # Region where are located the PNe
    result = findIntersection(2.7, 2.15, 0.0, 0.22058956, 0.0)
    result_y = 2.7*result + 2.15

    x_new = np.linspace(result, 15.5, 200)
    x_new2 = np.linspace(-10.0, result, 200)
    x_new3 = np.linspace(-10.0, result, 200)
    y = 2.7*x_new + 2.15
    yy = 0.0*x_new2 + 0.22058956

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

    for label_, x, y in zip(tab_np['Number'], x_np, y_np):
        ax1.annotate(label_, (x, y), alpha=0.9, size=8,
                   xytext=(3, 5), textcoords='offset points', ha='left', va='bottom', color='blue',)
    # for label_, x, y in zip(tab_np_known['Number'], x_np_known, y_np_known):
    #     ax1.annotate(label_, (x, y), alpha=0.9, size=8,
    #                  xytext=(-18, -15), textcoords='offset points', ha='left', va='bottom', color='green',)
    # for label_, x, y in zip(tab_hii_known['Number'], x_hii_known, y_hii_known):
    #     ax1.annotate(label_, (x, y), alpha=0.9, size=8,
    #                  xytext=(-18, -15), textcoords='offset points', ha='left', va='bottom', color='gray',)
    # for label_, x, y in zip(tab_syst['Number'], x_syst, y_syst):
    #     ax1.annotate(label_, (x, y), alpha=0.9, size=8,
    #              xytext=(-18, 5), textcoords='offset points', ha='left', va='bottom', color='red',)

    plt.text(0.05, 0.90, 'Zone HPNe',
             transform=ax1.transAxes, fontsize='small')
    #Symbiotics
    # for label_, x, y in zip(number_np, x1_np, y1_np):
    #     ax1.annotate(label_, (x, y), alpha=0.9, size=8,
    #                    xytext=(3, 5), textcoords='offset points', ha='left', va='bottom',)
    # for label_, x, y in zip(Field_np, x1_np, y1_np):
    #     ax1.annotate(label_, (x, y), alpha=0.9, size=8,
    #                  xytext=(-18, -15), textcoords='offset points', ha='left', va='bottom',)
    # plt.text(0.05, 0.90, 'Zone HPNe',
    #          transform=ax1.transAxes, fontsize='small')

    ax1.minorticks_on()
    #ax1.grid(which='minor')#, lw=0.3)
    ax1.legend(scatterpoints=1, fontsize=13.0, loc="lower right", **lgd_kws)
    ax1.grid()
    #sns.despine(bottom=True)
    plt.tight_layout()

    return plt.savefig(figfile)
    
def plot_z(x_np, y_np, figfile):
    '''
    z - g vs z - J0660
    '''
    lgd_kws = {'frameon': True, 'fancybox': True, 'shadow': True}
    sns.set_style('ticks')       
    fig = plt.figure(figsize=(7, 6))
    ax2 = fig.add_subplot(111)
    ax2.set_xlim(xmin=-5.5,xmax=3.0)
    ax2.set_ylim(ymin=-3.0,ymax=4.0)
    plt.tick_params(axis='x', labelsize=20)
    plt.tick_params(axis='y', labelsize=20)
    plt.xlabel('$zSDSS - gSDSS$', size =20)
    plt.ylabel('$zSDSS - J0660$', size =20)
    #ax4.scatter(r_i00, r_ha00, c='green', alpha=0.8, marker ='.',  s=35, label='All sources')
    ax2.scatter(x_np, y_np, c='blue', alpha=0.8, marker ='o', s=70, label='J-PLUS PN candidate')
    #ax4.scatter(x_syst, y_syst, c='red' , alpha=0.8, marker ='o', s=70, label='J-PLUS SySt candidates')
    # (_, caps, _) = ax2.errorbar(x_syst, y_syst, xerr=x_syst_err, yerr=y_syst_err, marker='.', fmt='r.', elinewidth=1.4, markeredgewidth=1.4,
    #                          markersize=14, label='J-PLUS SySt candidates')
    # for cap in caps:
    #     cap.set_markeredgewidth(1)
    # #ax4.scatter(x_np_known, y_np_known, c='green', alpha=0.8, marker ='o', s=70, label='J-PLUS known PN')
    # (_, caps, _) = ax2.errorbar(x_np_known, y_np_known, xerr=x_np_known_err, yerr=y_np_known_err, marker='.', fmt='g.', elinewidth=1.4,
    #                             markeredgewidth=1.4,  markersize=14, label='J-PLUS known PN')
    # for cap in caps:
    #     cap.set_markeredgewidth(1)
    # #ax4.scatter(x_hii_known, y_hii_known, c='gray', alpha=0.8, marker ='o', s=70, label='J-PLUS known H II region')
    # (_, caps, _) = ax2.errorbar(x_hii_known, y_hii_known, xerr=x_hii_known_err, yerr=y_hii_known_err, marker='.', fmt='.', color='gray', ecolor='gray', elinewidth=1.4, markeredgewidth=1.4, markersize=14, label='J-PLUS known H II region')
    # for cap in caps:
    #     cap.set_markeredgewidth(1)
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
    for label_, x, y in zip(tab_np['Number'], x_np, y_np):
        ax2.annotate(label_, (x, y), alpha=0.9, size=8,
                       xytext=(5, 5), textcoords='offset points', ha='left', va='bottom', color='blue',)
    # for label_, x, y in zip(tab_np_known['Number'], x_np_known, y_np_known):
    #     ax2.annotate(label_, (x, y), alpha=0.9, size=8,
    #                  xytext=(-18, -15), textcoords='offset points', ha='left', va='bottom', color='green',)
    # for label_, x, y in zip(tab_hii_known['Number'], x_hii_known, y_hii_known):
    #     ax2.annotate(label_, (x, y), alpha=0.9, size=8,
    #                  xytext=(-18, -15), textcoords='offset points', ha='left', va='bottom', color='gray',)
    # for label_, x, y in zip(tab_syst['Number'], x_syst, y_syst):
    #     ax2.annotate(label_, (x, y), alpha=0.9, size=8,
    #                  xytext=(-18, 5), textcoords='offset points', ha='left', va='bottom', color='red',)

    plt.text(0.8, 0.95, 'Zone HPNe',
             transform=ax2.transAxes, fontsize='large')

    ax2.minorticks_on()
    #ax1.grid(which='minor')#, lw=0.3)
    ax2.legend(scatterpoints=1, fontsize=13.0, loc="lower right", **lgd_kws)
    ax2.grid()
    #sns.despine(bottom=True)
    plt.tight_layout()
    #plt.savefig('Fig2-IDR-JPLUS-zSDSS-gSDSS-all.jpg')
    return plt.savefig(figfile)
   
def plot_g(x_np, y_np, figfile):
    '''
    J0660 - r vs J0660 - g
    '''
    lgd_kws = {'frameon': True, 'fancybox': True, 'shadow': True}
    sns.set_style('ticks')       
    fig = plt.figure(figsize=(7, 6))
    ax3 = fig.add_subplot(111)
    ax3.set_xlim(xmin=-2.5,xmax=0.5)
    ax3.set_ylim(ymin=-5.0,ymax=1.5)
    plt.tick_params(axis='x', labelsize=20)
    plt.tick_params(axis='y', labelsize=20)
    plt.xlabel('$J0660 - rSDSS$', size =20)
    plt.ylabel('$J0660 - gSDSS$', size =20)
    #ax4.scatter(r_i00, r_ha00, c='green', alpha=0.8, marker ='.',  s=35, label='All sources')
    ax3.scatter(x_np, y_np, c='blue', alpha=0.8, marker ='o', s=70, label='J-PLUS PN candidate')
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
    ax3.plot(x_new, y, color='k', linestyle='-')
    plt.axvline(x=-0.5, ymin=0.74, ymax = 1.79, color='k', linestyle='-')
    #plt.axvline(x=0.1, ymin=0.18, ymax = 1.79, linewidth=2, color='k')

    # ax4.plot(X, 1.559*X + 0.58, color='k', linestyle='-')
    # ax4.axvline(x=-0.5, color='k', linestyle='-')
    for label_, x, y in zip(tab_np['Number'], x_np, y_np):
        ax3.annotate(label_, (x, y), alpha=0.9, size=8,
                   xytext=(3, 5), textcoords='offset points', ha='left', va='bottom', color='blue',)
    # for label_, x, y in zip(tab_np_known['Number'], x_np_known, y_np_known):
    #     ax3.annotate(label_, (x, y), alpha=0.9, size=8,
    #                  xytext=(-18, -15), textcoords='offset points', ha='left', va='bottom', color='green',)
    # for label_, x, y in zip(tab_hii_known['Number'], x_hii_known, y_hii_known):
    #     ax3.annotate(label_, (x, y), alpha=0.9, size=8,
    #                  xytext=(-18, -15), textcoords='offset points', ha='left', va='bottom', color='gray',)
    # for label_, x, y in zip(tab_syst['Number'], x_syst, y_syst):
    #     ax3.annotate(label_, (x, y), alpha=0.9, size=8,
    #              xytext=(-18, -15), textcoords='offset points', ha='left', va='bottom', color='red',)
    
    plt.text(0.05, 0.90, 'Zone HPNe',
             transform=ax3.transAxes, fontsize='small')

    ax3.minorticks_on()
    #ax1.grid(which='minor')#, lw=0.3)
    ax3.legend(scatterpoints=1, fontsize=13.0, **lgd_kws)
    ax3.grid()
    #sns.despine(bottom=True)
    plt.tight_layout()
    #plt.savefig('Fig3-IDR-JPLUS-J0660-rSDSS-all.jpg')
    return plt.savefig(figfile)
   

def plot_r(x_np, y_np, figfile):
    '''
    J0660 - r vs g - J0515
    '''
    lgd_kws = {'frameon': True, 'fancybox': True, 'shadow': True}
    sns.set_style('ticks')       
    fig = plt.figure(figsize=(7, 6))
    ax4 = fig.add_subplot(111)
    ax4.set_xlim(xmin=-2.7,xmax=0.6)
    ax4.set_ylim(ymin=-3.2,ymax=1.8)
    plt.tick_params(axis='x', labelsize=20)
    plt.tick_params(axis='y', labelsize=20)
    plt.xlabel('$J0660 - rSDSS$', size =20)
    plt.ylabel('$gSDSS - J0515$', size =20)
    ax4.scatter(x_np, y_np, c='blue', alpha=0.8, marker ='o', s=70, label='J-PLUS PN candidate')
    #ax4.scatter(r_i00, r_ha00, c='green', alpha=0.8, marker ='.',  s=35, label='All sources')
    #ax4.scatter(x_np, y_np, c='blue', alpha=0.8, marker ='o', s=70, label='J-PLUS PN candidate')
    # (_, caps, _) = ax4.errorbar(x_np, y_np, xerr=x_np_err, yerr=y_np_err, marker='.', fmt='b.', elinewidth=1.4, markeredgewidth=1.4,
    #                             markersize=14, label='J-PLUS PN candidate')
    # for cap in caps:
    #     cap.set_markeredgewidth(1)
    # #ax4.scatter(x_syst, y_syst, c='red' , alpha=0.8, marker ='o', s=70, label='J-PLUS SySt candidates')
    # (_, caps, _) = ax4.errorbar(x_syst, y_syst, xerr=x_syst_err, yerr=y_syst_err, marker='.', fmt='r.', elinewidth=1.4, markeredgewidth=1.4,
    #                          markersize=14, label='J-PLUS SySt candidates')
    # for cap in caps:
    #     cap.set_markeredgewidth(1)
    # #ax4.scatter(x_np_known, y_np_known, c='green', alpha=0.8, marker ='o', s=70, label='J-PLUS known PN')
    # (_, caps, _) = ax4.errorbar(x_np_known, y_np_known, xerr=x_np_known_err, yerr=y_np_known_err, marker='.', fmt='g.', elinewidth=1.4,
    #                             markeredgewidth=1.4,  markersize=14, label='J-PLUS known PN')
    # for cap in caps:
    #     cap.set_markeredgewidth(1)
    #ax4.scatter(x_hii_known, y_hii_known, c='gray', alpha=0.8, marker ='o', s=70, label='J-PLUS known H II region')
    # (_, caps, _) = ax4.errorbar(x_hii_known, y_hii_known, xerr=x_hii_known_err, yerr=y_hii_known_err, marker='.', fmt='.', color='gray', ecolor='gray', elinewidth=1.4, markeredgewidth=1.4, markersize=14, label='J-PLUS known H II region')
    # for cap in caps:
    #     cap.set_markeredgewidth(1)
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
    ax4.plot(x_new, y, color='k', linestyle='-')
    ax4.plot(x_new2, yy , color='k', linestyle='-')

    # Region of the simbiotic stars
    result1 = findIntersection(-0.19, -0.05, -2.66, -2.2, 0.0)
    x_new_s = np.linspace(-15.5, result1, 200)
    x_new2_s = np.linspace(-15.0, result1, 200)
    y_s = -0.19*x_new_s - 0.09
    yy_s = -2.66*x_new2_s - 2.2

    ax4.plot(x_new_s, y_s, color='r', linestyle='--')
    ax4.plot(x_new2_s, yy_s , color='r', linestyle='--')


    # ax5.plot(X, 0.12*X - 0.01, color='k', linestyle='-' )
    # ax5.plot(X, -1.1*X - 1.07, color='k', linestyle='-' )

    for label_, x, y in zip(tab_np['Number'], x_np, y_np):
         ax4.annotate(label_, (x, y), alpha=0.9, size=8,
                   xytext=(3, 5), textcoords='offset points', ha='left', va='bottom', color='blue',)
    # for label_, x, y in zip(tab_np_known['Number'], x_np_known, y_np_known):
    #     ax4.annotate(label_, (x, y), alpha=0.9, size=8,
    #                  xytext=(-18, -15), textcoords='offset points', ha='left', va='bottom', color='green',)
    # for label_, x, y in zip(tab_hii_known['Number'], x_hii_known, y_hii_known):
    #     ax4.annotate(label_, (x, y), alpha=0.9, size=8,
    #                  xytext=(-35, -15), textcoords='offset points', ha='left', va='bottom', color='gray',)
    # for label_, x, y in zip(tab_syst['Number'], x_syst, y_syst):
    #      ax4.annotate(label_, (x, y), alpha=0.9, size=8,
    #                 xytext=(-18, 5), textcoords='offset points', ha='left', va='bottom', color='red',)

    # for label_, x, y in zip(number_sym, x4_sym, y4_sym):
    #     ax5.annotate(label_, (x, y), alpha=0.9, size=8,
    #                    xytext=(3, 5), textcoords='offset points', ha='left', va='bottom',)
    # for label_, x, y in zip(Field_sym, x4_np, y4_sym):
    #     ax5.annotate(label_, (x, y), alpha=0.9, size=8,
    #                  xytext=(-18, -15), textcoords='offset points', ha='left', va='bottom',)

    plt.text(0.05, 0.1, 'Zone HPNe',
             transform=ax4.transAxes, fontsize='large')
    ax4.minorticks_on()
    #ax1.grid(which='minor')#, lw=0.3)
    ax4.legend(scatterpoints=1, fontsize=13.0, loc="lower right", **lgd_kws)
    ax4.grid()
    #sns.despine(bottom=True)
    plt.tight_layout()
    #plt.savefig('Fig4-IDR-JPLUS-J0660-rSDSS-all.jpg')
    return plt.savefig(figfile)

def plot_gi(x_np, y_np, figfile):
    '''
    g - i vs J0410 - J0660
    '''
    lgd_kws = {'frameon': True, 'fancybox': True, 'shadow': True}
    sns.set_style('ticks')       
    fig = plt.figure(figsize=(7, 6))
    ax5 = fig.add_subplot(111)
    ax5.set_xlim(xmin=-3.0,xmax=5.0)
    ax5.set_ylim(ymin=-2.0,ymax=6.0)

    plt.tick_params(axis='x', labelsize=20)
    plt.tick_params(axis='y', labelsize=20)
    plt.xlabel('$gSDSS - iSDSS$', size =20)
    plt.ylabel('$J0410 - J0660$', size =20)
    #ax4.scatter(r_i00, r_ha00, c='green', alpha=0.8, marker ='.',  s=35, label='All sources')
    ax5.scatter(x_np, y_np, c='blue', alpha=0.8, marker ='o', s=70, label='J-PLUS PN candidate')
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
    ax5.plot(x_new, y, color='k', linestyle='-')
    ax5.plot(x_new2, yy , color='k', linestyle='-')

    # Region of the simbiotic stars
    result1 = findIntersection(-5.2, +10.60, 2.13, -1.43, 0.0)
    x_new_s = np.linspace(-15.5, result1, 200)
    x_new2_s = np.linspace(result1, 15.5, 200)
    y_s = -5.2*x_new_s + 10.60
    yy_s = 2.13*x_new2_s - 1.43


    ax5.plot(x_new_s, y_s, color='r', linestyle='--')
    ax5.plot(x_new2_s, yy_s , color='r', linestyle='--')


    # ax6.plot(X, 8.0*X + 4.50, color='k', linestyle='-')
    # ax6.plot(X, 0.8*X + 0.55, color='k', linestyle='-')

    for label_, x, y in zip(tab_np['Number'], x_np, y_np):
        ax5.annotate(label_, (x, y), alpha=0.9, size=8,
                   xytext=(3, -15), textcoords='offset points', ha='left', va='bottom', color='blue',)
    # for label_, x, y in zip(tab_np_known['Number'], x_np_known, y_np_known):
    #     ax5.annotate(label_, (x, y), alpha=0.9, size=8,
    #                  xytext=(-18, -15), textcoords='offset points', ha='left', va='bottom', color='green',)
    # for label_, x, y in zip(tab_hii_known['Number'], x_hii_known, y_hii_known):
    #     ax5.annotate(label_, (x, y), alpha=0.9, size=8,
    #                  xytext=(-18, -15), textcoords='offset points', ha='left', va='bottom', color='gray',)
    # for label_, x, y in zip(tab_syst['Number'], x_syst, y_syst):
    #     ax5.annotate(label_, (x, y), alpha=0.9, size=8,
    #                  xytext=(-18, -15), textcoords='offset points', ha='left', va='bottom', color='red', )

    plt.text(0.05, 0.90, 'Zone HPNe',
             transform=ax5.transAxes, fontsize='small')
    ax5.minorticks_on()
    #ax1.grid(which='minor')#, lw=0.3)
    ax5.legend(scatterpoints=1, fontsize=13.0, loc='lower right', **lgd_kws)
    ax5.grid()
    #sns.despine(bottom=True)
    plt.tight_layout()
    #plt.savefig('Fig5-IDR-JPLUS-gSDSS-iSDSS-all.jpg')
    return plt.savefig(figfile)

#Halpha emitters find to metodogy suggest by Carlinhos
#tab_np = Table.read("ha-emitter-j660-r_iso_v1.tab", format="ascii.tab")

#Halpha emitters find will whole the criteria
tab_np = Table.read("10725_wmask.tab", format="ascii.tab")

#Field and number of the objects
number_np = tab_np['Number']

# number_sym = tab_sym['Id']
# Field_sym = tab_sym['Field']

#Calor AUTO
#Color vironen
x_np_auto = tab_np['rSDSS_auto'] - tab_np['iSDSS_auto']
y_np_auto = tab_np['rSDSS_auto'] - tab_np['J0660_auto']


#Color
x1_np_auto = tab_np['J0515_auto'] - tab_np['J0861_auto']
y1_np_auto = tab_np['J0515_auto'] - tab_np['J0660_auto']

    
#Color
x2_np_auto = tab_np['zSDSS_auto'] - tab_np['gSDSS_auto']
y2_np_auto = tab_np['zSDSS_auto'] - tab_np['J0660_auto']


#Color
x3_np_auto = tab_np['J0660_auto'] - tab_np['rSDSS_auto']
y3_np_auto = tab_np['J0660_auto'] - tab_np['gSDSS_auto']


#Color
x4_np_auto = tab_np['J0660_auto'] - tab_np['rSDSS_auto']
y4_np_auto = tab_np['gSDSS_auto'] - tab_np['J0515_auto']

    
#Color
x5_np_auto = tab_np['gSDSS_auto'] - tab_np['iSDSS_auto']
y5_np_auto = tab_np['J0410_auto'] - tab_np['J0660_auto']


#Calor ISO GAUSS
#Color vironen
x_np_ISO_GAUSS = tab_np['rSDSS_ISO_GAUSS'] - tab_np['iSDSS_ISO_GAUSS']
y_np_ISO_GAUSS = tab_np['rSDSS_ISO_GAUSS'] - tab_np['J0660_ISO_GAUSS']

#Color
x1_np_ISO_GAUSS = tab_np['J0515_ISO_GAUSS'] - tab_np['J0861_ISO_GAUSS']
y1_np_ISO_GAUSS = tab_np['J0515_ISO_GAUSS'] - tab_np['J0660_ISO_GAUSS']

#Color
x2_np_ISO_GAUSS = tab_np['zSDSS_ISO_GAUSS'] - tab_np['gSDSS_ISO_GAUSS']
y2_np_ISO_GAUSS = tab_np['zSDSS_ISO_GAUSS'] - tab_np['J0660_ISO_GAUSS']

#Color
x3_np_ISO_GAUSS = tab_np['J0660_ISO_GAUSS'] - tab_np['rSDSS_ISO_GAUSS']
y3_np_ISO_GAUSS = tab_np['J0660_ISO_GAUSS'] - tab_np['gSDSS_ISO_GAUSS']

#Color
x4_np_ISO_GAUSS = tab_np['J0660_ISO_GAUSS'] - tab_np['rSDSS_ISO_GAUSS']
y4_np_ISO_GAUSS = tab_np['gSDSS_ISO_GAUSS'] - tab_np['J0515_ISO_GAUSS']

    
#Color
x5_np_ISO_GAUSS = tab_np['gSDSS_ISO_GAUSS'] - tab_np['iSDSS_ISO_GAUSS']
y5_np_ISO_GAUSS = tab_np['J0410_ISO_GAUSS'] - tab_np['J0660_ISO_GAUSS']


#plotting###################
#############################
plot_viironen(x_np_auto, y_np_auto, "Fig1-DR1-JPLUS-vironen_auto.pdf")
plot_viironen(x_np_ISO_GAUSS, y_np_ISO_GAUSS, "Fig1-IDR-JPLUS-vironen_ISO_GAUSS.pdf")

#########################
plot_J0515(x1_np_auto, y1_np_auto, "Fig2-DR1-JPLUS-J0515_auto.pdf")
plot_J0515(x1_np_ISO_GAUSS, y1_np_ISO_GAUSS, "Fig2-IDR-JPLUS-J0515_ISO_GAUSS.pdf")
##########################
plot_z(x2_np_auto, y2_np_auto,"Fig3-DR1-JPLUS-z_auto.pdf")
plot_z(x2_np_ISO_GAUSS, y2_np_ISO_GAUSS, "Fig3-IDR-JPLUS-z_ISO_GAUSS.pdf")

#########################
plot_g(x3_np_auto, y3_np_auto,"Fig4-DR1-JPLUS-g_auto.pdf")
plot_g(x3_np_ISO_GAUSS, y3_np_ISO_GAUSS, "Fig4-IDR-JPLUS-g_ISO_GAUSS.pdf")


#########################
plot_r(x4_np_auto, y4_np_auto, "Fig5-DR1-JPLUS-r_auto.pdf")
plot_r(x4_np_ISO_GAUSS, y4_np_ISO_GAUSS, "Fig5-IDR-JPLUS-r_ISO_GAUSS.pdf")

#########################
plot_gi(x5_np_auto, y5_np_auto,  "Fig6-DR1-JPLUS-gi_auto.pdf")
plot_gi(x5_np_ISO_GAUSS, y5_np_ISO_GAUSS, "Fig6-IDR-JPLUS-gi_ISO_GAUSS.pdf")



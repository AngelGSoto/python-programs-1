'''
Make photo spectra from observed candidates JPLUS spectra
'''
from __future__ import print_function
import numpy as np
import glob
import json
import matplotlib.pyplot as plt
from astropy.table import Table
#import seaborn as sns
import sys
import argparse
import os
from colour import Color


wl = [3485, 3785, 3950, 4100, 4300, 4803, 5150, 6250, 6600, 7660, 8610, 9110]
color = ["#CC00FF", "#9900FF", "#6600FF", "#0000FF", "#009999", "#006600", "#DD8000", "#FF0000", "#CC0066", "#990033", "#660033", "#330034"]
marker = ["s", "o", "o", "o", "o", "s", "o", "s", "o", "s", "o", "s"] ### tienen todos los filtros

wl1 = [ 3785, 3950, 4100, 4300, 4803, 5150, 6250, 6600, 7660, 8610, 9110]
color1 = [ "#9900FF", "#6600FF", "#0000FF", "#009999", "#006600", "#DD8000", "#FF0000", "#CC0066", "#990033", "#660033", "#330034"]
marker1 = [ "o", "o", "o", "o", "s", "o", "s", "o", "s", "o", "s"] # No tiene el primer filtro


parser = argparse.ArgumentParser(
    description="""Write wave and magnitude of a spectrum""")

parser.add_argument("source", type=str,
                    default="known-PN-jplus-idr",
                    help="Name of source, taken the prefix ")

parser.add_argument("--debug", action="store_true",
                    help="Print out verbose debugging info about each line in region file")

args = parser.parse_args()
file_ = args.source + ".tab"

data = Table.read(file_, format="ascii.tab")

n = data["ra"]

Number = []
mag_auto  = [[] for _ in range(len(n))]

mag_petro = [[] for _ in range(len(n))]
mag_aper = [[] for _ in range(len(n))]
mag_auto_WORSTPSF = [[] for _ in range(len(n))]

#Error
mag_auto_err  = [[] for _ in range(len(n))]
mag_petro_err  = [[] for _ in range(len(n))]

print(len(n))
#sys.exit()
for i in range(len(n)):
    mag_auto[i].append(data["ujava_auto"][i])
    mag_auto[i].append(data["f378_auto"][i])
    mag_auto[i].append(data["f395_auto"][i])
    mag_auto[i].append(data["f410_auto"][i])
    mag_auto[i].append(data["f430_auto"][i])
    mag_auto[i].append(data["g_auto"][i])
    mag_auto[i].append(data["f515_auto"][i]) 
    mag_auto[i].append(data["r_auto"][i]) 
    mag_auto[i].append(data["f660_auto"][i])
    mag_auto[i].append(data["i_auto"][i]) 
    mag_auto[i].append(data["f861_auto"][i]) 
    mag_auto[i].append(data["z_auto"][i])
    #Petro
    mag_petro[i].append(data["ujava_petro"][i])
    mag_petro[i].append(data["f378_petro"][i])
    mag_petro[i].append(data["f395_petro"][i])
    mag_petro[i].append(data["f410_petro"][i])
    mag_petro[i].append(data["f430_petro"][i])
    mag_petro[i].append(data["g_petro"][i])
    mag_petro[i].append(data["f515_petro"][i]) 
    mag_petro[i].append(data["r_petro"][i]) 
    mag_petro[i].append(data["f660_petro"][i])
    mag_petro[i].append(data["i_petro"][i]) 
    mag_petro[i].append(data["f861_petro"][i]) 
    mag_petro[i].append(data["z_petro"][i])
   
    #ERRO AUTO
    mag_auto_err[i].append(float(data["eujava_auto"][i]))
    mag_auto_err[i].append(float(data["ef378_auto"][i]))
    mag_auto_err[i].append(float(data["ef395_auto"][i]))
    mag_auto_err[i].append(float(data["ef410_auto"][i]))
    mag_auto_err[i].append(float(data["ef430_auto"][i]))
    mag_auto_err[i].append(float(data["eg_auto"][i]))
    mag_auto_err[i].append(float(data["ef515_auto"][i])) 
    mag_auto_err[i].append(float(data["er_auto"][i])) 
    mag_auto_err[i].append(float(data["ef660_auto"][i]))
    mag_auto_err[i].append(float(data["ei_auto"][i]))
    mag_auto_err[i].append(float(data["ef861_auto"][i]))
    mag_auto_err[i].append(float(data["ez_auto"][i]))

    
    #ERRO petro
    mag_petro_err[i].append(data["eujava_petro"][i])
    mag_petro_err[i].append(data["ef378_petro"][i])
    mag_petro_err[i].append(data["ef395_petro"][i])
    mag_petro_err[i].append(data["ef410_petro"][i])
    mag_petro_err[i].append(data["ef430_petro"][i])
    mag_petro_err[i].append(data["eg_petro"][i])
    mag_petro_err[i].append(data["ef515_petro"][i]) 
    mag_petro_err[i].append(data["er_petro"][i]) 
    mag_petro_err[i].append(data["ef660_petro"][i])
    mag_petro_err[i].append(data["ei_petro"][i]) 
    mag_petro_err[i].append(data["ef861_petro"][i]) 
    mag_petro_err[i].append(data["ez_petro"][i])

    font = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 16,
        }

    plotfile = "photos-pectrum_splus_"+str(data["id"][i].split("S.")[-1].split(".g")[0])+"_auto.pdf"
    fig = plt.figure(figsize=(15.5, 9.5))
    ax = fig.add_subplot(1,1,1)
    plt.tick_params(axis='x', labelsize=42) 
    plt.tick_params(axis='y', labelsize=42)
    ax.set_xlim(xmin=3000, xmax=9700)
    #ax.set_ylim(ymin=17.5,ymax=23)
    #ax1.set_xlabel(r'$\lambda$')
    ax.set_xlabel(r'Wavelength $[\mathrm{\AA]}$', fontsize = 44)
    ax.set_ylabel(r'Magnitude [AB]', fontsize = 44)
    ax.plot(wl, mag_auto[i], '-k', alpha=0.2)#, label='Auto')
    for wl1, mag, mag_err, colors, marker_ in zip(wl, mag_auto[i], mag_auto_err[i], color, marker):
        ax.scatter(wl1, mag, color = colors, marker=marker_, s=600, zorder=10)
        ax.errorbar(wl1, mag, yerr=mag_err, marker='.', fmt='.', color=colors, ecolor=colors, elinewidth=5.9, markeredgewidth=5.2,  capsize=20)
    # plt.text(0.06, 0.1, "Fr 2-21",
    #          transform=ax.transAxes, fontsize=48,  fontdict=font)
    #plt.subplots_adjust(bottom=0.19)
    plt.legend(fontsize=20.0)
    plt.tight_layout()
    plt.gca().invert_yaxis()
    #save_path = '../../../Dropbox/JPAS/paper-phot/'
    #file_save = os.path.join(save_path, plotfile)
    plt.savefig(plotfile)
    plt.clf()
    ##########################################################################################
    #PETRO####################################################################################
    ##########################################################################################
    plotfile = "photos-pectrum_splus_"+"-"+str(data["id"][i].split("S.")[-1].split(".g")[0])+"_petro.pdf"
    fig = plt.figure(figsize=(15.5, 9.5))
    ax1 = fig.add_subplot(1,1,1)
    plt.tick_params(axis='x', labelsize=42) 
    plt.tick_params(axis='y', labelsize=42)
    ax1.set_xlim(xmin=3000, xmax=9700)
    #ax.set_ylim(ymin=17.5,ymax=23)
    #ax1.set_xlabel(r'$\lambda$')
    ax1.set_xlabel(r'Wavelength $[\mathrm{\AA]}$', fontsize = 44)
    ax1.set_ylabel(r'Magnitude [AB]', fontsize = 44)
    #ax1.plot(wl, mag_petro[i], '-k', alpha=0.2)#, label='Auto')
    #for wl1, mag_1, mag_err_1, colors, marker_ in zip(wl, mag_petro[i], mag_petro_err[i], color, marker):
        #ax1.scatter(wl1, mag_1, color = colors, marker=marker_, s=600, zorder=10)
        #ax1.errorbar(wl1, mag_1, yerr=mag_err_1, marker='.', fmt='.', color=colors, ecolor=colors, elinewidth=5.9, markeredgewidth=5.2,  capsize=20)
    # plt.text(0.06, 0.1, "Fr 2-21",
    #          transform=ax.transAxes, fontsize=48,  fontdict=font)
    #plt.subplots_adjust(bottom=0.19)
    plt.legend(fontsize=20.0)
    plt.tight_layout()
    plt.gca().invert_yaxis()
    #save_path = '../../../Dropbox/JPAS/paper-phot/'
    #file_save = os.path.join(save_path, plotfile)
    #plt.savefig(plotfile)
    plt.clf()

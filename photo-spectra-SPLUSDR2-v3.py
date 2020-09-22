'''
Make photo-spectra from observed SPLUS objects. This program is an updated version of the program: photo-spectra-SPLUSDR2.py.
I madified this one to work with SPLUS SMC catalog
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

Number = []

wl = [3485, 3785, 3950, 4100, 4300, 4803, 5150, 6250, 6600, 7660, 8610, 9110]
color = ["#CC00FF", "#9900FF", "#6600FF", "#0000FF", "#009999", "#006600", "#DD8000", "#FF0000", "#CC0066", "#990033", "#660033", "#330034"]
marker = ["s", "o", "o", "o", "o", "s", "o", "s", "o", "s", "o", "s"] ### tienen todos los filtros

# wl1 = [3785, 3950, 4100, 4300, 4803, 5150, 6250, 6600, 7660, 8610, 9110]
# color1 = [ "#9900FF", "#6600FF", "#0000FF", "#009999", "#006600", "#DD8000", "#FF0000", "#CC0066", "#990033", "#660033", "#330034"]
# marker1 = [ "o", "o", "o", "o", "s", "o", "s", "o", "s", "o", "s"] # No tiene el primer filtro


parser = argparse.ArgumentParser(
    description="""Write wave and magnitude of a spectrum""")

parser.add_argument("source", type=str,
                    default="known-PN-jplus-idr",
                    help="Name of source, taken the prefix ")

parser.add_argument("--debug", action="store_true",
                    help="Print out verbose debugging info about each line in region file")

args = parser.parse_args()
file_ = args.source + ".dat"


data = Table.read(file_, format="ascii")
n = data["RA"]

Number = []
mag_auto  = [[] for _ in range(len(n))]
mag_petro = [[] for _ in range(len(n))]
mag_aper = [[] for _ in range(len(n))]

#Error
mag_auto_err  = [[] for _ in range(len(n))]
mag_petro_err  = [[] for _ in range(len(n))]
mag_aper_err  = [[] for _ in range(len(n))]

print("The number of objects for calculated the S-spectra are:", len(n))
#sys.exit()

def mag(mag_aper, list_):
    list_[i].append(float(data["U_"+ mag_aper][i])) 
    list_[i].append(float(data["F378_" + mag_aper][i]))
    list_[i].append(float(data["F395_" + mag_aper][i]))
    list_[i].append(float(data["F410_" + mag_aper][i]))
    list_[i].append(float(data["F430_" + mag_aper][i]))
    list_[i].append(float(data["G_"+ mag_aper][i]))
    list_[i].append(float(data["F515_" + mag_aper][i])) 
    list_[i].append(float(data["R_" + mag_aper][i])) 
    list_[i].append(float(data["F660_" + mag_aper][i]))
    list_[i].append(float(data["I_" + mag_aper][i])) 
    list_[i].append(float(data["F861_" + mag_aper][i])) 
    list_[i].append(float(data["Z_"+ mag_aper][i]))
    
#Error
def e_mag(e_mag_aper, list_err):
    list_err[i].append(float(data["e_U_"+ e_mag_aper][i])) 
    list_err[i].append(float(data["e_F378_" + e_mag_aper][i]))
    list_err[i].append(float(data["e_F395_" + e_mag_aper][i]))
    list_err[i].append(float(data["e_F410_" + e_mag_aper][i]))
    list_err[i].append(float(data["e_F430_" + e_mag_aper][i]))
    list_err[i].append(float(data["e_G_"+ e_mag_aper][i]))
    list_err[i].append(float(data["e_F515_" + e_mag_aper][i])) 
    list_err[i].append(float(data["e_R_" + e_mag_aper][i])) 
    list_err[i].append(float(data["e_F660_" + e_mag_aper][i]))
    list_err[i].append(float(data["e_I_" + e_mag_aper][i])) 
    list_err[i].append(float(data["e_F861_" + e_mag_aper][i])) 
    list_err[i].append(float(data["e_Z_"+ e_mag_aper][i]))
    
for i in range(len(n)):
    mag("aper_3", mag_aper) # Aper
    mag("auto", mag_auto)
    mag("petro", mag_petro)
    # Error
    e_mag("aper_3", mag_aper_err)
    e_mag("auto", mag_auto_err)
    e_mag("petro", mag_petro_err)

    font = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 16,
        }
    
    ##########################################################################################
    # Plotting -- Aper  ######################################################################
    ##########################################################################################
    plotfile = "photopectrum_splus_"+str(data["ID"][i].split("S.")[-1].split(".g")[0]).replace(".", "-")+"_aper.pdf"
    fig = plt.figure(figsize=(15.5, 9.5))
    ax = fig.add_subplot(1,1,1)
    plt.tick_params(axis='x', labelsize=42) 
    plt.tick_params(axis='y', labelsize=42)
    ax.set_xlim(left=3000, right=9700)
    #ax.set_ylim(ymin=17.5,ymax=23)
    #ax1.set_xlabel(r'$\lambda$')
    ax.set_xlabel(r'Wavelength $[\mathrm{\AA]}$', fontsize = 44)
    ax.set_ylabel(r'Magnitude [AB]', fontsize = 44)
    ax.plot(wl, mag_aper[i], '-k', alpha=0.2)#, label='Auto')
    for wl1, mag, mag_err, colors, marker_ in zip(wl, mag_aper[i], mag_aper_err[i], color, marker):
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
    # Plotting -- Auto  ######################################################################
    ##########################################################################################
    plotfile = "photopectrum_splus_"+str(data["ID"][i].split("S.")[-1].split(".g")[0]).replace(".", "-")+"_auto.pdf"
    fig = plt.figure(figsize=(15.5, 9.5))
    ax = fig.add_subplot(1,1,1)
    plt.tick_params(axis='x', labelsize=42) 
    plt.tick_params(axis='y', labelsize=42)
    ax.set_xlim(left=3000, right=9700)
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
    plotfile = "photopectrum_splus_"+str(data["ID"][i].split("S.")[-1].split(".g")[0]).replace(".", "-")+"_petro.pdf"
    fig = plt.figure(figsize=(15.5, 9.5))
    ax1 = fig.add_subplot(1,1,1)
    plt.tick_params(axis='x', labelsize=42) 
    plt.tick_params(axis='y', labelsize=42)
    ax1.set_xlim(left=3000, right=9700)
    #ax.set_ylim(ymin=17.5,ymax=23)
    #ax1.set_xlabel(r'$\lambda$')
    ax1.set_xlabel(r'Wavelength $[\mathrm{\AA]}$', fontsize = 44)
    ax1.set_ylabel(r'Magnitude [AB]', fontsize = 44)
    ax1.plot(wl, mag_petro[i], '-k', alpha=0.2)#, label='Auto')
    for wl1, mag_1, mag_err_1, colors, marker_ in zip(wl, mag_petro[i], mag_petro_err[i], color, marker):
        ax1.scatter(wl1, mag_1, color = colors, marker=marker_, s=600, zorder=10)
        ax1.errorbar(wl1, mag_1, yerr=mag_err_1, marker='.', fmt='.', color=colors, ecolor=colors, elinewidth=5.9, markeredgewidth=5.2,  capsize=20)
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

'''
Make photo-spectra from observed SPLUS objects. This program is an updated version of the program: photo-spectra-SPLUSDR2.py.
I madified this one to work with SPLUS SMC catalog
'''
from __future__ import print_function
import numpy as np
import glob
import json
import matplotlib.pyplot as plt
plt.rcParams.update({'figure.max_open_warning': 0})
from astropy.table import Table
#import seaborn as sns
import sys
import argparse
import os
from colour import Color
from pathlib import Path

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

ROOT_PATH = Path("..")  # necessary since we are in the sub-folder

data = Table.read(ROOT_PATH / file_, format="ascii")
n = len(data)

Number = []
mag_auto  = [[] for _ in range(n)]
mag_petro = [[] for _ in range(n)]
mag_aper = [[] for _ in range(n)]

#Error
mag_auto_err  = [[] for _ in range(n)]
mag_petro_err  = [[] for _ in range(n)]
mag_aper_err  = [[] for _ in range(n)]

print("The number of objects for calculated the S-spectra are:", n)

#sys.exit()
for i in range(n):
    mag_aper[i].append(data["U_aper_3"][i]) #aper
    mag_aper[i].append(data["F378_aper_3"][i])
    mag_aper[i].append(data["F395_aper_3"][i])
    mag_aper[i].append(data["F410_aper_3"][i])
    mag_aper[i].append(data["F430_aper_3"][i])
    mag_aper[i].append(data["G_aper_3"][i])
    mag_aper[i].append(data["F515_aper_3"][i]) 
    mag_aper[i].append(data["R_aper_3"][i]) 
    mag_aper[i].append(data["F660_aper_3"][i])
    mag_aper[i].append(data["I_aper_3"][i]) 
    mag_aper[i].append(data["F861_aper_3"][i]) 
    mag_aper[i].append(data["Z_aper_3"][i])
    #auto
    mag_auto[i].append(data["U_auto"][i]) #auto
    mag_auto[i].append(data["F378_auto"][i])
    mag_auto[i].append(data["F395_auto"][i])
    mag_auto[i].append(data["F410_auto"][i])
    mag_auto[i].append(data["F430_auto"][i])
    mag_auto[i].append(data["G_auto"][i])
    mag_auto[i].append(data["F515_auto"][i]) 
    mag_auto[i].append(data["R_auto"][i]) 
    mag_auto[i].append(data["F660_auto"][i])
    mag_auto[i].append(data["I_auto"][i]) 
    mag_auto[i].append(data["F861_auto"][i]) 
    mag_auto[i].append(data["Z_auto"][i])
    #Petro
    mag_petro[i].append(data["U_petro"][i])
    mag_petro[i].append(data["F378_petro"][i])
    mag_petro[i].append(data["F395_petro"][i])
    mag_petro[i].append(data["F410_petro"][i])
    mag_petro[i].append(data["F430_petro"][i])
    mag_petro[i].append(data["G_petro"][i])
    mag_petro[i].append(data["F515_petro"][i]) 
    mag_petro[i].append(data["R_petro"][i]) 
    mag_petro[i].append(data["F660_petro"][i])
    mag_petro[i].append(data["I_petro"][i]) 
    mag_petro[i].append(data["F861_petro"][i]) 
    mag_petro[i].append(data["Z_petro"][i])

    #ERRO Aper
    mag_aper_err[i].append(float(data["e_U_aper_3"][i]))
    mag_aper_err[i].append(float(data["e_F378_aper_3"][i]))
    mag_aper_err[i].append(float(data["e_F395_aper_3"][i]))
    mag_aper_err[i].append(float(data["e_F410_aper_3"][i]))
    mag_aper_err[i].append(float(data["e_F430_aper_3"][i]))
    mag_aper_err[i].append(float(data["e_G_aper_3"][i]))
    mag_aper_err[i].append(float(data["e_F515_aper_3"][i])) 
    mag_aper_err[i].append(float(data["e_R_aper_3"][i])) 
    mag_aper_err[i].append(float(data["e_F660_aper_3"][i])) 
    mag_aper_err[i].append(float(data["e_I_aper_3"][i]))
    mag_aper_err[i].append(float(data["e_F861_aper_3"][i]))
    mag_aper_err[i].append(float(data["e_Z_aper_3"][i]))
   
    #ERRO AUTO
    mag_auto_err[i].append(float(data["e_U_auto"][i]))
    mag_auto_err[i].append(float(data["e_F378_auto"][i]))
    mag_auto_err[i].append(float(data["e_F395_auto"][i]))
    mag_auto_err[i].append(float(data["e_F410_auto"][i]))
    mag_auto_err[i].append(float(data["e_F430_auto"][i]))
    mag_auto_err[i].append(float(data["e_G_auto"][i]))
    mag_auto_err[i].append(float(data["e_F515_auto"][i])) 
    mag_auto_err[i].append(float(data["e_R_auto"][i])) 
    mag_auto_err[i].append(float(data["e_F660_auto"][i]))
    mag_auto_err[i].append(float(data["e_I_auto"][i]))
    mag_auto_err[i].append(float(data["e_F861_auto"][i]))
    mag_auto_err[i].append(float(data["e_Z_auto"][i]))

    #ERRO petro
    mag_petro_err[i].append(data["e_U_petro"][i])
    mag_petro_err[i].append(data["e_F378_petro"][i])
    mag_petro_err[i].append(data["e_F395_petro"][i])
    mag_petro_err[i].append(data["e_F410_petro"][i])
    mag_petro_err[i].append(data["e_F430_petro"][i])
    mag_petro_err[i].append(data["e_G_petro"][i])
    mag_petro_err[i].append(data["e_F515_petro"][i]) 
    mag_petro_err[i].append(data["e_R_petro"][i]) 
    mag_petro_err[i].append(data["e_F660_petro"][i])
    mag_petro_err[i].append(data["e_I_petro"][i]) 
    mag_petro_err[i].append(data["e_F861_petro"][i]) 
    mag_petro_err[i].append(data["e_Z_petro"][i])

    font = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 16,
        }
    ##########################################################################################
    # Plotting -- Aper  ######################################################################
    ##########################################################################################
    plotfile = "photopectrum_splus_"+str(data["ID"][i].split("S.")[-1].split(".g")[0]).replace(".", "-")+"_{}_aper.pdf".format(file_.split('.da')[0])
    fig = plt.figure(figsize=(15.5, 9.5))
    ax = fig.add_subplot(1,1,1)
    plt.tick_params(axis='x', labelsize=42) 
    plt.tick_params(axis='y', labelsize=42)
    ax.set_xlim(left=3000, right=9700)
    #ax.set_ylim(ymin=17.5,ymax=23)
    #ax1.set_xlabel(r'$\lambda$')
    ax.set_xlabel(r'Wavelength $[\mathrm{\AA]}$', fontsize = 44)
    ax.set_ylabel(r'Magnitude [AB]', fontsize = 44)

    # Mask to no no take the values 99.0
    mask = [mag_aper[i][m] != 99.0 for m in range(len(mag_aper[0]))]

    ax.plot(np.array(wl)[mask], np.array(mag_aper[i])[mask], '-k', alpha=0.2)#, label='Auto')
    for wl1, mag, mag_err, colors, marker_ in zip(np.array(wl)[mask], np.array(mag_aper[i])[mask], mag_aper_err[i], color, marker):
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
    plotfile = "photopectrum_splus_"+str(data["ID"][i].split("S.")[-1].split(".g")[0]).replace(".", "-")+"_{}_auto.pdf".format(file_.split('.da')[0])
    fig = plt.figure(figsize=(15.5, 9.5))
    ax = fig.add_subplot(1,1,1)
    plt.tick_params(axis='x', labelsize=42) 
    plt.tick_params(axis='y', labelsize=42)
    ax.set_xlim(left=3000, right=9700)
    #ax.set_ylim(ymin=17.5,ymax=23)
    #ax1.set_xlabel(r'$\lambda$')
    ax.set_xlabel(r'Wavelength $[\mathrm{\AA]}$', fontsize = 44)
    ax.set_ylabel(r'Magnitude [AB]', fontsize = 44)

    # Mask to no take the values 99.0
    mask_au = [mag_auto[i][m] != 99.0 for m in range(len(mag_auto[0]))]

    ax.plot(np.array(wl)[mask_au], np.array(mag_auto[i])[mask_au], '-k', alpha=0.2)#, label='Auto')
    for wl1, mag, mag_err, colors, marker_ in zip(np.array(wl)[mask_au], np.array(mag_auto[i])[mask_au], mag_auto_err[i], color, marker):
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
    plotfile = "photopectrum_splus_"+str(data["ID"][i].split("S.")[-1].split(".g")[0]).replace(".", "-")+"_{}_petro.pdf".format(file_.split('.da')[0])
    fig = plt.figure(figsize=(15.5, 9.5))
    ax1 = fig.add_subplot(1,1,1)
    plt.tick_params(axis='x', labelsize=42) 
    plt.tick_params(axis='y', labelsize=42)
    ax1.set_xlim(left=3000, right=9700)
    #ax.set_ylim(ymin=17.5,ymax=23)
    #ax1.set_xlabel(r'$\lambda$')
    ax1.set_xlabel(r'Wavelength $[\mathrm{\AA]}$', fontsize = 44)
    ax1.set_ylabel(r'Magnitude [AB]', fontsize = 44)

    # Mask to no take the values 99.0
    mask_p = [mag_petro[i][m] != 99.0 for m in range(len(mag_petro[0]))]   

    ax1.plot(np.array(wl)[mask_p], np.array(mag_petro[i])[mask_p], '-k', alpha=0.2)#, label='Auto')
    for wl1, mag_1, mag_err_1, colors, marker_ in zip(np.array(wl)[mask_p], np.array(mag_petro[i])[mask_p], mag_petro_err[i], color, marker):
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

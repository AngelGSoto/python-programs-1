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

plt.rcParams.update({'figure.max_open_warning': 0})

wl = [3485, 3785, 3950, 4100, 4300, 4803, 5150, 6250, 6600, 7660, 8610, 9110]
color = ["#CC00FF", "#9900FF", "#6600FF", "#0000FF", "#009999", "#006600", "#DD8000", "#FF0000", "#CC0066", "#990033", "#660033", "#330034"]
marker = ["s", "o", "o", "o", "o", "s", "o", "s", "o", "s", "o", "s"] ### tienen todos los filtros

# wl1 = [ 3785, 3950, 4100, 4300, 4803, 5150, 6250, 6600, 7660, 8610, 9110]
# color1 = [ "#9900FF", "#6600FF", "#0000FF", "#009999", "#006600", "#DD8000", "#FF0000", "#CC0066", "#990033", "#660033", "#330034"]
# marker1 = [ "o", "o", "o", "o", "s", "o", "s", "o", "s", "o", "s"] # No tiene el primer filtro

#label_obj = ['PN candidate', "[HLG90] 55", "LEDA 101538", "PN Sp 4-1"]
label_pne = ['TK 1', "Kn J1857.7+3931", "KnPa J1848.6+4151", "Jacoby 1"]
label_obj = ['26063-6129', "LEDA 101538", "PN Sp 4-1", 'LEDA 2790884']

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
n = len(data)

Number = []

mag_auto  = [[] for _ in range(n)]
mag_MAG_APER_6_0 = [[] for _ in range(n)]
mag_aper = [[] for _ in range(n)]
mag_auto_WORSTPSF = [[] for _ in range(n)]

#Error
mag_auto_err  = [[] for _ in range(n)]
mag_MAG_APER_6_0_err  = [[] for _ in range(n)]

print(n)

for i in range(n):
    mag_auto[i].append(data["uJAVA_auto"][i])
    mag_auto[i].append(data["J0378_auto"][i])
    mag_auto[i].append(data["J0395_auto"][i])
    mag_auto[i].append(data["J0410_auto"][i])
    mag_auto[i].append(data["J0430_auto"][i])
    mag_auto[i].append(data["gSDSS_auto"][i])
    mag_auto[i].append(data["J0515_auto"][i]) 
    mag_auto[i].append(data["rSDSS_auto"][i]) 
    mag_auto[i].append(data["J0660_auto"][i])
    mag_auto[i].append(data["iSDSS_auto"][i]) 
    mag_auto[i].append(data["J0861_auto"][i]) 
    mag_auto[i].append(data["zSDSS_auto"][i])
    #Aper 6
    mag_MAG_APER_6_0[i].append(data["uJAVA_MAG_APER_6_0"][i])
    mag_MAG_APER_6_0[i].append(data["J0378_MAG_APER_6_0"][i])
    mag_MAG_APER_6_0[i].append(data["J0395_MAG_APER_6_0"][i])
    mag_MAG_APER_6_0[i].append(data["J0410_MAG_APER_6_0"][i])
    mag_MAG_APER_6_0[i].append(data["J0430_MAG_APER_6_0"][i])
    mag_MAG_APER_6_0[i].append(data["gSDSS_MAG_APER_6_0"][i])
    mag_MAG_APER_6_0[i].append(data["J0515_MAG_APER_6_0"][i]) 
    mag_MAG_APER_6_0[i].append(data["rSDSS_MAG_APER_6_0"][i]) 
    mag_MAG_APER_6_0[i].append(data["J0660_MAG_APER_6_0"][i])
    mag_MAG_APER_6_0[i].append(data["iSDSS_MAG_APER_6_0"][i]) 
    mag_MAG_APER_6_0[i].append(data["J0861_MAG_APER_6_0"][i]) 
    mag_MAG_APER_6_0[i].append(data["zSDSS_MAG_APER_6_0"][i])
    #ERRO AUTO
    mag_auto_err[i].append(data["uJAVA_auto_err"][i])
    mag_auto_err[i].append(data["J0378_auto_err"][i])
    mag_auto_err[i].append(data["J0395_auto_err"][i])
    mag_auto_err[i].append(data["J0410_auto_err"][i])
    mag_auto_err[i].append(data["J0430_auto_err"][i])
    mag_auto_err[i].append(data["gSDSS_auto_err"][i])
    mag_auto_err[i].append(data["J0515_auto_err"][i]) 
    mag_auto_err[i].append(data["rSDSS_auto_err"][i]) 
    mag_auto_err[i].append(data["J0660_auto_err"][i])
    mag_auto_err[i].append(data["iSDSS_auto_err"][i])
    try:
        mag_auto_err[i].append(data["J0861_auto_err"][i])
    except ValueError:
        mag_auto_err[i].append(float(0.0))
    mag_auto_err[i].append(data["zSDSS_auto_err"][i])

    #ERROR Aper 6
    mag_MAG_APER_6_0_err[i].append(data["uJAVA_MAG_APER_6_0_err"][i])
    mag_MAG_APER_6_0_err[i].append(data["J0378_MAG_APER_6_0_err"][i])
    mag_MAG_APER_6_0_err[i].append(data["J0395_MAG_APER_6_0_err"][i])
    mag_MAG_APER_6_0_err[i].append(data["J0410_MAG_APER_6_0_err"][i])
    mag_MAG_APER_6_0_err[i].append(data["J0430_MAG_APER_6_0_err"][i])
    mag_MAG_APER_6_0_err[i].append(data["gSDSS_MAG_APER_6_0_err"][i])
    mag_MAG_APER_6_0_err[i].append(data["J0515_MAG_APER_6_0_err"][i]) 
    mag_MAG_APER_6_0_err[i].append(data["rSDSS_MAG_APER_6_0_err"][i]) 
    mag_MAG_APER_6_0_err[i].append(data["J0660_MAG_APER_6_0_err"][i])
    mag_MAG_APER_6_0_err[i].append(data["iSDSS_MAG_APER_6_0_err"][i]) 
    mag_MAG_APER_6_0_err[i].append(data["J0861_MAG_APER_6_0_err"][i]) 
    mag_MAG_APER_6_0_err[i].append(data["zSDSS_MAG_APER_6_0_err"][i])
    
    font = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 16,
        }
    #########################################
    # Aper 6                              ###
    #########################################
    plotfile = "photospectrum_"+str(data["Tile"][i])+"-"+str(data["Number"][i])+"-{}_auto.pdf".format(file_.split('.ta')[0])
    fig = plt.figure(figsize=(15.5, 9.5))
    ax = fig.add_subplot(1,1,1)
    plt.tick_params(axis='x', labelsize=42) 
    plt.tick_params(axis='y', labelsize=42)
    ax.set_xlim(xmin=3000, xmax=9700)
    #ax.set_ylim(ymin=17.5,ymax=23)
    #ax1.set_xlabel(r'$\lambda$')
    ax.set_xlabel(r'Wavelength $[\mathrm{\AA]}$', fontsize = 44)
    ax.set_ylabel(r'Magnitude [AB]', fontsize = 44)
   
    # Mask to no take the values 99.0
    mask_au = [mag_auto[i][m] != 99.0 for m in range(len(mag_auto[0]))]

    ax.plot(np.array(wl)[mask_au], np.array(mag_auto[i])[mask_au], '-k', alpha=0.2)#, label='Auto')
    for wl1, mag, mag_err, colors, marker_ in zip(np.array(wl)[mask_au], np.array(mag_auto[i])[mask_au], np.array(mag_auto_err[i]), color, marker):
        ax.scatter(wl1, mag, color = colors, marker=marker_, s=600, zorder=10)
        try:
            ax.errorbar(wl1, mag, yerr=mag_err, marker='.', fmt='.', color=colors, ecolor=colors, elinewidth=5.9, markeredgewidth=5.2, capsize=20)
        except ValueError:
            continue
     
    #plt.subplots_adjust(bottom=0.19)
    # plt.text(0.06, 0.86, label_obj[i],
    #     transform=ax.transAxes, fontsize=48,  fontdict=font)
    # plt.text(0.06, 0.85, label_obj[i],
    #      transform=ax.transAxes, fontsize=45,  fontdict=font)
    plt.legend(fontsize=20.0)
    plt.tight_layout()
    plt.tight_layout()
    plt.gca().invert_yaxis()
    #save_path = '../../../../../Dropbox/JPAS/paper-phot/'
    # save_path = '../../../../../Dropbox/paper-pne/Fig/'
    save_path = 'figs-pca/'
    #save_path = 'Jspectra-missingPN/'
    file_save = os.path.join(save_path, plotfile)
    plt.savefig(file_save)
    plt.clf()

    #########################################
    # Auto                               ####
    #########################################
    plotfile1 = "photospectrum_"+str(data["Tile"][i])+"-"+str(data["Number"][i])+"-{}_MAG_APER_6_0.pdf".format(file_.split('.ta')[0])
    fig = plt.figure(figsize=(15.5, 9.5))
    ax = fig.add_subplot(1,1,1)
    plt.tick_params(axis='x', labelsize=42) 
    plt.tick_params(axis='y', labelsize=42)
    ax.set_xlim(xmin=3000, xmax=9700)
    #ax.set_ylim(ymin=17.5,ymax=23)
    #ax1.set_xlabel(r'$\lambda$')
    ax.set_xlabel(r'Wavelength $[\mathrm{\AA]}$', fontsize = 44)
    ax.set_ylabel(r'Magnitude [AB]', fontsize = 44)

    #Mask to no take the values 99.0
    mask_ap = [mag_MAG_APER_6_0[i][m] != 99.0 for m in range(len(mag_MAG_APER_6_0[0]))]
    
    ax.plot(np.array(wl)[mask_ap], np.array(mag_MAG_APER_6_0[i])[mask_ap], '-k', alpha=0.2)#, label='Auto')
    for wl1, mag, mag_err, colors, marker_ in zip(np.array(wl)[mask_ap], np.array(mag_MAG_APER_6_0[i])[mask_ap], np.array(mag_MAG_APER_6_0_err[i]), color, marker):
        ax.scatter(wl1, mag, color = colors, marker=marker_, s=600, zorder=10)
        try:
            ax.errorbar(wl1, mag, yerr=mag_err, marker='.', fmt='.', color=colors, ecolor=colors, elinewidth=5.9, markeredgewidth=5.2, capsize=20)
        except ValueError:
            continue
    #plt.subplots_adjust(bottom=0.19)
    # plt.text(0.06, 0.86, label_obj[i],
    #     transform=ax.transAxes, fontsize=48,  fontdict=font)
    # plt.text(0.06, 0.85, label_obj[i],
    #      transform=ax.transAxes, fontsize=45,  fontdict=font)
    plt.legend(fontsize=20.0)
    plt.tight_layout()
    plt.tight_layout()
    plt.gca().invert_yaxis()
    #save_path = '../../../../../Dropbox/JPAS/paper-phot/'
    #save_path = 'figs-pca/'
    file_save = os.path.join(save_path, plotfile1)
    plt.savefig(file_save)
    plt.clf()

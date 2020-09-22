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

Number = []
n = 4
mag_auto  = []
mag_ISO_GAUSS = [[] for _ in range(n)]
mag_aper = [[] for _ in range(n)]
mag_auto_WORSTPSF = [[] for _ in range(n)]

#Error
mag_auto_err  = []
mag_ISO_GAUSS_err  = [[] for _ in range(n)]

# wl = [3485, 3785, 3950, 4100, 4300, 4803, 5150, 6250, 6600, 7660, 8610, 9110]
# color = ["#CC00FF", "#9900FF", "#6600FF", "#0000FF", "#009999", "#006600", "#DD8000", "#FF0000", "#CC0066", "#990033", "#660033", "#330034"]
# marker = ["s", "o", "o", "o", "o", "s", "o", "s", "o", "s", "o", "s"] ### tienen todos los filtros

wl = [3785, 3950, 4100, 4300, 4803, 5150, 6250, 6600, 7660, 8610, 9110]
color = [ "#9900FF", "#6600FF", "#0000FF", "#009999", "#006600", "#DD8000", "#FF0000", "#CC0066", "#990033", "#660033", "#330034"]
marker = [ "o", "o", "o", "o", "s", "o", "s", "o", "s", "o", "s"] # No tiene el primer filtro

label_pne = ['TK 1', "Kn J1857.7+3931", "KnPa J1848.6+4151", "Jacoby 1"]

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

mag_auto.append(data["J0378_auto"][2])
mag_auto.append(data["J0395_auto"][2])
mag_auto.append(data["J0410_auto"][2])
mag_auto.append(data["J0430_auto"][2])
mag_auto.append(data["gSDSS_auto"][2])
mag_auto.append(data["J0515_auto"][2]) 
mag_auto.append(data["rSDSS_auto"][2]) 
mag_auto.append(data["J0660_auto"][2])
mag_auto.append(data["iSDSS_auto"][2]) 
mag_auto.append(data["J0861_auto"][2]) 
mag_auto.append(data["zSDSS_auto"][2])
#Petro
mag_ISO_GAUSS.append(data["J0378_ISO_GAUSS"][2])
mag_ISO_GAUSS.append(data["J0395_ISO_GAUSS"][2])
mag_ISO_GAUSS.append(data["J0410_ISO_GAUSS"][2])
mag_ISO_GAUSS.append(data["J0430_ISO_GAUSS"][2])
mag_ISO_GAUSS.append(data["gSDSS_ISO_GAUSS"][2])
mag_ISO_GAUSS.append(data["J0515_ISO_GAUSS"][2]) 
mag_ISO_GAUSS.append(data["rSDSS_ISO_GAUSS"][2]) 
mag_ISO_GAUSS.append(data["J0660_ISO_GAUSS"][2])
mag_ISO_GAUSS.append(data["iSDSS_ISO_GAUSS"][2]) 
mag_ISO_GAUSS.append(data["J0861_ISO_GAUSS"][2]) 
mag_ISO_GAUSS.append(data["zSDSS_ISO_GAUSS"][2])
   
    #ERRO AUTO
mag_auto_err.append(float(data["J0378_auto_err"][2]))
mag_auto_err.append(float(data["J0395_auto_err"][2]))
mag_auto_err.append(float(data["J0410_auto_err"][2]))
mag_auto_err.append(float(data["J0430_auto_err"][2]))
mag_auto_err.append(float(data["gSDSS_auto_err"][2]))
mag_auto_err.append(float(data["J0515_auto_err"][2])) 
mag_auto_err.append(float(data["rSDSS_auto_err"][2])) 
mag_auto_err.append(float(data["J0660_auto_err"][2]))
mag_auto_err.append(float(data["iSDSS_auto_err"][2]))
try:
    mag_auto_err.append(float(data["J0861_auto_err"][2]))
except ValueError:
    mag_auto_err.append(float(0.0))
mag_auto_err.append(float(data["zSDSS_auto_err"][2]))

font = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 16,
        }

plotfile = "photospectrum_"+str(data["Number"][2])+"_auto.pdf"
fig = plt.figure(figsize=(14.29, 9))
ax = fig.add_subplot(1,1,1)
plt.tick_params(axis='x', labelsize=42) 
plt.tick_params(axis='y', labelsize=42)
ax.set_xlim(xmin=3000, xmax=9700)
#ax.set_ylim(ymin=18.9,ymax=21)
#ax1.set_xlabel(r'$\lambda$')
ax.set_xlabel(r'Wavelength $[\mathrm{\AA]}$', fontsize = 44)
ax.set_ylabel(r'Magnitude [AB]', fontsize = 44)
ax.plot(wl, mag_auto, '-k', alpha=0.2)#, label='Auto')
for wl1, mag, mag_err, colors, marker_ in zip(wl, mag_auto, mag_auto_err, color, marker):
    ax.scatter(wl1, mag, color = colors, marker=marker_, s=600, zorder=10)
    ax.errorbar(wl1, mag, yerr=mag_err, marker='.', fmt='.', color=colors, ecolor=colors, elinewidth=5.9, markeredgewidth=5.2,  capsize=20)
#plt.subplots_adjust(bottom=0.19)
plt.text(0.18, 0.1, label_pne[2],
         transform=ax.transAxes, fontsize=45,  fontdict=font)
plt.legend(fontsize=20.0)
plt.tight_layout()
plt.gca().invert_yaxis()
#save_path = '../../../../../Dropbox/JPAS/paper-phot/'
save_path = '../../../../../Dropbox/paper-pne/Fig/'
file_save = os.path.join(save_path, plotfile)
plt.savefig(file_save)
plt.clf()

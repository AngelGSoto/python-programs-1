'''
Plot spectra
'''
from __future__ import print_function
import numpy as np
import glob
import json
import matplotlib.pyplot as plt
#import seaborn as sns
import sys
import argparse
from astropy.table import Table
import os
from colour import Color

parser = argparse.ArgumentParser(
    description="""Write wave and magnitude of a spectrum""")

parser.add_argument("source", type=str,
                    default="DdDm-1-HPNe-JPLUS17-magnitude",
                    help="Name of source, taken the prefix ")

parser.add_argument("--savefig", action="store_true",
                    help="Save a figure showing the magnitude")

parser.add_argument("--debug", action="store_true",
                    help="Print out verbose debugging info about each line in region file")

args = parser.parse_args()
file_ = args.source + ".dat"

#photometry
wl = [3485, 3785, 3950, 4100, 4300, 4803, 5150, 6250, 6600, 7660, 8610, 9110]
color= ["#CC00FF", "#9900FF", "#6600FF", "#0000FF", "#009999", "#006600", "#DD8000", "#FF0000", "#CC0066", "#990033", "#660033", "#330034"]
marker = ["s", "o", "o", "o", "o", "s", "o", "s", "o", "s", "o", "s"]
mag_auto = []
mag_auto_err = []
data = Table.read("10725_wmask.tab", format="ascii.tab")
mag_auto.append(data["uJAVA_auto"])
mag_auto.append(data["J0378_auto"])
mag_auto.append(data["J0395_auto"])
mag_auto.append(data["J0410_auto"])
mag_auto.append(data["J0430_auto"])
mag_auto.append(data["gSDSS_auto"])
mag_auto.append(data["J0515_auto"]) 
mag_auto.append(data["rSDSS_auto"]) 
mag_auto.append(data["J0660_auto"])
mag_auto.append(data["iSDSS_auto"]) 
mag_auto.append(data["J0861_auto"]) 
mag_auto.append(data["zSDSS_auto"])

#error
mag_auto_err.append(float(data["uJAVA_auto_err"]))
mag_auto_err.append(float(data["J0378_auto_err"]))
mag_auto_err.append(float(data["J0395_auto_err"]))
mag_auto_err.append(float(data["J0410_auto_err"]))
mag_auto_err.append(float(data["J0430_auto_err"]))
mag_auto_err.append(float(data["gSDSS_auto_err"]))
mag_auto_err.append(float(data["J0515_auto_err"])) 
mag_auto_err.append(float(data["rSDSS_auto_err"])) 
mag_auto_err.append(float(data["J0660_auto_err"]))
mag_auto_err.append(float(data["iSDSS_auto_err"]))
mag_auto_err.append(float(data["J0861_auto_err"]))
mag_auto_err.append(float(data["zSDSS_auto_err"]))

# Spectrum
def sys(spectra):
    file_ = spectra
    x = np.loadtxt(file_, delimiter = None, skiprows = 0, usecols = None,
                   unpack = False, dtype = np.dtype([('Wl', '|f8'), ('Flux', 'f8')]))
    return x['Wl'], x['Flux']

x, y = sys(file_)
m = (x >=3600) & (x <= 7010)
y /=1e-15

x1 = x[m]
y1 = y[m]

if args.savefig:
    plotfile = file_.replace(".dat", 
                    ".pdf")
    fig = plt.figure(figsize=(14.29, 9))
    ax = fig.add_subplot(1,1,1)
    plt.tick_params(axis='x', labelsize=30) 
    plt.tick_params(axis='y', labelsize=30)
    #ax.set_xlim(xmin=3000, xmax=9700)
    ax.set_xlim(xmin=3600, xmax=7000)
    ax.set_ylim(ymin=-0.15,ymax=3.3)
    #ax.set_ylim(ymin=-1,ymax=12.0)
    #ax1.set_xlabel(r'$\lambda$')
    ax.set_xlabel(r'Wavelength $[\mathrm{\AA]}$', fontsize = 33)
    ax.set_ylabel(r'Flux $(\mathrm{10^{-15} erg\ s^{-1} cm^{-2} \AA^{-1}})$', fontsize = 33)
    #ax.set_ylabel(r'Normalized Flux', fontsize = 20)
    ax.plot(x1, y1, linewidth=2.3, alpha = 0.6, color="black")
    #plt.subplots_adjust(bottom=0.19)
    # plt.text(0.75, 0.94, 'QSO (z=2.3)',
    #          transform=ax.transAxes, fontsize=25, weight='bold')
    # plt.text(0.75, 0.68, 'Star (A0)',
    #          transform=ax.transAxes, fontsize=25, weight='bold')
    # plt.text(0.71, 0.25, 'Galaxy (z=0.0)',
    #          transform=ax.transAxes, fontsize=25, weight='bold')
    #Plot syntehtic object 
    for wl1, mag, mag_err, colors, marker_ in zip(wl, mag_auto, mag_auto_err, color, marker):       #
        F = (10**(-(mag + 2.41) / 2.5)) / wl1**2
        F_err = (10**(-(mag_err + 2.41) / 2.5)) / wl1**2
        #F_.append(F)
        # print(y+7)
        F /=1e-15
        F *=0.3
        F_err /=1e-15
        #F_err *=0.3
        ax.scatter(wl1, F, c = colors, marker=marker_, s=250, zorder=3)
        ax.errorbar(wl1, F, yerr=mag_err, marker='.', fmt='.', color=colors, ecolor=colors, elinewidth=5.9, markeredgewidth=5.2, capsize=15)
       
    #plt.legend(fontsize=20.0)
    #plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig(plotfile)
    plt.clf()

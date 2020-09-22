'''
Make photo-spectra from convolved J-PLUS spectra
'''
from __future__ import print_function
import numpy as np
import glob
import json
import matplotlib.pyplot as plt
#import seaborn as sns
import sys
import argparse
import os
from colour import Color
from astropy.io import fits
import seaborn as sns

magnitude= []

wl = [3485, 3785, 3950, 4100, 4300, 4803, 5150, 6250, 6600, 7660, 8610, 9110]
# color= ["#0000FF", "#5F9EA0", "#8EE5EE", "#008000", "#FFFF00", "#FFA54F", "#8B5A2B", "#FA8072", "#FF0000", "#A52A2A", "#8B3E2F", "#800000"]
# color1= ["#0000FF", "#0000FF", "#0000FF", "#0000FF", "#0000FF", "#0000FF", "#0000FF", "#0000FF", "#0000FF", "#0000FF", "#0000FF", "#0000FF"]
# marker = ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o"]
color= ["#CC00FF", "#9900FF", "#6600FF", "#0000FF", "#009999", "#006600", "#DD8000", "#FF0000", "#CC0066", "#990033", "#660033", "#330034"]
marker = ["s", "o", "o", "o", "o", "s", "o", "s", "o", "s", "o", "s"]


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
file_ = args.source + ".json"


c = 2.99792458e18 #speed of light in Angstron/sec
with open(file_) as f:
    data = json.load(f)
    magnitude.append(data["F348"])
    magnitude.append(data["F378"])
    magnitude.append(data["F395"])
    magnitude.append(data["F410"])
    magnitude.append(data["F430"])
    magnitude.append(data["F480_g_sdss"])
    magnitude.append(data["F515"]) 
    magnitude.append(data["F625_r_sdss"]) 
    magnitude.append(data["F660"])
    magnitude.append(data["F766_i_sdss"]) 
    magnitude.append(data["F861"]) 
    magnitude.append(data["F911_z_sdss"])


# Spectrum from SLOAN
hdulist = fits.open("spec-2967-54584-0410.fits")
y = 1E-17*hdulist[1].data.field('flux')
x = 10**hdulist[1].data.field('loglam')
y /= 1E-15

#Object observed by S-PLUS
mag_s = [19.65, 19.52, 19.12, 19.33, 19.45, 18.6, 18.41, 17.99, 17.92, 17.66, 17.57, 17.48]

#####################################################
if args.savefig:
    plotfile = file_.replace(".json", 
                    "-flux.pdf")
    fig = plt.figure(figsize=(14.29, 9))
    ax = fig.add_subplot(1,1,1)
    plt.tick_params(axis='x', labelsize=40) 
    plt.tick_params(axis='y', labelsize=35)
    ax.set_xlim(xmin=3000,xmax=9700)
    ax.set_ylim(ymin=-0.0,ymax=0.7)
    #ax.set_ylim(ymin=-0.1,ymax=1e-10)
    #ax.set_ylim(ymin=0,ymax=12.3)
    #ax1.set_xlabel(r'$\lambda$')
    ax.set_xlabel(r'Wavelength $[\mathrm{\AA]}$', fontsize = 40)
    #ax.set_ylabel(r'Magnitude [AB]', fontsize = 26)
    #ax.set_ylabel(r'Flux $(\mathrm{6^{-16} erg s^{-1} cm^{-2} \AA^{-1}})$', fontsize = 26)
    ax.set_ylabel(r'Flux $(\mathrm{10^{-15} erg\ s^{-1} cm^{-2} \AA^{-1}})$', fontsize = 38)
    ax.plot(x, y, linewidth=2.8, color="black", alpha = 0.6)
    # ax.plot(x1, y1+4.5, linewidth=2.3, color="black")
    #ax.plot(x2, y2, linewidth=2.3, color="black")
    for wl1, mag, colors, marker_ in zip(wl, magnitude, color, marker):       #
        F = (10**(-(mag + 2.41) / 2.5)) / wl1**2
        F /=1e-15
        # print(F)
        # print(y+7)
        ax.scatter(wl1, F, c = colors, marker=marker_, s=400, zorder=3)
    # for wl1, mag1, colors, marker_ in zip(wl, magnitude1, color, marker):       #
    #     F1 = 10**-(mag1+2.41) / 2.5
    #     F1 /= 0.21e19 #0.295e19
    #     ax.scatter(wl1, F1+4.3, c = colors, marker=marker_, s=400, zorder=2)
    # for wl1, mag2, colors, marker_ in zip(wl, magnitude2, color, marker):       #
    #     F2 = 10**(-(mag2+2.41) / 2.5)
    #     F2 /= 1.2e8 #1.3-6
    #     ax.scatter(wl1, F2+0.9, c = colors, marker=marker_, s=400, zorder=2)

    #plt.subplots_adjust(bottom=0.19)
    # plt.text(0.75, 0.74, 'QSO (z=2.3)',
    #          transform=ax.transAxes, fontsize="xx-large", weight='bold')
    # plt.text(0.75, 0.43, 'Star (A0)',
    #          transform=ax.transAxes, fontsize="xx-large", weight='bold')
    # plt.text(0.75, 0.25, 'Galaxy (z=0.0)',
    #          transform=ax.transAxes, fontsize="xx-large", weight='bold')
    plt.legend(fontsize=20.0)
    #plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig(plotfile)
    plt.clf()

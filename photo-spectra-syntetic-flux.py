'''
Make photo spectra from convolved JPLUS spectra
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

magnitude= []
magnitude1= []
magnitude2= []
wl = [3485, 3785, 3950, 4100, 4300, 4803, 5150, 6250, 6600, 7660, 8610, 9110]
color= ["#CC00FF", "#9900FF", "#6600FF", "#0000FF", "#009999", "#006600", "#DD8000", "#FF0000", "#CC0066", "#990033", "#660033", "#330034"]
marker = ["s", "o", "o", "o", "o", "s", "o", "s", "o", "s", "o", "s"]

parser = argparse.ArgumentParser(
    description="""Write wave and magnitude of a spectrum""")

parser.add_argument("source", type=str,
                    default="DdDm-1-HPNe-JPLUS17-magnitude",
                    help="Name of source, taken the prefix ")
parser.add_argument("source1", type=str,
                    default="DdDm-1-HPNe-JPLUS17-magnitude",
                    help="Name of source, taken the prefix ")
parser.add_argument("source2", type=str,
                    default="DdDm-1-HPNe-JPLUS17-magnitude",
                    help="Name of source, taken the prefix ")

parser.add_argument("--savefig", action="store_true",
                    help="Save a figure showing the magnitude")

parser.add_argument("--debug", action="store_true",
                    help="Print out verbose debugging info about each line in region file")

args = parser.parse_args()
file_ = args.source + ".json"
file_1 = args.source1 + ".json"
file_2 = args.source2 + ".json"

c = 2.99792458e18 #speed of light in Angstron/sec
with open(file_) as f:
    data = json.load(f)
    magnitude.append(data["F348_U"])
    magnitude.append(data["F378"])
    magnitude.append(data["F395"])
    magnitude.append(data["F410"])
    magnitude.append(data["F430"])
    magnitude.append(data["F480_G"])
    magnitude.append(data["F515"]) 
    magnitude.append(data["F625_R"]) 
    magnitude.append(data["F660"])
    magnitude.append(data["F766_I"]) 
    magnitude.append(data["F861"]) 
    magnitude.append(data["F911_Z"])

with open(file_1) as f1:
    data1 = json.load(f1)
    magnitude1.append(data1["F348_U"])
    magnitude1.append(data1["F378"])
    magnitude1.append(data1["F395"])
    magnitude1.append(data1["F410"])
    magnitude1.append(data1["F430"])
    magnitude1.append(data1["F480_G"])
    magnitude1.append(data1["F515"]) 
    magnitude1.append(data1["F625_R"]) 
    magnitude1.append(data1["F660"])
    magnitude1.append(data1["F766_I"]) 
    magnitude1.append(data1["F861"]) 
    magnitude1.append(data1["F911_Z"])

with open(file_2) as f2:
    data2 = json.load(f2)
    magnitude2.append(data2["F348_U"])
    magnitude2.append(data2["F378"])
    magnitude2.append(data2["F395"])
    magnitude2.append(data2["F410"])
    magnitude2.append(data2["F430"])
    magnitude2.append(data2["F480_G"])
    magnitude2.append(data2["F515"]) 
    magnitude2.append(data2["F625_R"]) 
    magnitude2.append(data2["F660"])
    magnitude2.append(data2["F766_I"]) 
    magnitude2.append(data2["F861"]) 
    magnitude2.append(data2["F911_Z"])

# Spectrum
def sys(spectra):
    file_ = spectra
    x = np.loadtxt(file_, delimiter = None, skiprows = 0, usecols = None,
                   unpack = False, dtype = np.dtype([('Wl', '|f8'), ('Flux', 'f8')]))
    return x['Wl'], x['Flux']

x, y = sys("DdDm-1.dat")
y /= 1e-13
#x, y = sys("DdDm-1.dat")
# x1, y1 = sys("star.dat")
# y1 /= 1e-6 
# x2, y2 = sys("galaxy.sed")
# print(y2)
#y2 /= 1e-8

if args.savefig:
    plotfile = file_.replace(".json", 
                    "-flux.jpg")
    fig = plt.figure(figsize=(14.29, 9))
    ax = fig.add_subplot(1,1,1)
    plt.tick_params(axis='x', labelsize=40) 
    plt.tick_params(axis='y', labelsize=35)
    ax.set_xlim(xmin=3e3,xmax=9700)
    ax.set_ylim(ymin=-0.17,ymax=4.0)
    #ax.set_ylim(ymin=-0.1,ymax=1e-10)
    #ax.set_ylim(ymin=0,ymax=12.3)
    #ax1.set_xlabel(r'$\lambda$')
    ax.set_xlabel(r'Wavelength $[\mathrm{\AA]}$', fontsize = 40)
    #ax.set_ylabel(r'Magnitude [AB]', fontsize = 26)
    #ax.set_ylabel(r'Flux $(\mathrm{6^{-16} erg s^{-1} cm^{-2} \AA^{-1}})$', fontsize = 26)
    ax.set_ylabel(r'Flux $(\mathrm{10^{-13} erg\ s^{-1} cm^{-2} \AA^{-1}})$', fontsize = 38)
    ax.plot(x, y, linewidth=3.0, color="black", alpha = 0.6)
    # ax.plot(x1, y1+4.5, linewidth=2.3, color="black")
    # ax.plot(x2, y2, linewidth=2.3, color="black")
    for wl1, mag, colors, marker_ in zip(wl, magnitude, color, marker):       #
        F = (10**(-(mag + 2.41) / 2.5)) / wl1**2
        F /=1e-13
        # print(F)
        # print(y+7)
        ax.scatter(wl1, F, c = colors, marker=marker_, s=400, zorder=3)

    #plt.subplots_adjust(bottom=0.19)
    # plt.text(0.75, 0.94, 'QSO (z=2.3)',
    #          transform=ax.transAxes, fontsize=25, weight='bold')
    # plt.text(0.75, 0.68, 'Star (A0)',
    #          transform=ax.transAxes, fontsize=25, weight='bold')
    # plt.text(0.71, 0.25, 'Galaxy (z=0.0)',
    #          transform=ax.transAxes, fontsize=25, weight='bold')
    plt.legend(fontsize=20.0)
    #plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig(plotfile)
    plt.clf()



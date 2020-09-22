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

#mag_auto = []
mag_petro = []
mag_aper = []
wl = [3485, 3785, 3950, 4100, 4300, 4803, 5150, 6250, 6600, 7660, 8610, 9110]
color= ["#CC00FF", "#9900FF", "#6600FF", "#0000FF", "#009999", "#006600", "#DD8000", "#FF0000", "#CC0066", "#990033", "#660033", "#330034"]
marker = ["s", "o", "o", "o", "o", "s", "o", "s", "o", "s", "o", "s"]

# wl = [ 3785, 3950, 4100, 4300, 4803, 5150, 6250, 6600, 7660, 8610, 9110]
# color= [ "#9900FF", "#6600FF", "#0000FF", "#009999", "#006600", "#DD8000", "#FF0000", "#CC0066", "#990033", "#660033", "#330034"]
# marker = [ "o", "o", "o", "o", "s", "o", "s", "o", "s", "o", "s"]


# wl1 = [3485, 3785, 3950, 4100, 4300, 4803, 5150, 6250, 6600, 7660, 9110]
# color1= ["#CC00FF", "#9900FF", "#6600FF", "#0000FF", "#009999", "#006600", "#DD8000", "#FF0000", "#CC0066", "#990033", "#330034"]
# marker1 = ["s", "o", "o", "o", "o", "s", "o", "s", "o", "s", "s"]

wl1 = [3485, 3785, 4803, 5150, 6250, 6600, 7660, 8610, 9110]
color1= ["#CC00FF", "#9900FF", "#006600", "#DD8000", "#FF0000", "#CC0066", "#990033", "#660033", "#330034"]
marker1 = ["s", "o",  "s", "o", "s", "o", "s", "o", "s"]

wl2 = [3485,  4803, 6250, 6600, 7660, 8610, 9110]
color2= ["#CC00FF",  "#006600",  "#FF0000", "#CC0066", "#990033", "#660033", "#330034"]
marker2 = ["s", "s", "s", "o", "s", "o", "s"]

wl3 = [3485, 3785,  4300, 4803,  6250, 6600, 7660, 8610, 9110]
color3= ["#CC00FF", "#9900FF",  "#009999", "#006600", "#FF0000", "#CC0066", "#990033", "#660033", "#330034"]
marker3 = ["s", "o",  "o", "s",  "s", "o", "s", "o", "s"]

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
file_ = args.source + ".tab"

data = Table.read(file_, format="ascii.tab")

n = 2
mag_auto  = [[] for _ in range(n)]

for i in range(2):
    mag_auto[i].append(float(data["uJAVA"][i]))
    mag_auto[i].append(float(data["J0378"][i]))
    mag_auto[i].append(float(data["J0395"][i]))
    mag_auto[i].append(float(data["J0410"][i]))
    mag_auto[i].append(float(data["J0430"][i]))
    mag_auto[i].append(float(data["gSDSS"][i]))
    mag_auto[i].append(float(data["J0515"][i])) 
    mag_auto[i].append(float(data["rSDSS"][i])) 
    mag_auto[i].append(float(data["J0660"][i]))
    mag_auto[i].append(float(data["iSDSS"][i])) 
    mag_auto[i].append(float(data["J0861"][i])) 
    mag_auto[i].append(float(data["zSDSS"][i]))

    plotfile = "photospectrum_"+str(data["Id"][i])+"_auto-IAU.jpg"
    fig = plt.figure(figsize=(14, 9))
    ax = fig.add_subplot(1,1,1)
    plt.tick_params(axis='x', labelsize=26) 
    plt.tick_params(axis='y', labelsize=26)
    #ax.set_ylim(ymin=17.5,ymax=23)
    #ax1.set_xlabel(r'$\lambda$')
    ax.set_xlabel(r'Wavelength $[\mathrm{\AA]}$', fontsize = 26)
    ax.set_ylabel(r'Magnitude [AB]', fontsize = 26)
    ax.plot(wl, mag_auto[i], '-r')#, label='Auto')
    print(mag_auto[i])
    for wl1, mag, colors, marker_ in zip(wl, mag_auto[i], color, marker):
        ax.scatter(wl1, mag, color = colors, marker=marker_, s=400, zorder=2)
    plt.subplots_adjust(bottom=0.19)
    plt.legend(fontsize=20.0)
    plt.tight_layout()
    plt.gca().invert_yaxis()
    plt.savefig(plotfile)
    plt.clf()

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

mag_auto = []
mag_petro = []
mag_aper = []
wl = [3485, 3785, 3950, 4100, 4300, 4803, 5150, 6250, 6600, 7660, 8610, 9110]
color= ["#CC00FF", "#9900FF", "#6600FF", "#0000FF", "#009999", "#006600", "#DD8000", "#FF0000", "#CC0066", "#990033", "#660033", "#330034"]
marker = ["s", "o", "o", "o", "o", "s", "o", "s", "o", "s", "o", "s"]

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

mag_auto.append(float(data["uJAVA"]))
mag_auto.append(float(data["J0378"]))
mag_auto.append(float(data["J0395"]))
mag_auto.append(float(data["J0410"]))
mag_auto.append(float(data["J0430"]))
mag_auto.append(float(data["gSDSS"]))
mag_auto.append(float(data["J0515"])) 
mag_auto.append(float(data["rSDSS"])) 
mag_auto.append(float(data["J0660"]))
mag_auto.append(float(data["iSDSS"])) 
mag_auto.append(float(data["J0861"])) 
mag_auto.append(float(data["zSDSS"]))

#Petro
mag_petro.append(float(data["uJAVA_petro"]))
mag_petro.append(float(data["J0378_petro"]))
mag_petro.append(float(data["J0395_petro"]))
mag_petro.append(float(data["J0410_petro"]))
mag_petro.append(float(data["J0430_petro"]))
mag_petro.append(float(data["gSDSS_petro"]))
mag_petro.append(float(data["J0515_petro"])) 
mag_petro.append(float(data["rSDSS_petro"])) 
mag_petro.append(float(data["J0660_petro"]))
mag_petro.append(float(data["iSDSS_petro"])) 
mag_petro.append(float(data["J0861_petro"])) 
mag_petro.append(float(data["zSDSS_petro"]))

#Aper
mag_aper.append(float(data["uJAVA_aper"]))
mag_aper.append(float(data["J0378_aper"]))
mag_aper.append(float(data["J0395_aper"]))
mag_aper.append(float(data["J0410_aper"]))
mag_aper.append(float(data["J0430_aper"]))
mag_aper.append(float(data["gSDSS_aper"]))
mag_aper.append(float(data["J0515_aper"])) 
mag_aper.append(float(data["rSDSS_aper"])) 
mag_aper.append(float(data["J0660_aper"]))
mag_aper.append(float(data["iSDSS_aper"])) 
mag_aper.append(float(data["J0861_aper"])) 
mag_aper.append(float(data["zSDSS_aper"]))

print(mag_aper)
if args.savefig:
    plotfile = file_.replace(".tab", 
                    "-auto.jpg")
    fig = plt.figure(figsize=(14, 9))
    ax = fig.add_subplot(1,1,1)
    plt.tick_params(axis='x', labelsize=26) 
    plt.tick_params(axis='y', labelsize=26)
    #ax.set_ylim(ymin=17.5,ymax=23)
    #ax1.set_xlabel(r'$\lambda$')
    ax.set_xlabel(r'Wavelength $[\mathrm{\AA]}$', fontsize = 26)
    ax.set_ylabel(r'Magnitude [AB]', fontsize = 26)
    
    ax.plot(wl1, mag_auto, '-r', label='Auto')
    for wl1, mag, colors, marker_ in zip(wl1, mag_auto, color1, marker1):
        ax.scatter(wl1, mag, color = colors, marker=marker_, s=400, zorder=2)
    plt.subplots_adjust(bottom=0.19)
    plt.legend(fontsize=20.0)
    plt.tight_layout()
    plt.gca().invert_yaxis()
    plt.savefig(plotfile)
    plt.clf()

    plotfile1 = file_.replace(".tab", 
                    "-petro.jpg")
    fig = plt.figure(figsize=(14, 9))
    ax1 = fig.add_subplot(1,1,1)
    plt.tick_params(axis='x', labelsize=26) 
    plt.tick_params(axis='y', labelsize=26)
    #ax1.set_ylim(ymin=17.5,ymax=23)
    #ax1.set_xlabel(r'$\lambda$')
    ax1.set_xlabel(r'Wavelength $[\mathrm{\AA]}$', fontsize = 26)
    ax1.set_ylabel(r'Magnitude [AB]', fontsize = 26)
    ax1.plot(wl2, mag_petro, '-b', label='Petro')
    for wl1, mag, colors, marker_ in zip(wl2, mag_petro, color2, marker2):
        ax1.scatter(wl1, mag, color = colors, marker=marker_, s=400, zorder=2)
    plt.subplots_adjust(bottom=0.19)
    plt.legend(fontsize=20.0)
    plt.tight_layout()
    plt.gca().invert_yaxis()
    plt.savefig(plotfile1)
    plt.clf()

    plotfile2 = file_.replace(".tab", 
                    "-aper.jpg")
    fig = plt.figure(figsize=(14, 9))
    ax2 = fig.add_subplot(1,1,1)
    plt.tick_params(axis='x', labelsize=26) 
    plt.tick_params(axis='y', labelsize=26)
    #ax2.set_ylim(ymin=17.5,ymax=23)
    #ax1.set_xlabel(r'$\lambda$')
    ax2.set_xlabel(r'Wavelength $[\mathrm{\AA]}$', fontsize = 26)
    ax2.set_ylabel(r'Magnitude [AB]', fontsize = 26)
    ax2.plot(wl3, mag_aper, '-g', label='Aper')
    for wl1, mag, colors, marker_ in zip(wl3, mag_aper, color3, marker3):
        ax2.scatter(wl1, mag, color = colors, marker=marker_, s=400, zorder=2)
    plt.subplots_adjust(bottom=0.19)
    plt.legend(fontsize=20.0)
    plt.tight_layout()
    plt.gca().invert_yaxis()
    plt.savefig(plotfile2)
    plt.clf()

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
import itertools

magnitude= []
magnitude1= []
wl = [3485, 3785, 3950, 4100, 4300, 4803, 5150, 6250, 6600, 7660, 8610, 9110]
color= itertools.cycle(["#0000FF", "#5F9EA0", "#8EE5EE", "#008000", "#FFFF00", "#FFA54F", "#8B5A2B", "#FA8072", "#FF0000", "#A52A2A", "#8B3E2F", "#800000"])
marker = ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o"]


parser = argparse.ArgumentParser(
    description="""Write wave and magnitude of a spectrum""")

parser.add_argument("source", type=str,
                    default="DdDm-1-HPNe-JPLUS17-magnitude",
                    help="Name of source, taken the prefix ")
parser.add_argument("source1", type=str,
                    default="DdDm-1-HPNe-JPLUS17-magnitude",
                    help="Name of source, taken the prefix ")

parser.add_argument("--savefig", action="store_true",
                    help="Save a figure showing the magnitude")

parser.add_argument("--debug", action="store_true",
                    help="Print out verbose debugging info about each line in region file")

args = parser.parse_args()
file_ = args.source + ".json"
file_1 = args.source1 + ".json"

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

# Spectrum
def sys(spectra):
    file_ = spectra
    x = np.loadtxt(file_, delimiter = None, skiprows = 0, usecols = None,
                   unpack = False, dtype = np.dtype([('Wl', '|f8'), ('Flux', 'f8')]))
    return x['Wl'], x['Flux']

x, y = sys("DdDm-1.dat")
y /=10e-13

x1, y1 = sys("LHa_115_N_67_1996.txt")

y1 /=10e-15 #0.4-14

#FILTERS####################################################
colors= itertools.cycle(["#5F9EA0", "#8EE5EE", "#008000", "#FFFF00", "#8B5A2B",  "#FF0000", "#8B3E2F",])
colors1= itertools.cycle(["#0000FF", "#FFA54F",  "#FA8072",  "#A52A2A", "#800000"])
def load_file(filename):
    datadir = "../filters/splus-filter-2018/filter_curves-master/"
    file_ = filename
    wll, ress = [], []
    data = np.loadtxt(os.path.join(datadir, file_), delimiter=None, converters=None, skiprows=0,
                                       usecols=None, unpack=False, ndmin=0)
    for i in data:
        wl = str(i[0])
        res = str(i[1]*50)
        wll.append(wl)
        ress.append(res)
        return wll, ress

files = [ 'F378.dat', 'F395.dat', 
'F410.dat', 'F430.dat', 
'F515.dat', 'F660.dat',  'F861.dat']

files1 = ['U.dat', 'G.dat',  'R.dat', 'I.dat', 'Z.dat']

###################################################################

F_ = []
if args.savefig:
    plotfile = file_.replace(".json", 
                    ".pdf")
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(1,1,1)
    plt.tick_params(axis='x', labelsize=20) 
    plt.tick_params(axis='y', labelsize=20)
    ax.set_xlim(xmin=3000,xmax=9700)
    #ax.set_ylim(ymin=-0.1,ymax=1e-10)
    #ax.set_ylim(ymin=-1.5,ymax=14.0)
    #ax.set_ylim(ymin=-1.5,ymax=10.9)
    ax.set_ylim(ymin=0.0,ymax=6.5)
    #ax1.set_xlabel(r'$\lambda$')
    ax.set_xlabel(r'Wavelength $[\mathrm{\AA]}$', fontsize = 22)
    #ax.set_ylabel(r'Magnitude [AB]', fontsize = 26)
    #ax.set_ylabel(r'$\mathrm{F_{\lambda} (10^{-14} erg}$ $\mathrm{s^{-1} cm^{-2} \AA^{-1}})$', fontsize = 26)
    ax.set_ylabel(r'Normalized Flux + Const.', fontsize = 22)
    #ax.plot(x, y+44.0, linewidth=3.0, color="black")
    ax.plot(x, y+4.8, linewidth=3.0, color="black")
    for wl1, mag, colors, marker_ in zip(wl, magnitude, color, marker):       #
        F = (10**(-(mag + 2.41) / 2.5)) / wl1**2
        F_.append(F)
        #F /= 1.2e-06 #1.3-6
    #   F /= 20e-07 #1.3-6
        F /= 10e-13
        ax.scatter(wl1, F+4.8, color=colors, marker=marker_, s=170, edgecolor='black', zorder=3) #zorder The default drawing order for axes is patches, lines, text. This order is determined by the zorder attribute. The following defaults are set
    #ax.plot(x1, y1+2.0, linewidth=3.0, color="black")
    ax.plot(x1, y1+0.5, linewidth=3.0, color="black")
    for wl1, mag1, colors, marker_ in zip(wl, magnitude1, color, marker):       #
        F1 = (10**(-(mag1+2.41) / 2.5)) / wl1**2
        print(F1)
        #F1 /= 2.1e-07 #1.3-6
        #F1 /= 0.5e-7 #0.5e-7
        F1 /= 10e-15
        ax.scatter(wl1, F1+0.5, color = colors, marker=marker_, s=170, edgecolor='black', zorder=3)
    plt.subplots_adjust(bottom=0.19)
    plt.text(0.89, 0.78, 'PN',
             transform=ax.transAxes, fontsize=22)
    plt.text(0.65, 0.17, 'Symbiotic Star',
             transform=ax.transAxes, fontsize=22)

    plt.legend(fontsize=20.0)
    #plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig(plotfile)
    plt.clf()

#Save files with flux
asciifile = "DdDm1-PN-SPLUS.dat"
file=open(asciifile,'w') #create file  
for x,y in zip(wl, F_):  
    file.write('%f  %s\n'%(x,y))     #assume you separate columns by tabs  
file.close()     #close file  
    
F1_ = []
if args.savefig:
    #symbiotic
    plotfile = file_1.replace(".json", 
                    "-zoom.pdf")
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    plt.tick_params(axis='x', labelsize=22) 
    plt.tick_params(axis='y', labelsize=22)
    ax.set_xlim(xmin=3000,xmax=9700)
    #ax.set_ylim(ymin=-0.1,ymax=1e-10)
    ax.set_ylim(ymin=-0.5,ymax=10.0)
    #ax1.set_xlabel(r'$\lambda$')
    ax.set_xlabel(r'Wavelength $[\mathrm{\AA]}$', fontsize = 26)
    #ax.set_ylabel(r'Magnitude [AB]', fontsize = 26)
    ax.set_ylabel(r'$\mathrm{F_{\lambda} (10^{-16} erg}$ $\mathrm{s^{-1} cm^{-2} \AA^{-1}})$', fontsize = 26)
    colors= itertools.cycle(["#5F9EA0", "#8EE5EE", "#008000", "#FFFF00", "#8B5A2B",  "#FF0000", "#8B3E2F",])
    colors1= itertools.cycle(["#0000FF", "#FFA54F",  "#FA8072",  "#A52A2A", "#800000"])
    ax.plot(x1, y1, linewidth=2.3, color="black")
    for wl1, mag1, colors, marker_ in zip(wl, magnitude1, color, marker):       #
        F1 = (10**(-(mag1+2.41) / 2.5)) / wl1**2
        F1_.append(F1)
        #F1 /= 2.1e-07 #1.3-6
        #F1 /= 0.5e-7 #0.5e-7
        F1 /= 10e-16
        ax.scatter(wl1, F1, c = colors, marker=marker_, s=190, zorder=3)

    plt.subplots_adjust(bottom=0.19)
    # plt.text(0.89, 0.56, 'PN',
    #          transform=ax.transAxes, fontsize=25, weight='bold')
    # plt.text(0.70, 0.19, 'Symbiotic Star',
    #          transform=ax.transAxes, fontsize=25, weight='bold')

    plt.legend(fontsize=20.0)
    #plt.gca().invert_yaxis()
    plt.tight_layout()
    #plt.savefig(plotfile)
    plt.clf()

#Save files with flux
asciifile = "LHa_115_N_67_1996-SySt-SPLUS.dat"
file=open(asciifile,'w') #create file  
for x,y in zip(wl, F1_):  
    file.write('%f  %s\n'%(x,y))     #assume you separate columns by tabs  
file.close()     #close file  

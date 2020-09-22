
'''
Make photo spectra from convolved J-PAS spectra
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
from collections import OrderedDict
import matplotlib.cm as cm
from astropy.io import fits

magnitude= []
wl = [3495, 3781, 3900, 4000, 4100, 4200, 4301, 4400, 4501, 4600, 4701, 4801, 4900, 5001, 5101, 5201, 5300, 5400, 5500, 5600, 5700, 5799, 5898,  5999, 6098, 6199, 6300, 6401, 6500, 6600, 6700, 6800, 6900, 7000, 7100, 7200, 7300, 7400, 7500, 7600, 7700, 7800, 7900, 8000, 8100, 8201, 8300, 8400, 8500, 8600, 8700, 8800, 8900, 9000, 9100, 9669]
color= ["#CC00FF", "#9900FF", "#6600FF", "#0000FF", "#009999", "#006600", "#DD8000", "#FF0000", "#CC0066", "#990033", "#660033", "#330034"]
marker = ["s", "o", "o", "o", "o", "s", "o", "s", "o", "s", "o", "s"]


parser = argparse.ArgumentParser(
    description="""Write wave and magnitude of a spectrum""")

parser.add_argument("source", type=str,
                    default="DdDm-1-HPNe-JPAS17-magnitude",
                    help="Name of source, taken the prefix ")

parser.add_argument("--savefig", action="store_true",
                    help="Save a figure showing the magnitude")

parser.add_argument("--debug", action="store_true",
                    help="Print out verbose debugging info about each line in region file")

args = parser.parse_args()
file_list = args.source + ".json"
with open(file_list) as f:
    data = json.load(f)
    data = OrderedDict((k, v) for k, v in sorted(data.items(), key=lambda x: x[0]))
    for k in data.keys():
        if k.startswith('Jv0915'):
            imagename=k
            magnitude.append(data[imagename])

#Color of the points
colors = cm.rainbow(np.linspace(0, 1, len(magnitude)))

# Spectrum
def sys(spectra):
    file_ = spectra
    try:
        x = np.loadtxt(file_, delimiter = None, skiprows = 0, usecols = None,
                   unpack = False, dtype = np.dtype([('Wl', '|f8'), ('Flux', 'f8')]))
        return x['Wl'], x['Flux']
    except UnicodeDecodeError:             #Spectra from SDSS
        hdulist = fits.open(file_)
        return 10**hdulist[1].data.field('loglam'), 1E-17*hdulist[1].data.field('flux')

#x, y = sys("DdDm-1.dat")
#x, y = sys("LMC1.txt")
x, y = sys("H-9b.0042+r.dat")
#x, y = sys("spec-0377-52145-0540-catB.dat")
#x, y = sys("Sz83.dat")
#x, y = sys("spec-2967-54584-0410.fits") #SFG
#x, y = sys("slit9b+r.dat") #Exter PN
#x, y = sys("th351fim.dat")
#x, y = sys("spec-0844-52378-0041.fits")

# m=x>=3731.        #
# x, y = x[m], y[m] # Be stars
y /=1.e-15

#FITS file
# Spectrum from SLOAN
# hdulist = fits.open("spec-0416-51811-0427.fits")
# y = 1E-17*hdulist[1].data.field('flux')
# x = 10**hdulist[1].data.field('loglam')
# y /= 1E-15

#print(data)
font = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 16,
        }
    
if args.savefig:
    plotfile = file_list.replace(".json", 
                    "-flux.pdf")
    fig = plt.figure(figsize=(17.8, 11.8))
    ax1 = fig.add_subplot(1,1,1)
    plt.tick_params(axis='x', labelsize=48) 
    plt.tick_params(axis='y', labelsize=48)
    ax1.set_xlim(3e3, 10e3)
    ax1.set_ylim(-0.01, 0.7)
    #ax1.set_ylim(ymin=15,y4ax=-5)
    #ax1.set_xlabel(r'$\lambda$')
    ax1.set_xlabel(r'Wavelength $[\mathrm{\AA]}$', fontsize = 56)
    ax1.set_ylabel(r'Flux $(\mathrm{10^{-15} erg\ s^{-1} cm^{-2} \AA^{-1}})$', fontsize = 45)
    ax1.plot(x, y, linewidth=3.0, color="black", alpha = 0.6)
    for wl, mag, colorss in zip(wl, magnitude, colors):
        F = (10**(-(mag + 2.41) / 2.5)) / wl**2
        F /=1.e-15
        ax1.scatter(wl, F, color = colorss, marker='o',  cmap=plt.cm.hot, edgecolor='black', s=200, zorder=10)
    # plt.text(0.68, 0.86, 'Halo PN',
    #          transform=ax1.transAxes, fontsize=60,  fontdict=font)
    # plt.text(0.80, 0.86, 'SySt',
    #          transform=ax1.transAxes, fontsize=60,  fontdict=font)
    plt.text(0.64, 0.86, 'H II region',
            transform=ax1.transAxes, fontsize=60,  fontdict=font)
    # plt.text(0.76, 0.86, 'QSO',                                   #
    #         transform=ax1.transAxes, fontsize=60,  fontdict=font)  #
    # plt.text(0.76, 0.76, 'z = 1.4',                               #QSO
    #         transform=ax1.transAxes, fontsize=60,  fontdict=font)  #
    # plt.text(0.80, 0.86, 'YSO',
    #          transform=ax1.transAxes, fontsize=60,  fontdict=font)
    # plt.text(0.80, 0.86, 'CV',
    #            transform=ax1.transAxes, fontsize=60,  fontdict=font)
    # plt.text(0.80, 0.86, 'SFG',
    #           transform=ax1.transAxes, fontsize=60,  fontdict=font)
    # plt.text(0.03, 0.89, 'CLOUDY modelled halo PN',
    #          transform=ax1.transAxes, fontsize=31,  fontdict=font)
    # plt.text(0.03, 0.79, '$\mathrm{T_{eff}} = 200 \mathrm{X} 10^3$ K',
    #          transform=ax1.transAxes, fontsize=31,  fontdict=font)
    # plt.text(0.03, 0.69, '$\mathrm{L} = 10 \mathrm{X} 10^3 \mathrm{L_{\odot}}$',
    #          transform=ax1.transAxes, fontsize=31,  fontdict=font)
    # plt.text(0.03, 0.59, '$\mathrm{N_{e}} = 6 \mathrm{X} 10^3 \mathrm{cm^{-3}}$ ',
    #          transform=ax1.transAxes, fontsize=31,  fontdict=font)

    # plt.text(0.05, 0.35, 'CLOUDY modelled halo PN',
    #          transform=ax1.transAxes, fontsize=31,  fontdict=font)
    # plt.text(0.05, 0.25, '$\mathrm{T_{eff}} = 60 \mathrm{X} 10^3 $ K',
    #          transform=ax1.transAxes, fontsize=31,  fontdict=font)
    # plt.text(0.05, 0.15, '$\mathrm{L} = 10 \mathrm{X} 10^3 \mathrm{L_{\odot}}$',
    #          transform=ax1.transAxes, fontsize=31,  fontdict=font)
    # plt.text(0.05, 0.05, '$\mathrm{N_{e}} = 1 \mathrm{X} 10^3 \mathrm{cm^{-3}}$ ',
    #          transform=ax1.transAxes, fontsize=31,  fontdict=font)

    # plt.text(0.68, 0.86, 'QSO',                                   #
    #         transform=ax1.transAxes, fontsize=41,  fontdict=font)  #
    # plt.text(0.68, 0.78, 'z = 2.5',                               #QSO
    #         transform=ax1.transAxes, fontsize=41,  fontdict=font)  #

    # plt.text(0.75, 0.86, 'QSO',                                   #
    #         transform=ax1.transAxes, fontsize=41,  fontdict=font)  #
    # plt.text(0.75, 0.78, 'z = 3.3',                               #QSO
    #         transform=ax1.transAxes, fontsize=41,  fontdict=font)  #
    # plt.text(0.48, 0.86, 'PN of NGC 205 ',
    #          transform=ax1.transAxes, fontsize=60,  fontdict=font)

    # for wl1, mag, colors, marker_ in zip(wl, magnitude, color, marker):
    #     ax1.scatter(wl1, mag, color = colors, marker=marker_, s=400, zorder=2)
    # plt.text(0.65, 0.86, 'H II galaxy',
    #          transform=ax1.transAxes, fontsize=60,  fontdict=font)
    # plt.text(0.70, 0.86, 'B[e] star',
    #            transform=ax1.transAxes, fontsize=60,  fontdict=font)

    plt.legend(fontsize=20.0)
    #plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.tight_layout()
    save_path = '../../../Dropbox/JPAS/Tesis/Fig'
    file_save = os.path.join(save_path, plotfile)
    plt.savefig(file_save)
    plt.clf()

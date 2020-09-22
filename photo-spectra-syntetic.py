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
#magnitude1= []
wl = [3485, 3785, 3950, 4100, 4300, 4803, 5150, 6250, 6600, 7660, 8610, 9110]
color= ["#CC00FF", "#9900FF", "#6600FF", "#0000FF", "#009999", "#006600", "#DD8000", "#FF0000", "#CC0066", "#990033", "#660033", "#330034"]
marker = ["s", "o", "o", "o", "o", "s", "o", "s", "o", "s", "o", "s"]

# wl = [3785, 3950, 4100, 4300, 4803, 5150, 6250, 6600, 7660, 8610, 9110]
# color= ["#9900FF", "#6600FF", "#0000FF", "#009999", "#006600", "#DD8000", "#FF0000", "#CC0066", "#990033", "#660033", "#330034"]
# marker = ["o", "o", "o", "o", "s", "o", "s", "o", "s", "o", "s"]


parser = argparse.ArgumentParser(
    description="""Write wave and magnitude of a spectrum""")

parser.add_argument("source", type=str,
                    default="DdDm-1-HPNe-JPLUS17-magnitude",
                    help="Name of source, taken the prefix ")

# parser.add_argument("source1", type=str,
#                     default="DdDm-1-HPNe-SPLUS-magnitude",
#                     help="Name of source, taken the prefix ")

parser.add_argument("--savefig", action="store_true",
                    help="Save a figure showing the magnitude")

parser.add_argument("--debug", action="store_true",
                    help="Print out verbose debugging info about each line in region file")

args = parser.parse_args()
file_ = args.source + ".json"

# args1 = parser.parse_args()
# file_1 = args1.source1 + ".json"

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

#known PN observed by J-PLUS
# with open(file_) as f:
#     data = json.load(f)
#     magnitude.append(data["J0348_uJAVA"]-25+20.996)
#     magnitude.append(data["J0378"]-25+20.376)
#     magnitude.append(data["J0395"]-25+20.130)
#     magnitude.append(data["J0410"]-25+21.102)
#     magnitude.append(data["J0430"]-25+21.218)
#     magnitude.append(data["J0480_gSDSS"]-25+23.425)
#     magnitude.append(data["J0515"]-25+21.444)
#     magnitude.append(data["J0625_rSDSS"]-25+23.565)
#     magnitude.append(data["J0660"]-25+21.058)
#     magnitude.append(data["J0766_iSDSS"]-25+23.255)
#     magnitude.append(data["J0861"]-25+21.534)
#     magnitude.append(data["J0911_zSDSS"]-25+22.535)

#SPLUS
# with open(file_) as f:
#     data = json.load(f)
#     magnitude.append(data["F348_U"])
#     magnitude.append(data["F378"])
#     magnitude.append(data["F395"])
#     magnitude.append(data["F410"])
#     magnitude.append(data["F430"])
#     magnitude.append(data["F480_G"])
#     magnitude.append(data["F515"]) 
#     magnitude.append(data["F625_R"]) 
#     magnitude.append(data["F660"])
#     magnitude.append(data["F766_I"]) 
#     magnitude.append(data["F861"]) 
#     magnitude.append(data["F911_Z"])


# Spectrum
# def sys(spectra):
#     file_ = spectra
#     x = np.loadtxt(file_, delimiter = None, skiprows = 0, usecols = None,
#                    unpack = False, dtype = np.dtype([('Wl', '|f8'), ('Flux', 'f8')]))
#     return x['Wl'], x['Flux']

#x, y = sys("Lin358.txt")
# x, y = sys("DdDm-1.dat")

# y /=10e-15
#y1 /=1e-16

#sys
# x1, y1 = sys("LHa_115_N_67_1996.txt")
# print(y1)
# y1 /=10e-16 #0.4-14
font = {'family': 'serif',
        'color':  'black',
        'weight': 'normal',
        'size': 16,
        }


if args.savefig:
    plotfile = file_.replace(".json", 
                    "-paper.pdf")
    #fig = plt.figure(figsize=(14.29, 9)) #figsize=(14, 9)
    fig = plt.figure(figsize=(15.8, 9.8)) #para cv
    ax = fig.add_subplot(1,1,1)
    plt.tick_params(axis='x', labelsize=44) 
    plt.tick_params(axis='y', labelsize=44)
    ax.set_xlim(xmin=3000, xmax=9700)
    #ax.set_ylim(ymin=-0.5,ymax=25)
    #ax1.set_ylim(ymin=15,ymax=-5)
    #ax1.set_xlabel(r'$\lambda$')
    ax.set_xlabel(r'Wavelength $[\mathrm{\AA]}$', fontsize = 48)
    ax.set_ylabel(r'Magnitude [AB]', fontsize = 48)
    #ax.set_ylabel(r'Flux $(\mathrm{6^{-16} erg s^{-1} cm^{-2} \AA^{-1}})$', fontsize = 26)
    #plt.plot(x, y, linewidth=2.3, color="black")
    #plt.plot(x1, y1, linewidth=2.3, color="black")
    ax.plot(wl, magnitude, '-k', alpha=0.2)
    for wl1, mag, colors, marker_ in zip(wl, magnitude, color, marker):
        ax.scatter(wl1, mag, color = colors, marker=marker_, s=600, zorder=3)
    plt.text(0.68, 0.86, 'J-PLUS',
            transform=ax.transAxes, fontsize=60,  fontdict=font)
    # plt.text(0.65, 0.86, 'Halo PN',
    #          transform=ax.transAxes, fontsize=60,  fontdict=font)
    # plt.text(0.05, 0.86, '(a)',
    #              transform=ax.transAxes, fontsize=60,  fontdict=font)
    # plt.text(0.80, 0.1, 'SySt',
    #          transform=ax.transAxes, fontsize=60,  fontdict=font)
    # plt.text(0.05, 0.86, '(f)',
    #            transform=ax.transAxes, fontsize=60,  fontdict=font)
    # plt.text(0.62, 0.1, 'H II region',
    #         transform=ax.transAxes, fontsize=60,  fontdict=font)
    # plt.text(0.05, 0.86, '(e)',
    #            transform=ax.transAxes, fontsize=60,  fontdict=font)
    # plt.text(0.73, 0.86, 'QSO',                                   #
    #         transform=ax.transAxes, fontsize=60,  fontdict=font)  #
    # plt.text(0.73, 0.74, 'z = 1.4',                               #QSO
    #         transform=ax.transAxes, fontsize=60,  fontdict=font)  #
    # plt.text(0.05, 0.87, '(k)',                                   #
    #           transform=ax.transAxes, fontsize=60,  fontdict=font)#
    # plt.text(0.80, 0.1, 'YSO',
    #          transform=ax.transAxes, fontsize=60,  fontdict=font)
    # plt.text(0.05, 0.86, '(h)',
    #              transform=ax.transAxes, fontsize=60,  fontdict=font)
    # plt.text(0.70, 0.1, 'B[e] star',
    #            transform=ax.transAxes, fontsize=60,  fontdict=font)
    # plt.text(0.05, 0.9, '(j)',
    #           transform=ax.transAxes, fontsize=60,  fontdict=font)
    # plt.text(0.80, 0.86, 'CV',
    #         transform=ax.transAxes, fontsize=60,  fontdict=font)
    # plt.text(0.05, 0.86, '(i)',
    #              transform=ax.transAxes, fontsize=60,  fontdict=font)

    # plt.text(0.80, 0.1, 'SFG',
    #            transform=ax.transAxes, fontsize=60,  fontdict=font)
    # plt.text(0.05, 0.86, '(n)',                                   #
    #             transform=ax.transAxes, fontsize=60,  fontdict=font)
             
    # plt.text(0.03, 0.89, 'PN model',
    #          transform=ax.transAxes, fontsize=60,  fontdict=font)
    # plt.text(0.03, 0.75, 'High excitation',
    #          transform=ax.transAxes, fontsize=60,  fontdict=font)
    # plt.text(0.03, 0.69, '$\mathrm{L} = 10 \mathrm{X} 10^3 \mathrm{L_{\odot}}$',
    #          transform=ax.transAxes, fontsize=43,  fontdict=font)
    # plt.text(0.03, 0.59, '$\mathrm{N_{e}} = 6 \mathrm{X} 10^3 \mathrm{cm^{-3}}$ ',
    #          transform=ax.transAxes, fontsize=43,  fontdict=font)
    # plt.text(0.88, 0.86, '(d)',
    #            transform=ax.transAxes, fontsize=60,  fontdict=font)

    # plt.text(0.05, 0.25, 'PN model',
    #          transform=ax.transAxes, fontsize=60,  fontdict=font)
    # plt.text(0.05, 0.11, 'Low excitation',
    #          transform=ax.transAxes, fontsize=60,  fontdict=font)
    # plt.text(0.05, 0.15, '$\mathrm{L} = 10 \mathrm{X} 10^3 \mathrm{L_{\odot}}$',
    #          transform=ax.transAxes, fontsize=43,  fontdict=font)
    # plt.text(0.05, 0.05, '$\mathrm{N_{e}} = 1 \mathrm{X} 10^3 \mathrm{cm^{-3}}$ ',
    #          transform=ax.transAxes, fontsize=43,  fontdict=font)
    # plt.text(0.05, 0.86, '(c)',
    #             transform=ax.transAxes, fontsize=60,  fontdict=font)
    
    # plt.text(0.68, 0.24, 'QSO',                                   #
    #         transform=ax.transAxes, fontsize=60,  fontdict=font)  #
    # plt.text(0.68, 0.12, 'z = 2.5',                               #QSO
    #        transform=ax.transAxes, fontsize=60,  fontdict=font)  #
    # plt.text(0.05, 0.86, '(l)',                                   #
    #            transform=ax.transAxes, fontsize=60,  fontdict=font)

    # plt.text(0.75, 0.86, 'QSO',                                   #
    #         transform=ax.transAxes, fontsize=60,  fontdict=font)  #
    # plt.text(0.75, 0.74, 'z = 3.3',                               #QSO
    #         transform=ax.transAxes, fontsize=60,  fontdict=font)  #
    # plt.text(0.05, 0.86, '(m)',                                   #
    #            transform=ax.transAxes, fontsize=60,  fontdict=font)
    
    # plt.text(0.01, 0.86, 'PN of NGC 205 ',
    #          transform=ax.transAxes, fontsize=60,  fontdict=font)
    # plt.text(0.88, 0.86, '(b)',
    #            transform=ax.transAxes, fontsize=60,  fontdict=font)

    # plt.text(0.62, 0.86, 'H II galaxy',
    #          transform=ax.transAxes, fontsize=60,  fontdict=font)
    # plt.text(0.05, 0.86, '(g)',
    #             transform=ax.transAxes, fontsize=60,  fontdict=font)
#plt.margins(0.06)
    #plt.subplots_adjust(bottom=0.19)
    plt.legend(fontsize=20.0)
    #plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.tight_layout()
    plt.gca().invert_yaxis()
    save_path = '../../../Dropbox/JPAS/Tesis/Fig'
    file_save = os.path.join(save_path, plotfile)
    plt.savefig(file_save)
    plt.clf()



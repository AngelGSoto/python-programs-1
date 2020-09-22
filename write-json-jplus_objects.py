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
from collections import OrderedDict
import pandas as pd

Number = []
n = 4
mag_auto  = [[] for _ in range(n)]
mag_ISO_GAUSS = [[] for _ in range(n)]
mag_aper = [[] for _ in range(n)]
mag_auto_WORSTPSF = [[] for _ in range(n)]

#Error
mag_auto_err  = [[] for _ in range(n)]
mag_ISO_GAUSS_err  = [[] for _ in range(n)]

wl = [3485, 3785, 3950, 4100, 4300, 4803, 5150, 6250, 6600, 7660, 8610, 9110]
color = ["#CC00FF", "#9900FF", "#6600FF", "#0000FF", "#009999", "#006600", "#DD8000", "#FF0000", "#CC0066", "#990033", "#660033", "#330034"]
marker = ["s", "o", "o", "o", "o", "s", "o", "s", "o", "s", "o", "s"] ### tienen todos los filtros

wl1 = [ 785, 3950, 4100, 4300, 4803, 5150, 6250, 6600, 7660, 8610, 9110]
color1 = [ "#9900FF", "#6600FF", "#0000FF", "#009999", "#006600", "#DD8000", "#FF0000", "#CC0066", "#990033", "#660033", "#330034"]
marker1 = [ "o", "o", "o", "o", "s", "o", "s", "o", "s", "o", "s"] # No tiene el primer filtro

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

# Dictionary
n = [b for b in range(len(data["id"]))]
#n = ['0', '1', '2', '3']
#n = ['0']
filter_ = ["id",
    "F348",
    "F378",
    "F395",
    "F410",
    "F430",
    "F480_g_sdss",
    "F515",
    "F625_r_sdss",
    "F660",
    "F766_i_sdss",
    "F861",
    "F911_z_sdss"]

magn = OrderedDict({i.capitalize():{filter_s:[] for filter_s in filter_} for i in str(n)})

# for i in n:
#     magn[i]['id'] = i
#     print(magn[i]['id'])
# sys.exit()
for ii in range(len(data["id"])):
    for i in n:
        magn[i]["id"] =  str(data["id"][ii])+"-DR1jplus"
        magn[i]["F348"] = data["uJAVA_MAG_APER_6_0"][ii]
        magn[i]["F378"] = data["J0378_MAG_APER_6_0"][ii]
        magn[i]["F395"] = data["J0395_MAG_APER_6_0"][ii]
        magn[i]["F410"] = data["J0410_MAG_APER_6_0"][ii]
        magn[i]["F430"] = data["J0430_MAG_APER_6_0"][ii]
        magn[i]["F480_g_sdss"] = data["gSDSS_MAG_APER_6_0"][ii]
        magn[i]["F515"] = data["J0515_MAG_APER_6_0"][ii] 
        magn[i]["F625_r_sdss"] = data["rSDSS_MAG_APER_6_0"][ii] 
        magn[i]["F660"] = data["J0660_MAG_APER_6_0"][ii]
        magn[i]["F766_i_sdss"] = data["iSDSS_MAG_APER_6_0"][ii] 
        magn[i]["F861"] = data["J0861_MAG_APER_6_0"][ii] 
        magn[i]["F911_z_sdss"] = data["zSDSS_MAG_APER_6_0"][ii]
sys.exit()        
#Creates The JSON files with the magnitudes
        jsonfile = str(data["id"][ii])+"-JPLUS17-magnitude.json"
        with open(jsonfile, "w") as f:
            json.dump(magn[i], f, indent=4)    

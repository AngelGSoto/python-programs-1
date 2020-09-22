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

# Number = []
# n = 4
# mag_auto  = [[] for _ in range(n)]
# mag_ISO_GAUSS = [[] for _ in range(n)]
# mag_aper = [[] for _ in range(n)]
# mag_auto_WORSTPSF = [[] for _ in range(n)]

# #Error
# mag_auto_err  = [[] for _ in range(n)]
# mag_ISO_GAUSS_err  = [[] for _ in range(n)]

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

#filer deep splus mask
f_err = data["uJAVA_ISO_GAUSS_err"] <= 0.2
f1_err = data["J0378_ISO_GAUSS_err"] <= 0.2
f2_err = data["J0395_ISO_GAUSS_err"] < 0.2
f3_err = data["J0410_ISO_GAUSS_err"] <= 0.2
f4_err = data["J0430_ISO_GAUSS_err"] < 0.2
f5_err =  data["gSDSS_ISO_GAUSS_err"] <= 0.2
f6_err = data["J0515_ISO_GAUSS_err"] <= 0.2
f7_err = data["rSDSS_ISO_GAUSS_err"] <= 0.2
f8_err = data["J0660_ISO_GAUSS_err"] <= 0.2
f9_err =  data["iSDSS_ISO_GAUSS_err"] <= 0.2
f10_err = data["J0861_ISO_GAUSS_err"] <= 0.2
f11_err = data["zSDSS_ISO_GAUSS_err"] <= 0.2

f_r = data["rSDSS_ISO_GAUSS"] <= 19
m = data['PhotoFlag'] == 0.0

mask = f_r & m & f1_err & f2_err & f3_err & f4_err & f5_err & f6_err & f7_err & f8_err & f9_err & f10_err & f11_err  

# Dictionary
n = len(data["id"][mask])
#n = ['0', '1', '2', '3']
#n = ['0']

filter_ = ["id",
    "F348_U",
    "F378",
    "F395",
    "F410",
    "F430",
    "F480_G",
    "F515",
    "F625_R",
    "F660",
    "F766_I",
    "F861",
    "F911_Z"]

#Multyple disctionaly longitud of len(data["id"])
magn = OrderedDict({i:{filter_s:[] for filter_s in filter_} for i in range(n)})

for ii in range(n):
    magn[ii]["id"] =  str(data["id"][ii])+"-DR1SplusWDs"
    magn[ii]["F348_U"] = data["uJAVA_ISO_GAUSS"][mask][ii]
    magn[ii]["F378"] = data["J0378_ISO_GAUSS"][mask][ii]
    magn[ii]["F395"] = data["J0395_ISO_GAUSS"][mask][ii]
    magn[ii]["F410"] = data["J0410_ISO_GAUSS"][mask][ii]
    magn[ii]["F430"] = data["J0430_ISO_GAUSS"][mask][ii]
    magn[ii]["F480_G"] = data["gSDSS_ISO_GAUSS"][mask][ii]
    magn[ii]["F515"] = data["J0515_ISO_GAUSS"][mask][ii] 
    magn[ii]["F625_R"] = data["rSDSS_ISO_GAUSS"][mask][ii] 
    magn[ii]["F660"] = data["J0660_ISO_GAUSS"][mask][ii]
    magn[ii]["F766_I"] = data["iSDSS_ISO_GAUSS"][mask][ii] 
    magn[ii]["F861"] = data["J0861_ISO_GAUSS"][mask][ii] 
    magn[ii]["F911_Z"] = data["zSDSS_ISO_GAUSS"][mask][ii]
       
#Creates The JSON files with the magnitudes
    jsonfile = str(data["id"][ii])+"-SPLUS18-magnitude.json"
    with open(jsonfile, "w") as f:
        json.dump(magn[ii], f, indent=4)    

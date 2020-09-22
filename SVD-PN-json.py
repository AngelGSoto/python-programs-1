'''
Make photo spectra
'''
from __future__ import print_function
import numpy as np
import glob
import json
import matplotlib.pyplot as plt
#import seaborn as sns
import sys
import os
import argparse
import os
from colour import Color
from collections import OrderedDict
import pandas as pd

X_h4 = []
X_p35 = []
err_zp_h4 = [0.128,  0.020,  0.061,  0.029,  0.067,  0.036,  0.044,  0.042, 0.043,  0.048,  0.030, 0.092]
err_zp_pn135 =[ 0.102, 0.0,  0.115,  0.103,  0.127, 0.073,  0.073,  0.073, 0.078,  0.071,  0.070,  0.100]
filters = []
S_h41 = []
S_135 = []
filter_name = ['uJAVA', 'J0378', 'J0395', 'J0410', 'J0430', 'gSDSS', 'J0515', 'rSDSS', 'J0660', 'iSDSS', 'J0861', 'zSDSS']
for a in range(1, 13):
    filters.append(a)

wl = [3485, 3785, 3950, 4100, 4300, 4803, 5150, 6250, 6600, 7660, 8610, 9110]
color= ["#CC00FF", "#9900FF", "#6600FF", "#0000FF", "#009999", "#006600", "#DD8000", "#FF0000", "#CC0066", "#990033", "#660033", "#330034"]
marker = ["s", "o", "o", "o", "o", "s", "o", "s", "o", "s", "o", "s"]

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

magn = OrderedDict({filter_s:[] for filter_s in filter_})

# The PNe H4 1
pattern = "../JPLUS-data/H4-1-phot/*6pix.json"
file_list = glob.glob(pattern)
for file_name in file_list:
    with open(file_name) as f:
        data = json.load(f)
    magn["id"] =  "H-41-hPNe-SVD"
    magn["F348"] = data["J0348_uJAVA"]-25+20.955
    magn["F378"] = data["J0378"]-25+20.361
    magn["F395"] = data["J0395"]-25+20.094
    magn["F410"] = data["J0410"]-25+20.971
    magn["F430"] = data["J0430"]-25+21.079
    magn["F480_g_sdss"]  = data["J0480_gSDSS"]-25+23.297
    magn["F515"] = data["J0515"]-25+21.193
    magn["F625_r_sdss"] = data["J0625_rSDSS"]-25+23.335
    magn["F660"] = data["J0660"]-25+20.859
    magn["F766_i_sdss"] = data["J0766_iSDSS"]-25+23.122
    magn["F861"] = data["J0861"]-25+21.410
    magn["F911_z_sdss"] = data["J0911_zSDSS"]-25+22.562
    
#error propagation
err_h41 = []
for i in err_zp_h4:
    err_h4 = np.sqrt(i**2)
    err_h41.append(err_h4)

## PNG 135
magn1 = OrderedDict({filter_s:[] for filter_s in filter_})

pattern1 = "../JPLUS-data/PNG135coadded-phot/*6pix.json"
file_list1 = glob.glob(pattern1)
for file_name1 in file_list1:
    with open(file_name1) as f1:
        data = json.load(f1)
    magn1["id"] =  "PNG135-hPN-SVD"
    magn1["F348"] = data["J0348_uJAVA"]-25+20.996
    magn1["F378"] = data["J0378"]-25+20.376
    magn1["F395"] = data["J0395"]-25+20.130
    magn1["F410"] = data["J0410"]-25+21.102
    magn1["F430"] = data["J0430"]-25+21.218
    magn1["F480_g_sdss"] = data["J0480_gSDSS"]-25+23.425
    magn1["F515"] = data["J0515"]-25+21.444
    magn1["F625_r_sdss"] = data["J0625_rSDSS"]-25+23.565
    magn1["F660"] = data["J0660"]-25+21.058
    magn1["F766_i_sdss"] = data["J0766_iSDSS"]-25+23.255
    magn1["F861"] = data["J0861"]-25+21.534
    magn1["F911_z_sdss"] = data["J0911_zSDSS"]-25+22.535

jsonfile = "H4-1-SVD-JPLUS17-magnitude.json"
with open(jsonfile, "w") as f:
    json.dump(magn, f, indent=4)    

jsonfile1 = "PNG135-SVD-JPLUS17-magnitude.json"
with open(jsonfile1, "w") as f1:
    json.dump(magn1, f1, indent=4)    

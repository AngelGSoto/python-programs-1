from astropy.io import fits
import os
import glob
import json
import argparse
import matplotlib.pyplot as plt
import pandas as pd
#import StringIO
from astropy.table import Table
from astropy.io import ascii
import sys
import numpy as np

#create list with the magnitudes
n = 77
magnitude = [[] for _ in range(n)]

parser = argparse.ArgumentParser(
    description="""Write wave and flux of a spectrum""")

parser.add_argument("source", type=str,
                    default="table-6mil-obj-jplus",
                    help="Name of source, taken the prefix ")
parser.add_argument("--savefile", action="store_true",
                    help="Save ascii file showing the magnitude")


parser.add_argument("--debug", action="store_true",
                    help="Print out verbose debugging info about each line in region file")

args = parser.parse_args()
file_ = args.source + ".dat"

def mag(type_mag):
    dta = tab[type_mag]
    dta = pd.Series(dta)
    dta_exp = dta.str.split(' ', expand=True)
    return dta_exp

#Read files
tab = ascii.read(file_)

Tile = tab["TILE_ID"]
Number = tab["NUMBER"]
RA = tab["ALPHA_J2000"]
DEC = tab["DELTA_J2000"]
r_auto = mag("MAG_AUTO")[0]
g_auto = mag("MAG_AUTO")[1]
i_auto = mag("MAG_AUTO")[2]
z_auto = mag("MAG_AUTO")[3]
uJAVA_auto = mag("MAG_AUTO")[4]
J0378_auto = mag("MAG_AUTO")[5]
J0395_auto = mag("MAG_AUTO")[6]
J0410_auto = mag("MAG_AUTO")[7]
J0430_auto = mag("MAG_AUTO")[8]
J0515_auto = mag("MAG_AUTO")[9]
J0660_auto = mag("MAG_AUTO")[10]
J0861_auto = mag("MAG_AUTO")[11]
r_MAG_ISO_GAUSS = mag("MAG_ISO_GAUSS")[0]
g_MAG_ISO_GAUSS = mag("MAG_ISO_GAUSS")[1]
i_MAG_ISO_GAUSS = mag("MAG_ISO_GAUSS")[2]
z_MAG_ISO_GAUSS = mag("MAG_ISO_GAUSS")[3]
uJAVA_MAG_ISO_GAUSS = mag("MAG_ISO_GAUSS")[4]
J0378_MAG_ISO_GAUSS = mag("MAG_ISO_GAUSS")[5]
J0395_MAG_ISO_GAUSS = mag("MAG_ISO_GAUSS")[6]
J0410_MAG_ISO_GAUSS = mag("MAG_ISO_GAUSS")[7]
J0430_MAG_ISO_GAUSS = mag("MAG_ISO_GAUSS")[8]
J0515_MAG_ISO_GAUSS = mag("MAG_ISO_GAUSS")[9]
J0660_MAG_ISO_GAUSS = mag("MAG_ISO_GAUSS")[10]
J0861_MAG_ISO_GAUSS = mag("MAG_ISO_GAUSS")[11]
r_MAG_APER_6_0 = mag("MAG_APER_6_0")[0]
g_MAG_APER_6_0 = mag("MAG_APER_6_0")[1]
i_MAG_APER_6_0 = mag("MAG_APER_6_0")[2]
z_MAG_APER_6_0 = mag("MAG_APER_6_0")[3]
uJAVA_MAG_APER_6_0 = mag("MAG_APER_6_0")[4]
J0378_MAG_APER_6_0 = mag("MAG_APER_6_0")[5]
J0395_MAG_APER_6_0 = mag("MAG_APER_6_0")[6]
J0410_MAG_APER_6_0 = mag("MAG_APER_6_0")[7]
J0430_MAG_APER_6_0 = mag("MAG_APER_6_0")[8]
J0515_MAG_APER_6_0 = mag("MAG_APER_6_0")[9]
J0660_MAG_APER_6_0 = mag("MAG_APER_6_0")[10]
J0861_MAG_APER_6_0 = mag("MAG_APER_6_0")[11]

#ERROR
r_auto_err = mag("MAG_ERR_AUTO")[0]
g_auto_err = mag("MAG_ERR_AUTO")[1]
i_auto_err = mag("MAG_ERR_AUTO")[2]
z_auto_err = mag("MAG_ERR_AUTO")[3]
uJAVA_auto_err = mag("MAG_ERR_AUTO")[4]
J0378_auto_err = mag("MAG_ERR_AUTO")[5]
J0395_auto_err = mag("MAG_ERR_AUTO")[6]
J0410_auto_err = mag("MAG_ERR_AUTO")[7]
J0430_auto_err = mag("MAG_ERR_AUTO")[8]
J0515_auto_err = mag("MAG_ERR_AUTO")[9]
J0660_auto_err = mag("MAG_ERR_AUTO")[10]
J0861_auto_err = mag("MAG_ERR_AUTO")[11]
r_MAG_ISO_GAUSS_ERR  = mag("MAG_ERR_ISO_GAUSS")[0]
g_MAG_ISO_GAUSS_ERR = mag("MAG_ERR_ISO_GAUSS")[1]
i_MAG_ISO_GAUSS_ERR = mag("MAG_ERR_ISO_GAUSS")[2]
z_MAG_ISO_GAUSS_ERR = mag("MAG_ERR_ISO_GAUSS")[3]
# try:
#     uJAVA_MAG_ISO_GAUSS_ERR = mag("MAG_ERR_ISO_GAUS")[4]
# except KeyError:
#     None
uJAVA_MAG_ISO_GAUSS_ERR = mag("MAG_ERR_ISO_GAUSS")[4]
J0378_MAG_ISO_GAUSS_ERR = mag("MAG_ERR_ISO_GAUSS")[5]
J0395_MAG_ISO_GAUSS_ERR = mag("MAG_ERR_ISO_GAUSS")[6]
J0410_MAG_ISO_GAUSS_ERR = mag("MAG_ERR_ISO_GAUSS")[7]
J0430_MAG_ISO_GAUSS_ERR = mag("MAG_ERR_ISO_GAUSS")[8]
J0515_MAG_ISO_GAUSS_ERR = mag("MAG_ERR_ISO_GAUSS")[9]
J0660_MAG_ISO_GAUSS_ERR = mag("MAG_ERR_ISO_GAUSS")[10]
J0861_MAG_ISO_GAUSS_ERR = mag("MAG_ERR_ISO_GAUSS")[11]
r_MAG_APER_6_0_err = mag("MAG_ERR_APER_6_0")[0]
g_MAG_APER_6_0_err = mag("MAG_ERR_APER_6_0")[1]
i_MAG_APER_6_0_err = mag("MAG_ERR_APER_6_0")[2]
z_MAG_APER_6_0_err = mag("MAG_ERR_APER_6_0")[3]
uJAVA_MAG_APER_6_0_err = mag("MAG_ERR_APER_6_0")[4]
J0378_MAG_APER_6_0_err = mag("MAG_ERR_APER_6_0")[5]
J0395_MAG_APER_6_0_err = mag("MAG_ERR_APER_6_0")[6]
J0410_MAG_APER_6_0_err = mag("MAG_ERR_APER_6_0")[7]
J0430_MAG_APER_6_0_err = mag("MAG_ERR_APER_6_0")[8]
J0515_MAG_APER_6_0_err = mag("MAG_ERR_APER_6_0")[9]
J0660_MAG_APER_6_0_err = mag("MAG_ERR_APER_6_0")[10]
J0861_MAG_APER_6_0_err = mag("MAG_ERR_APER_6_0")[11]


#Crearting the table
#table = Table([Tile, Number, RA, DEC, r_auto, g_auto, i_auto, z_auto, uJAVA_auto, J0378_auto, J0395_auto,  J0410_auto , J0430_auto, J0515_auto, J0660_auto, J0861_auto, r_MAG_ISO_GAUSS, g_MAG_ISO_GAUSS, i_MAG_ISO_GAUSS, z_MAG_ISO_GAUSS, uJAVA_MAG_ISO_GAUSS, J0378_MAG_ISO_GAUSS, J0395_MAG_ISO_GAUSS,  J0410_MAG_ISO_GAUSS , J0430_MAG_ISO_GAUSS, J0515_MAG_ISO_GAUSS, J0660_MAG_ISO_GAUSS, J0861_MAG_ISO_GAUSS, r_MAG_APER_6_0, g_MAG_APER_6_0, i_MAG_APER_6_0, z_MAG_APER_6_0, uJAVA_MAG_APER_6_0, J0378_MAG_APER_6_0, J0395_MAG_APER_6_0,  J0410_MAG_APER_6_0 , J0430_MAG_APER_6_0, J0515_MAG_APER_6_0, J0660_MAG_APER_6_0, J0861_MAG_APER_6_0, r_auto_err, g_auto_err, i_auto_err, z_auto_err, uJAVA_auto_err, J0378_auto_err, J0395_auto_err,  J0410_auto_err , J0430_auto_err, J0515_auto_err, J0660_auto_err, J0861_auto_err, r_MAG_ISO_GAUSS_ERR, g_MAG_ISO_GAUSS_ERR, i_MAG_ISO_GAUSS_ERR, z_MAG_ISO_GAUSS_ERR, uJAVA_MAG_ISO_GAUSS_ERR, J0378_MAG_ISO_GAUSS_ERR, J0395_MAG_ISO_GAUSS_ERR,  J0410_MAG_ISO_GAUSS_ERR , J0430_MAG_ISO_GAUSS_ERR, J0515_MAG_ISO_GAUSS_ERR, J0660_MAG_ISO_GAUSS_ERR, J0861_MAG_ISO_GAUSS_ERR, r_MAG_APER_6_0_err, g_MAG_APER_6_0_err, i_MAG_APER_6_0_err, z_MAG_APER_6_0_err, uJAVA_MAG_APER_6_0_err, J0378_MAG_APER_6_0_err, J0395_MAG_APER_6_0_err,  J0410_MAG_APER_6_0_err , J0430_MAG_APER_6_0_err, J0515_MAG_APER_6_0_err, J0660_MAG_APER_6_0_err, J0861_MAG_APER_6_0_err], names=('Tile', 'Number', 'RA', 'Dec', 'rSDSS_auto', 'gSDSS_auto', 'iSDSS_auto', 'zSDSS_auto', 'uJAVA_auto', 'J0378_auto', 'J0395_auto', 'J0410_auto', 'J0430_auto', 'J0515_auto', 'J0660_auto', 'J0861_auto', 'rSDSS_ISO_GAUSS', 'gSDSS_ISO_GAUSS', 'iSDSS_ISO_GAUSS', 'zSDSS_ISO_GAUSS', 'uJAVA_ISO_GAUSS', 'J0378_ISO_GAUSS', 'J0395_ISO_GAUSS', 'J0410_ISO_GAUSS', 'J0430_ISO_GAUSS', 'J0515_ISO_GAUSS', 'J0660_ISO_GAUSS', 'J0861_ISO_GAUSS', 'rSDSS_MAG_APER_6_0', 'gSDSS_MAG_APER_6_0', 'iSDSS_MAG_APER_6_0', 'zSDSS_MAG_APER_6_0', 'uJAVA_MAG_APER_6_0', 'J0378_MAG_APER_6_0', 'J0395_MAG_APER_6_0', 'J0410_MAG_APER_6_0', 'J0430_MAG_APER_6_0', 'J0515_MAG_APER_6_0', 'J0660_MAG_APER_6_0', 'J0861_MAG_APER_6_0', 'rSDSS_auto_err', 'gSDSS_auto_err', 'iSDSS_auto_err', 'zSDSS_auto_err', 'uJAVA_auto_err', 'J0378_auto_err', 'J0395_auto_err', 'J0410_auto_err', 'J0430_auto_err', 'J0515_auto_err', 'J0660_auto_err', 'J0861_auto_err',  'rSDSS_ISO_GAUSS_err', 'gSDSS_ISO_GAUSS_err', 'iSDSS_ISO_GAUSS_err', 'zSDSS_ISO_GAUSS_err', 'uJAVA_ISO_GAUSS_err', 'J0378_ISO_GAUSS_err', 'J0395_ISO_GAUSS_err', 'J0410_ISO_GAUSS_err', 'J0430_ISO_GAUSS_err', 'J0515_ISO_GAUSS_err', 'J0660_ISO_GAUSS_err', 'J0861_ISO_GAUSS_err', 'rSDSS_MAG_APER_6_0_err', 'gSDSS_MAG_APER_6_0_err', 'iSDSS_MAG_APER_6_0_err', 'zSDSS_MAG_APER_6_0_err', 'uJAVA_MAG_APER_6_0_err', 'J0378_MAG_APER_6_0_err', 'J0395_MAG_APER_6_0_err', 'J0410_MAG_APER_6_0_err', 'J0430_MAG_APER_6_0_err', 'J0515_MAG_APER_6_0_err', 'J0660_MAG_APER_6_0_err', 'J0861_MAG_APER_6_0_err'), meta={'name': 'first table'})  

table = Table([Tile, Number, RA, DEC, r_auto, g_auto, i_auto, z_auto, uJAVA_auto, J0378_auto, J0395_auto,  J0410_auto , J0430_auto, J0515_auto, J0660_auto, J0861_auto, r_MAG_ISO_GAUSS, g_MAG_ISO_GAUSS, i_MAG_ISO_GAUSS, z_MAG_ISO_GAUSS, uJAVA_MAG_ISO_GAUSS, J0378_MAG_ISO_GAUSS, J0395_MAG_ISO_GAUSS,  J0410_MAG_ISO_GAUSS , J0430_MAG_ISO_GAUSS, J0515_MAG_ISO_GAUSS, J0660_MAG_ISO_GAUSS, J0861_MAG_ISO_GAUSS, r_MAG_APER_6_0, g_MAG_APER_6_0, i_MAG_APER_6_0, z_MAG_APER_6_0, uJAVA_MAG_APER_6_0, J0378_MAG_APER_6_0, J0395_MAG_APER_6_0,  J0410_MAG_APER_6_0 , J0430_MAG_APER_6_0, J0515_MAG_APER_6_0, J0660_MAG_APER_6_0, J0861_MAG_APER_6_0, r_auto_err, g_auto_err, i_auto_err, z_auto_err, uJAVA_auto_err, J0378_auto_err, J0395_auto_err,  J0410_auto_err, J0430_auto_err, J0515_auto_err, J0660_auto_err, J0861_auto_err, r_MAG_ISO_GAUSS_ERR, g_MAG_ISO_GAUSS_ERR, i_MAG_ISO_GAUSS_ERR, z_MAG_ISO_GAUSS_ERR, uJAVA_MAG_ISO_GAUSS_ERR, J0378_MAG_ISO_GAUSS_ERR, J0395_MAG_ISO_GAUSS_ERR, J0410_MAG_ISO_GAUSS_ERR , J0430_MAG_ISO_GAUSS_ERR, J0515_MAG_ISO_GAUSS_ERR, J0660_MAG_ISO_GAUSS_ERR, J0861_MAG_ISO_GAUSS_ERR,  r_MAG_APER_6_0_err, g_MAG_APER_6_0_err, i_MAG_APER_6_0_err, z_MAG_APER_6_0_err, uJAVA_MAG_APER_6_0_err, J0378_MAG_APER_6_0_err, J0395_MAG_APER_6_0_err,  J0410_MAG_APER_6_0_err , J0430_MAG_APER_6_0_err, J0515_MAG_APER_6_0_err, J0660_MAG_APER_6_0_err, J0861_MAG_APER_6_0_err], names=('Tile', 'Number', 'RA', 'Dec', 'rSDSS_auto', 'gSDSS_auto', 'iSDSS_auto', 'zSDSS_auto', 'uJAVA_auto', 'J0378_auto', 'J0395_auto', 'J0410_auto', 'J0430_auto', 'J0515_auto', 'J0660_auto', 'J0861_auto', 'rSDSS_ISO_GAUSS', 'gSDSS_ISO_GAUSS', 'iSDSS_ISO_GAUSS', 'zSDSS_ISO_GAUSS', 'uJAVA_ISO_GAUSS', 'J0378_ISO_GAUSS', 'J0395_ISO_GAUSS', 'J0410_ISO_GAUSS', 'J0430_ISO_GAUSS', 'J0515_ISO_GAUSS', 'J0660_ISO_GAUSS', 'J0861_ISO_GAUSS', 'rSDSS_MAG_APER_6_0', 'gSDSS_MAG_APER_6_0', 'iSDSS_MAG_APER_6_0', 'zSDSS_MAG_APER_6_0', 'uJAVA_MAG_APER_6_0', 'J0378_MAG_APER_6_0', 'J0395_MAG_APER_6_0', 'J0410_MAG_APER_6_0', 'J0430_MAG_APER_6_0', 'J0515_MAG_APER_6_0', 'J0660_MAG_APER_6_0', 'J0861_MAG_APER_6_0', 'rSDSS_auto_err', 'gSDSS_auto_err', 'iSDSS_auto_err', 'zSDSS_auto_err', 'uJAVA_auto_err', 'J0378_auto_err', 'J0395_auto_err', 'J0410_auto_err', 'J0430_auto_err', 'J0515_auto_err', 'J0660_auto_err', 'J0861_auto_err',  'rSDSS_ISO_GAUSS_err', 'gSDSS_ISO_GAUSS_err', 'iSDSS_ISO_GAUSS_err', 'zSDSS_ISO_GAUSS_err', 'uJAVA_ISO_GAUSS_err', 'J0378_ISO_GAUSS_err', 'J0395_ISO_GAUSS_err', 'J0410_ISO_GAUSS_err', 'J0430_ISO_GAUSS_err', 'J0515_ISO_GAUSS_err', 'J0660_ISO_GAUSS_err', 'J0861_ISO_GAUSS_err','rSDSS_MAG_APER_6_0_err', 'gSDSS_MAG_APER_6_0_err', 'iSDSS_MAG_APER_6_0_err', 'zSDSS_MAG_APER_6_0_err', 'uJAVA_MAG_APER_6_0_err', 'J0378_MAG_APER_6_0_err', 'J0395_MAG_APER_6_0_err', 'J0410_MAG_APER_6_0_err', 'J0430_MAG_APER_6_0_err', 'J0515_MAG_APER_6_0_err', 'J0660_MAG_APER_6_0_err', 'J0861_MAG_APER_6_0_err'), meta={'name': 'first table'})  

#Saving resultated table
if args.savefile:
    asciifile = file_.replace(".dat", ".tab")
    table.write(asciifile, format="ascii.tab")


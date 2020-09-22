from astropy.io import fits
import os
import glob
import json
import argparse
import matplotlib.pyplot as plt
import pandas as pd
#import StringIO
from astropy.table import Table
import sys

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

f = open(file_, 'r')
header1 = f.readline()
for line in f:
    line = line.strip()
    columns = line.split()
    magnitude[0].append(columns[0])
    magnitude[1].append(columns[1])
    magnitude[2].append(columns[2])
    magnitude[3].append(columns[3])
    magnitude[4].append(columns[17].split('"')[-1]) #auto
    magnitude[5].append(columns[18])
    magnitude[6].append(columns[19])
    magnitude[7].append(columns[20])
    magnitude[8].append(columns[21])
    magnitude[9].append(columns[22])
    magnitude[10].append(columns[23])
    magnitude[11].append(columns[24])
    magnitude[12].append(columns[25])
    magnitude[13].append(columns[26])
    magnitude[14].append(columns[27])
    magnitude[15].append(columns[28].split('"')[0])
    magnitude[16].append(columns[29].split('"')[-1]) # ISO
    magnitude[17].append(columns[30])
    magnitude[18].append(columns[31])
    magnitude[19].append(columns[32])
    magnitude[20].append(columns[33])
    magnitude[21].append(columns[34])
    magnitude[22].append(columns[35])
    magnitude[23].append(columns[36])
    magnitude[24].append(columns[37])
    magnitude[25].append(columns[38])
    magnitude[26].append(columns[39])
    magnitude[27].append(columns[40].split('"')[0])
    magnitude[28].append(columns[41].split('"')[-1]) #petro
    magnitude[29].append(columns[42])
    magnitude[30].append(columns[43])
    magnitude[31].append(columns[44])
    magnitude[32].append(columns[45])
    magnitude[33].append(columns[46])
    magnitude[34].append(columns[47])
    magnitude[35].append(columns[48])
    magnitude[36].append(columns[49])
    magnitude[37].append(columns[50])
    magnitude[38].append(columns[51])
    magnitude[39].append(columns[52].split('"')[0])
    magnitude[40].append(columns[163].split('"')[-1]) # Aper_6.0
    magnitude[41].append(columns[164])
    magnitude[42].append(columns[165])
    magnitude[43].append(columns[166])
    magnitude[44].append(columns[167])
    magnitude[45].append(columns[168])
    magnitude[46].append(columns[169])
    magnitude[47].append(columns[170])
    magnitude[48].append(columns[171])
    magnitude[49].append(columns[172])
    magnitude[50].append(columns[173])
    magnitude[51].append(columns[174].split('"')[0])
    magnitude[52].append(columns[403].split('"')[-1])
    magnitude[53].append(columns[404])
    magnitude[54].append(columns[405])
    magnitude[55].append(columns[406])
    magnitude[56].append(columns[407])
    magnitude[57].append(columns[408])
    magnitude[58].append(columns[409])
    magnitude[59].append(columns[410])
    magnitude[60].append(columns[411])
    magnitude[61].append(columns[412])
    magnitude[62].append(columns[413])
    magnitude[63].append(columns[414].split('"')[0])
    magnitude[64].append(columns[175].split('"')[-1]) # error AUTO
    magnitude[65].append(columns[176])
    magnitude[66].append(columns[177])
    magnitude[67].append(columns[178])
    magnitude[68].append(columns[179])
    magnitude[69].append(columns[180])
    magnitude[70].append(columns[181])
    magnitude[71].append(columns[182])
    magnitude[72].append(columns[183])
    magnitude[73].append(columns[184])
    magnitude[74].append(columns[185])
    magnitude[75].append(columns[186].split('"')[0])
    magnitude[76].append(columns[175].split('"')[-1]) # error ISO_GAUS
    magnitude[77].append(columns[176])
    magnitude[78].append(columns[177])
    magnitude[79].append(columns[178])
    magnitude[80].append(columns[179])
    magnitude[81].append(columns[180])
    magnitude[82].append(columns[181])
    magnitude[83].append(columns[182])
    magnitude[84].append(columns[183])
    magnitude[85].append(columns[184])
    magnitude[86].append(columns[185])
    magnitude[87].append(columns[186].split('"')[0])
    
    magnitude[76].append(columns[16])#Class Star
    # magnitude[53].append(columns[2])
    # magnitude[54].append(columns[4]) # Status from HASH

#Crearting the table   
table = Table([magnitude[0], magnitude[1], magnitude[2], magnitude[3], magnitude[4], magnitude[5], magnitude[6], magnitude[7], magnitude[8], magnitude[9], magnitude[10], magnitude[11], magnitude[12], magnitude[13], magnitude[14], magnitude[15], magnitude[16], magnitude[17], magnitude[18], magnitude[19], magnitude[20], magnitude[21], magnitude[22], magnitude[23], magnitude[24], magnitude[25], magnitude[26], magnitude[27], magnitude[28], magnitude[29], magnitude[30], magnitude[31], magnitude[32], magnitude[33], magnitude[34], magnitude[35], magnitude[36], magnitude[37], magnitude[38], magnitude[39], magnitude[40], magnitude[41], magnitude[42], magnitude[43], magnitude[44], magnitude[45], magnitude[46], magnitude[47], magnitude[48], magnitude[49], magnitude[50], magnitude[51], magnitude[52], magnitude[53], magnitude[54], magnitude[55], magnitude[56], magnitude[57], magnitude[58], magnitude[59], magnitude[60], magnitude[61], magnitude[62], magnitude[63], magnitude[64], magnitude[65], magnitude[66], magnitude[67], magnitude[68], magnitude[69], magnitude[70], magnitude[71], magnitude[72], magnitude[73], magnitude[74], magnitude[75], magnitude[76]], names=('Tile', 'Number', 'RA', 'Dec', 'rSDSS_auto', 'gSDSS_auto', 'iSDSS_auto', 'zSDSS_auto', 'uJAVA_auto', 'J0378_auto', 'J0395_auto', 'J0410_auto', 'J0430_auto', 'J0515_auto', 'J0660_auto', 'J0861_auto', 'rSDSS_ISO', 'gSDSS_ISO', 'iSDSS_ISO', 'zSDSS_ISO', 'uJAVA_ISO', 'J0378_ISO', 'J0395_ISO', 'J0410_ISO', 'J0430_ISO', 'J0515_ISO', 'J0660_ISO', 'J0861_ISO', 'rSDSS_petro', 'gSDSS_petro', 'iSDSS_petro', 'zSDSS_petro', 'uJAVA_petro', 'J0378_petro', 'J0395_petro', 'J0410_petro', 'J0430_petro', 'J0515_petro', 'J0660_petro', 'J0861_petro', 'rSDSS_60', 'gSDSS_60', 'iSDSS_60', 'zSDSS_60', 'uJAVA_60', 'J0378_60', 'J0395_60', 'J0410_60', 'J0430_60', 'J0515_60', 'J0660_60', 'J0861_60', 'rSDSS_3_WORSTPSF', 'gSDSS_3_WORSTPSF', 'iSDSS_3_WORSTPSF', 'zSDSS_3_WORSTPSF', 'uJAVA_3_WORSTPSF', 'J0378_3_WORSTPSF', 'J0395_3_WORSTPSF', 'J0410_3_WORSTPSF', 'J0430_3_WORSTPSF', 'J0515_3_WORSTPSF', 'J0660_3_WORSTPSF', 'J0861_3_WORSTPSF', 'rSDSS_auto_err', 'gSDSS_auto_err', 'iSDSS_auto_err', 'zSDSS_auto_err', 'uJAVA_auto_err', 'J0378_auto_err', 'J0395_auto_err', 'J0410_auto_err', 'J0430_auto_err', 'J0515_auto_err', 'J0660_auto_err', 'J0861_auto_err', 'Class star'), meta={'name': 'first table'})  

#Saving resultated table
if args.savefile:
    asciifile = file_.replace(".dat", ".tab")
    table.write(asciifile, format="ascii.tab")
